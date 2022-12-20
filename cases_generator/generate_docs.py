import requests

from lxml.etree import HTML

__all__ = [
    'fetch_docs',
]

DEFAULT_DIS_DOCS_URL = 'https://docs.python.org/3.12/library/dis.html'


def fetch_docs() -> dict:
    result = {}
    doc = HTML(requests.get(DEFAULT_DIS_DOCS_URL).content)
    for opcode in doc.xpath('//dl[@class="std opcode"]'):
        opcode_name = opcode.xpath('./dt/span[contains(@class, "descname")]/span')[0].text
        opcode_ps = []
        for idx, doc in enumerate(opcode.xpath('./dd//p')):
            opcode_ps.append(''.join(doc.itertext()))
        result[opcode_name] = '\n\n'.join(opcode_ps)
    return result
