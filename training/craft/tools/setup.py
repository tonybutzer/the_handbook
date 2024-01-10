
from setuptools import setup

setup (
    name='pyan', 
    version='1.0',
    py_modules=['pyan'],
    install_requires=[
        'compiler',
    ],

    entry_points='''
        [console_scripts]
        pyan=pyan:main
    '''

)

