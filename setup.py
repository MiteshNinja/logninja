from setuptools import setup

setup(
    name='logn',
    version='0.1',
    py_modules=['logninja'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        logn=logninja:logninja
    ''',
)
