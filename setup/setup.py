from setuptools import setup

setup(
    name="custompython",
    version="0.1",
    py_modules=["custompython", "pycharm"],
    entry_points={
        'pygments.lexers': [
            'custompython = custompython:CustompythonLexer'
        ],
        'pygments.styles': [
            'pycharm = pycharm:PycharmStyle'
        ]
    }
)