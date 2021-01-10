========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pyacremote/badge/?style=flat
    :target: https://readthedocs.org/projects/pyacremote
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/eiaro/pyacremote.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/eiaro/pyacremote

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/eiaro/pyacremote?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/eiaro/pyacremote

.. |requires| image:: https://requires.io/github/eiaro/pyacremote/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/eiaro/pyacremote/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/eiaro/pyacremote/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/eiaro/pyacremote

.. |codecov| image:: https://codecov.io/gh/eiaro/pyacremote/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/eiaro/pyacremote

.. |version| image:: https://img.shields.io/pypi/v/pyacremote.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pyacremote

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyacremote.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pyacremote

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyacremote.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pyacremote

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyacremote.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pyacremote

.. |commits-since| image:: https://img.shields.io/github/commits-since/eiaro/pyacremote/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/eiaro/pyacremote/compare/v0.0.1...master



.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install pyacremote

You can also install the in-development version with::

    pip install https://github.com/eiaro/pyacremote/archive/master.zip


Documentation
=============


https://pyacremote.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
