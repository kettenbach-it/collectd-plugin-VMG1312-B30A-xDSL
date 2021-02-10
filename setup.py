from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='collectd-plugin-VMG1312-xDSL',
    version='1.0.1',
    #packages=[''],
    url='https://github.com/kettenbach-it/collectd-plugin-VMG1312-B30A-xDSL',
    license='GPL v3',
    author='Volker Kettenbach',
    author_email='volker@ktnbch.de',
    description='A collectd module written in Python for getting the xDSL status of Zyxel VMG1312 modems/routers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages',
        'Source': 'https://github.com/kettenbach-it/collectd-plugin-VMG1312-B30A-xDSL',
    }
)
