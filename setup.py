from setuptools import setup

packages = [
    'cullerton.contacts',
]

requires = []

setup(
    name='cullerton.contacts',
    version="0.0.1",
    packages=packages,
    namespace_packages=['cullerton'],
    install_requires=requires,
    author='mike cullerton',
    author_email='michaelc@cullerton.com',
    description='A simple contact manager',
    url='https://github.com/cullerton/cullerton.contacts',
    download_url='https://github.com/cullerton/cullerton.contacts/tarball/0.0.1',
    keywords=['academic', 'simple', 'example'],
    classifiers=[],
    package_data={
        '': ['*.txt', '*.rst', '*.ipynb'],
    },
)
