import re
import setuptools
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


extras_require = {
    'tests': [
        'pytest >=2.5.2,<3',
        'pytest-cov >=1.7,<2',
        'mock >=1.0,<2.0',
        'unittest2 >=0.5.1,<0.6',
        'iso8601 >=0.1,<0.2',
    ],
}

packages = setuptools.find_packages('.', exclude=('tests', 'tests.*'))

setuptools.setup(
    name='pilo',
    version=(
        re
        .compile(r".*__version__ = '(.*?)'", re.S)
        .match(open('pilo/__init__.py').read())
        .group(1)
    ),
    url='https://github.com/bninja/pilo/',
    license=open('LICENSE').read(),
    author='egon',
    author_email='egon@gb.com',
    description='Yet another form parser.',
    long_description=open('README.rst').read(),
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    extras_require=extras_require,
    tests_require=extras_require['tests'],
    install_requires=[],
    cmdclass={'test': PyTest},
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
