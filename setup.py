from setuptools import setup, find_packages

setup(
    name='nxbuilder',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nxb=cli:run',
        ],
    },
)
