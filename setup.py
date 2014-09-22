from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='reek-restructuredfield',
    version='0.1.dev0',
    url='http://github.com/bpeschier/reek-restructuredfield',
    author="Bas Peschier",
    author_email="bpeschier@fizzgig.nl",
    packages=['restructuredfield'],
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['Django>=1.7', ]
)