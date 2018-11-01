from setuptools import setup

exec(open('iam_tools/version.py').read())

setup(
    name='iam_tools',
    description=(
        'The IAM_tools - '
        'a Python package of tools to deal with IAM data.'),
    long_description=open('README.md').read(),
    url='https://gitlab.com/dlab-indecol/iam_tools.git',
    author='Radek Lonka, Konstantin Stadler',
    author_email='radek.lonka@ntnu.no, konstantin.stadler@ntnu.no',
    version=__version__,  # noqa
    packages=['iam_tools', ],
    package_data={'iam_tools': ['../LICENSE']},
    entry_points={
        'console_scripts':
        ['filter_iam = iam_tools.filter:main']},
    install_requires=['pandas >= 0.23.0', 'scipy >= 1.0.0'],
    classifiers=[
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3 :: Only',
          'License :: OSI Approved :: BSD 3-Clause License',
          'Development Status :: 0 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Topic :: Utilities',
          ],
)