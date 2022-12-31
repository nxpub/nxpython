import re
import contextlib

from enum import IntFlag, auto

from pycparser import c_ast


class Context(IntFlag):
    FuncDef = auto()
    FuncBody = auto()
    FuncArgs = auto()


# TODO: Better interface for string building (emit), blocks and so on
class PyGenerator:
    """
    Uses the same visitor pattern as c_ast.NodeVisitor, but modified to
    return a value from each visit method, using string accumulation in
    generic_visit.
    """

    DEFAULT_INDENT = ' ' * 4

    def __init__(self, reduce_parentheses=False, pragma_begin: bool = True):
        # Statements start with indentation of self.indent_level spaces, using
        # the _make_indent method.
        self._state = 0
        self._parent = None
        self._begin = not pragma_begin
        self.indent_level = 0
        self.reduce_parentheses = reduce_parentheses

    @contextlib.contextmanager
    def indent(self):
        self.indent_level += 1
        yield
        self.indent_level -= 1

    def _make_indent(self):
        return self.DEFAULT_INDENT * self.indent_level

    def visit(self, node, *, flag: Context = None):
        method = 'visit_' + node.__class__.__name__
        if flag:
            self._state |= flag
        ret = getattr(self, method, self.generic_visit)(node)
        if flag:
            self._state &= ~flag
        return ret

    def generic_visit(self, node):
        if node is None:
            return ''
        else:
            return ''.join(self.visit(c) for c_name, c in node.children())

    RE_LITERAL_SUFFIX = re.compile(r'^([0-9a-f.x]+)(ull|ll|ul|l|uz|u|z)$', re.IGNORECASE)

    def _convert_literal(self, value: str) -> str:
        # TODO: Check literal strings
        stripped = self.RE_LITERAL_SUFFIX.sub(r'\1', value)
        if '.' in stripped and stripped[-1] == 'f':
            stripped = stripped[:-1]
        return stripped

    def visit_Constant(self, n):
        return self._convert_literal(n.value)

    def visit_ID(self, n):
        return n.name

    def visit_Pragma(self, n):
        ret = '#pragma'
        if n.string:
            if n.string == '__begin__':
                self._begin = True
                return ''
            ret += ' ' + n.string
        return ret

    def visit_ArrayRef(self, n):
        arrref = self._parenthesize_unless_simple(n.name)
        return arrref + '[' + self.visit(n.subscript) + ']'

    def visit_StructRef(self, n):
        sref = self._parenthesize_unless_simple(n.name)
        ref_type = n.type
        # TODO: Check other types, we're good with '.' only
        if ref_type == '->':
            ref_type = '.'
        return sref + ref_type + self.visit(n.field)

    def visit_FuncCall(self, n):
        fref = self._parenthesize_unless_simple(n.name)
        return fref + '(' + self.visit(n.args) + ')'

    unary_op_map = {
        '&': '',      # TODO: Can we do smth tricky with ptr ops?
        '*': '',
        '!': 'not ',
    }

    def visit_UnaryOp(self, n):
        if n.op == 'sizeof':
            # Always parenthesize the argument of sizeof since it can be
            # a name.
            return 'sizeof(%s)' % self.visit(n.expr)
        else:
            operand = self._parenthesize_unless_simple(n.expr)
            # TODO: We need to detect cases when we can't do this
            if n.op == 'p++':
                # return '%s++' % operand
                return f'{operand} += 1'
            elif n.op == 'p--':
                # return '%s--' % operand
                return f'{operand} -= 1'
            else:
                return '%s%s' % (self.unary_op_map.get(n.op, n.op), operand)

    # Precedence map of binary operators:
    precedence_map = {
        # Should be in sync with c_parser.CParser.precedence
        # Higher numbers are stronger binding
        '||': 0,  # weakest binding
        '&&': 1,
        '|': 2,
        '^': 3,
        '&': 4,
        '==': 5, '!=': 5,
        '>': 6, '>=': 6, '<': 6, '<=': 6,
        '>>': 7, '<<': 7,
        '+': 8, '-': 8,
        '*': 9, '/': 9, '%': 9  # strongest binding
    }

    binary_op_map = {
        '||': 'or',
        '&&': 'and',
    }

    def visit_BinaryOp(self, n):
        # Note: all binary operators are left-to-right associative
        #
        # If `n.left.op` has a stronger or equally binding precedence in
        # comparison to `n.op`, no parenthesis are needed for the left:
        # e.g., `(a*b) + c` is equivalent to `a*b + c`, as well as
        #       `(a+b) - c` is equivalent to `a+b - c` (same precedence).
        # If the left operator is weaker binding than the current, then
        # parentheses are necessary:
        # e.g., `(a+b) * c` is NOT equivalent to `a+b * c`.
        lval_str = self._parenthesize_if(
            n.left,
            lambda d: not (
                self._is_simple_node(d) or
                self.reduce_parentheses and isinstance(d, c_ast.BinaryOp) and
                self.precedence_map[d.op] >= self.precedence_map[n.op]
            )
        )
        # If `n.right.op` has a stronger -but not equal- binding precedence,
        # parenthesis can be omitted on the right:
        # e.g., `a + (b*c)` is equivalent to `a + b*c`.
        # If the right operator is weaker or equally binding, then parentheses
        # are necessary:
        # e.g., `a * (b+c)` is NOT equivalent to `a * b+c` and
        #       `a - (b+c)` is NOT equivalent to `a - b+c` (same precedence).
        rval_str = self._parenthesize_if(
            n.right,
            lambda d: not (
                self._is_simple_node(d) or
                self.reduce_parentheses and isinstance(d, c_ast.BinaryOp) and
                self.precedence_map[d.op] > self.precedence_map[n.op]
            )
        )
        return '%s %s %s' % (lval_str, self.binary_op_map.get(n.op, n.op), rval_str)

    def visit_Assignment(self, n):
        lval_str = self.visit(n.lvalue)
        # TODO: Python is ok w/ chained assignment and not ok w/ x = (y = z)
        # rval_str = self._parenthesize_if(n.rvalue, lambda x: isinstance(x, c_ast.Assignment))
        rval_str = self.visit(n.rvalue)
        return '%s %s %s' % (lval_str, n.op, rval_str)

    def visit_IdentifierType(self, n):
        return ' '.join(n.names)

    def _visit_expr(self, n):
        if isinstance(n, c_ast.InitList):
            return '[' + self.visit(n) + ']'  # '{' + self.visit(n) + '}'
        elif isinstance(n, c_ast.ExprList):
            return '(' + self.visit(n) + ')'
        else:
            return self.visit(n)

    def visit_Decl(self, n, no_type=False):
        # no_type is used when a Decl is part of a DeclList, where the type is
        # explicitly only for the first declaration in a list.
        s = n.name if no_type else self._generate_decl(n)
        if n.bitsize:
            s += ' : ' + self.visit(n.bitsize)
        if n.init:
            # TODO: We have lhs' type, hypothetically we can convert 0 to False, for example, and so on
            s += ' = ' + self._visit_expr(n.init)
        # We should ignore those outside of the func body
        if not n.init and self._state & Context.FuncBody:
            s += ' | None = None'
        return s

    def visit_DeclList(self, n):
        s = self.visit(n.decls[0])
        if len(n.decls) > 1:
            s += ', ' + ', '.join(self.visit_Decl(decl, no_type=True) for decl in n.decls[1:])
        return s

    def visit_Typedef(self, n):
        s = ''
        if n.storage:
            # TODO: I'm not sure if we ever will need this, skipped for now
            # s += ' '.join(n.storage) + ' '
            pass
        s += self._generate_type(n.type)
        return s

    def visit_Cast(self, n):
        # s = '(' + self._generate_type(n.to_type, emit_declname=False) + ')'
        # return s + ' ' + self._parenthesize_unless_simple(n.expr)
        # TODO: We don't support casts, but probably some handler/trigger should be here
        return self._parenthesize_unless_simple(n.expr)

    def visit_ExprList(self, n):
        visited_subexprs = []
        for expr in n.exprs:
            visited_subexprs.append(self._visit_expr(expr))
        return ', '.join(visited_subexprs)

    def visit_InitList(self, n):
        visited_subexprs = []
        for expr in n.exprs:
            visited_subexprs.append(self._visit_expr(expr))
        return ', '.join(visited_subexprs)

    def visit_Enum(self, n):
        return self._generate_struct_union_enum(n, name='enum')

    def visit_Alignas(self, n):
        return '_Alignas({})'.format(self.visit(n.alignment))

    def visit_Enumerator(self, n):
        if not n.value:
            # TODO: Import auto
            return '{indent}{name} = auto()\n'.format(
                indent=self._make_indent(),
                name=n.name,
            )
        else:
            return '{indent}{name} = {value}\n'.format(
                indent=self._make_indent(),
                name=n.name,
                value=self.visit(n.value),
            )

    def visit_FuncDef(self, n):
        decl = self.visit(n.decl, flag=Context.FuncDef)
        self.indent_level = 0
        body = self.visit(n.body, flag=Context.FuncDef | Context.FuncBody)
        # We can't have an empty body in the function definition, TODO: check similar cases
        if not body:
            with self.indent():
                body = self._make_indent() + 'pass'
        if n.param_decls:
            knrdecls = ';\n'.join(self.visit(p) for p in n.param_decls)
            return 'def ' + decl + ':\n' + knrdecls + ';\n' + body + '\n'
        else:
            return 'def ' + decl + ':\n' + body + '\n'

    def visit_FileAST(self, n):
        s = ''
        for ext in n.ext:
            if isinstance(ext, c_ast.FuncDef):
                s += self.visit(ext)
            elif isinstance(ext, c_ast.Pragma):
                s += self.visit(ext) + '\n'
            # TODO: Add some class-level filter, too hardcoded now
            elif isinstance(ext, (c_ast.Typedef, c_ast.Struct)):
                # Let's ignore for now
                pass
            else:
                # We have typedefs and top-level func decls here + some global vars
                if isinstance(ext.type, c_ast.FuncDecl):
                    print('ignoring func decl', ext.name)
                else:
                    # Typedef, Struct, TypeDecl
                    if isinstance(ext.type, (c_ast.Struct,)):
                        continue
                    s += self.visit(ext) + '\n\n'  # ';\n'
        return s

    def visit_Compound(self, n):
        # TODO: Find a proper solution for compound inside of compound
        s = ''  # self._make_indent() + '{\n'
        if do_indent := not isinstance(self._parent, c_ast.Compound):
            self.indent_level += 1
        else:
            print('ignored')
        if n.block_items:
            s += ''.join(self._generate_stmt(stmt) for stmt in n.block_items)
        if do_indent:
            self.indent_level -= 1
        s += ''  # self._make_indent() + '}\n'
        return s

    def visit_CompoundLiteral(self, n):
        # TODO: We should check n.type.type, probably to make a right render
        #  For now let's use ArrayDecl as the default
        # Python doesn't support casts, skipped
        # return '(' + self.visit(n.type) + '){' + self.visit(n.init) + '}'
        return f'[{self.visit(n.init)}]'

    def visit_EmptyStatement(self, n):
        # TODO: Sometimes we will need to intercept empty stmt outside
        return 'pass'  # ';'

    def visit_ParamList(self, n):
        return ', '.join(self.visit(param) for param in n.params)

    def visit_Return(self, n):
        s = 'return'
        if n.expr:
            s += ' ' + self.visit(n.expr)
        return s  # + ';'

    def visit_Break(self, n):
        return 'break'  # 'break;'

    def visit_Continue(self, n):
        return 'continue'  # 'continue;'

    def visit_TernaryOp(self, n):
        # s = '(' + self._visit_expr(n.cond) + ') ? '
        # s += '(' + self._visit_expr(n.iftrue) + ') : '
        # s += '(' + self._visit_expr(n.iffalse) + ')'
        s = f'({self._visit_expr(n.iftrue)}) if ({self._visit_expr(n.cond)}) else ({self._visit_expr(n.iffalse)})'
        return s

    def visit_If(self, n):
        s = 'if ('
        if n.cond:
            s += self.visit(n.cond)
        s += '):\n'
        s += self._generate_stmt(n.iftrue, add_indent=True)
        # TODO: There's a problem w/ indents in nested ifs, original c/py mix
        if n.iffalse:
            s += self._make_indent() + 'else:\n'
            s += self._generate_stmt(n.iffalse, add_indent=True)
        return s

    def visit_For(self, n):
        # TODO: In Python we will have a few different ways to render C-for
        # s = 'for ('
        # if n.init:
        #     s += self.visit(n.init)
        # s += ';'
        # if n.cond:
        #     s += ' ' + self.visit(n.cond)
        # s += ';'
        # if n.next:
        #     s += ' ' + self.visit(n.next)
        # s += ')\n'
        # s += self._generate_stmt(n.stmt, add_indent=True)
        s = ''
        if n.init:
            s += self.visit(n.init)
        s += '\n'
        indent = self.indent_level
        s += self._make_indent() + 'while True:\n'
        s += self._generate_stmt(n.stmt, add_indent=True)
        self.indent_level += 1
        if n.next:
            s += self._make_indent() + self.visit(n.next) + '\n'
        if n.cond:
            s += self._make_indent() + f'if not ({self.visit(n.cond)}):\n'
            self.indent_level += 1
            s += self._make_indent() + 'break'
            self.indent_level -= 1
        self.indent_level = indent
        return s

    def visit_While(self, n):
        s = 'while ('
        if n.cond:
            s += self.visit(n.cond)
        s += '):\n'
        s += self._generate_stmt(n.stmt, add_indent=True)
        return s

    def visit_DoWhile(self, n):
        # TODO: Verify
        indent = self.indent_level
        s = 'while True:\n'  # 'do\n'
        s += self._generate_stmt(n.stmt, add_indent=True)
        # s += self._make_indent() + 'while ('
        # if n.cond:
        #     s += self.visit(n.cond)
        # s += ');'
        if n.cond:
            self.indent_level = indent + 1
            s += self._make_indent() + 'if not (' + self.visit(n.cond) + '):\n'
            self.indent_level += 1
            s += self._make_indent() + 'break\n'
        self.indent_level = indent
        return s

    def visit_StaticAssert(self, n):
        s = '_Static_assert('
        s += self.visit(n.cond)
        if n.message:
            s += ','
            s += self.visit(n.message)
        s += ')'
        return s

    def visit_Switch(self, n):
        # TODO: Probably the best tactic would be to use ifs instead of match
        s = 'match (' + self.visit(n.cond) + ')\n'
        s += self._generate_stmt(n.stmt, add_indent=True)
        return s

    def visit_Case(self, n):
        # TODO: We need to check if the case is fallthrough (has no break), match doesn't support it
        s = 'case ' + self.visit(n.expr) + ':\n'
        for stmt in n.stmts:
            s += self._generate_stmt(stmt, add_indent=True)
        return s

    def visit_Default(self, n):
        s = 'case _:\n'  # 'default:\n'
        for stmt in n.stmts:
            s += self._generate_stmt(stmt, add_indent=True)
        return s

    def visit_Label(self, n):
        # TODO: We don't support labels, so some handler/trigger should be activated here
        return n.name + ':\n' + self._generate_stmt(n.stmt)

    def visit_Goto(self, n):
        # TODO: We don't support gotos, use handler/trigger instead
        return f'goto {n.name}'

    def visit_EllipsisParam(self, n):
        return '...'

    def visit_Struct(self, n):
        return self._generate_struct_union_enum(n, 'struct')

    def visit_Typename(self, n):
        return self._generate_type(n.type)

    def visit_Union(self, n):
        return self._generate_struct_union_enum(n, 'union')

    def visit_NamedInitializer(self, n):
        s = ''
        for name in n.name:
            if isinstance(name, c_ast.ID):
                s += '.' + name.name
            else:
                s += '[' + self.visit(name) + ']'
        s += ' = ' + self._visit_expr(n.expr)
        return s

    def visit_FuncDecl(self, n):
        return self._generate_type(n)

    def visit_ArrayDecl(self, n):
        return self._generate_type(n, emit_declname=False)

    def visit_TypeDecl(self, n):
        return self._generate_type(n, emit_declname=False)

    def visit_PtrDecl(self, n):
        return self._generate_type(n, emit_declname=False)

    def _generate_struct_union_enum(self, n, name):
        """ Generates code for structs, unions, and enums. name should be 'struct', 'union', or 'enum'. """
        if name in ('struct', 'union'):
            members = n.decls
            body_function = self._generate_struct_union_body
            s = name + ' ' + (n.name or '')
        else:
            assert name == 'enum'
            members = None if n.values is None else n.values.enumerators
            body_function = self._generate_enum_body
            s = f'class {n.name}(IntEnum):'
            # TODO: Make some imports
        if members is not None:
            # None means no members
            # Empty sequence means an empty list of members
            s += '\n'
            s += self._make_indent()
            self.indent_level += 1
            # s += '{\n'
            s += body_function(members)
            self.indent_level -= 1
            # s += self._make_indent() + '}'
        return s

    def _generate_struct_union_body(self, members):
        return ''.join(self._generate_stmt(decl) for decl in members)

    def _generate_enum_body(self, members):
        return ''.join(self.visit(value) for value in members) + '\n'

    def _generate_stmt(self, n, add_indent=False):
        """ Generation from a statement node. This method exists as a wrapper
        for individual visit_* methods to handle different treatment of
        some statements in this context. """
        typ = type(n)
        if add_indent:
            self.indent_level += 1
        indent = self._make_indent()
        if add_indent:
            self.indent_level -= 1

        if typ in (
            c_ast.Decl, c_ast.Assignment, c_ast.Cast, c_ast.UnaryOp,
            c_ast.BinaryOp, c_ast.TernaryOp, c_ast.FuncCall, c_ast.ArrayRef,
            c_ast.StructRef, c_ast.Constant, c_ast.ID, c_ast.Typedef,
            c_ast.ExprList
        ):
            # These can also appear in an expression context so no semicolon
            # is added to them automatically
            if ret := self.visit(n):
                return indent + ret + '\n'  # ';\n'
            else:
                # It's possible that node will be reduced, TODO: check other cases like this
                return ''
        elif typ in (c_ast.Compound,):
            # No extra indentation required before the opening brace of a
            # compound - because it consists of multiple lines it has to
            # compute its own indentation.
            return self.visit(n)
        elif typ in (c_ast.If,):
            return indent + self.visit(n)
        else:
            return indent + self.visit(n) + '\n'

    def _generate_decl(self, n):
        """ Generation from a Decl node. """
        s = ''
        if n.funcspec:
            # TODO: We don't support funcspecs (like inline), handler/trigger suggested
            # s = ' '.join(n.funcspec) + ' '
            pass
        if n.storage:
            # TODO: We don't support storage (like static), handler/trigger suggested
            # TODO: We probably support extern via import, but also skipped for now
            # s += ' '.join(n.storage) + ' '
            pass
        # TODO: Check if we have align in pycparser at all
        if hasattr(n, 'align') and n.align:
            s += self.visit(n.align[0]) + ' '
        s += self._generate_type(n.type)
        return s

    types_map = {
        'List[uint8_t]': 'bytes',
        'List[char]': 'str',
        'int32_t': 'int',
        'uint32_t': 'int',
        'int64_t': 'int',
        'uint64_t': 'int',
        'size_t': 'int',
        'double': 'float',  # TODO
        'void': 'None',
    }

    def _map_type(self, c_type: str) -> str:
        mapped = self.types_map.get(c_type, c_type)
        print('mapped', c_type, mapped)
        return mapped

    # TODO: Get rid of default []
    def _generate_type(self, n, modifiers=[], emit_declname=True):
        """ Recursive generation from a type node. n is the type node.
        modifiers collects the PtrDecl, ArrayDecl and FuncDecl modifiers
        encountered on the way down to a TypeDecl, to allow proper
        generation from it. """
        typ = type(n)
        if typ == c_ast.TypeDecl:
            s = ''
            if n.quals:
                # TODO: Make some handle/trigger, we don't support quals in Python
                # s += ' '.join(n.quals) + ' '
                pass
            s += self.visit(n.type)

            nstr = n.declname if n.declname and emit_declname else ''
            # Resolve modifiers.
            # Wrap in parens to distinguish pointer to array and pointer to
            # function syntax.
            for i, modifier in enumerate(modifiers):
                if isinstance(modifier, c_ast.ArrayDecl):
                    if i != 0 and isinstance(modifiers[i - 1], c_ast.PtrDecl):
                        nstr = '(' + nstr + ')'
                    # TODO: Remove, check dim processing
                    # nstr += '['
                    # if modifier.dim_quals:
                    #     nstr += ' '.join(modifier.dim_quals) + ' '
                    # nstr += self.visit(modifier.dim) + ']'
                    s = f'List[{self._map_type(s)}]'
                elif isinstance(modifier, c_ast.FuncDecl):
                    if i != 0 and isinstance(modifiers[i - 1], c_ast.PtrDecl):
                        # TODO: Check, looks like we can skip/reduce this
                        nstr = '(' + nstr + ')'
                    nstr += '(' + self.visit(modifier.args, flag=Context.FuncArgs) + ')'
                elif isinstance(modifier, c_ast.PtrDecl):
                    # TODO: We don't support quals (like 'const'), skipped
                    # if modifier.quals:
                    #     nstr = '* %s%s' % (' '.join(modifier.quals), ' ' + nstr if nstr else '')
                    # else:
                    #     nstr = '*' + nstr
                    # There's no real way to determine what's this ptr means, so we can guess
                    s = f'List[{self._map_type(s)}]'
            if nstr:
                s = self._map_type(s)
                if self._state & Context.FuncArgs or self._state & Context.FuncBody:
                    s = f'{nstr}: {s}'
                elif self._state & Context.FuncDef:
                    s = f'{nstr} -> {s}'
                else:
                    s = f'{nstr}: {s}'
                    # s += ' ' + nstr
            else:
                s = self._map_type(s)
            return s
        elif typ == c_ast.Decl:
            return self._generate_decl(n.type)
        elif typ == c_ast.Typename:
            return self._generate_type(n.type, emit_declname=emit_declname)
        elif typ == c_ast.IdentifierType:
            return ' '.join(n.names) + ' '
        elif typ in (c_ast.ArrayDecl, c_ast.PtrDecl, c_ast.FuncDecl):
            return self._generate_type(n.type, modifiers + [n], emit_declname=emit_declname)
        else:
            return self.visit(n)

    def _parenthesize_if(self, n, condition):
        """ Visits 'n' and returns its string representation, parenthesized
        if the condition function applied to the node returns True. """
        s = self._visit_expr(n)
        if condition(n):
            return '(' + s + ')'
        else:
            return s

    def _parenthesize_unless_simple(self, n):
        """ Common use case for _parenthesize_if """
        return self._parenthesize_if(n, lambda d: not self._is_simple_node(d))

    def _is_simple_node(self, n):
        """ Returns True for nodes that are "simple" - i.e. nodes that always
        have higher precedence than operators. """
        return isinstance(n, (c_ast.Constant, c_ast.ID, c_ast.ArrayRef,
                              c_ast.StructRef, c_ast.FuncCall))