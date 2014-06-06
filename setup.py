from distutils.core import setup

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(
    name='petrarch',
    install_requires=required,
    entry_points={
        'console_scripts': ['petrarch = petrarch.petrarch:main']},
    version='0.01a',
    author='Philip Schrodt, John Beieler',
    author_email='openeventdata@gmail.com',
    packages=['petrarch'],
    url='openeventdata.org',
    license='LICENSE.txt',
    description='PETRARCH parser for event data.',
    long_description=open('README.md').read())