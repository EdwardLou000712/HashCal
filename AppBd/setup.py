from setuptools import setup

APP = ['/Users/shutonglou/Desktop/hashCal/HashCal/AppBd/hash_tool.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
