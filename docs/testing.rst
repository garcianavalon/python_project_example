Testing Fundamentals
********************

:Last Reviewed: 2015-11-17

.. contents::
   :local:
   :depth: 3

Unittest
========

:mod:`unittest` is the batteries-included test module in the Python standard
library. Its API will be familiar to anyone who has used any of the
JUnit/nUnit/CppUnit series of tools.

As of Python 2.7 unittest also includes its own test discovery mechanisms.

    `unittest in the standard library documentation <http://docs.python.org/library/unittest.html>`_


Doctest
=======

The :mod:`doctest` module searches for pieces of text that look like interactive
Python sessions in docstrings, and then executes those sessions to verify that
they work exactly as shown.

Doctests have a different use case than proper unit tests: they are usually
less detailed and don't catch special cases or obscure regression bugs. They
are useful as an expressive documentation of the main use cases of a module and
its components. However, doctests should run automatically each time the full
test suite runs.


py.test
=======

py.test is a no-boilerplate alternative to Python's standard unittest module.

Despite being a fully-featured and extensible test tool, it boasts a simple
syntax. Creating a test suite is as easy as writing a module with a couple of
functions and then running the `py.test` command

.. code-block:: console

    $ py.test
    =========================== test session starts ============================
    platform darwin -- Python 2.7.1 -- pytest-2.2.1
    collecting ... collected 1 items

    test_sample.py F

    ================================= FAILURES =================================
    _______________________________ test_answer ________________________________

        def test_answer():
    >       assert func(3) == 5
    E       assert 4 == 5
    E        +  where 4 = func(3)

    test_sample.py:5: AssertionError
    ========================= 1 failed in 0.02 seconds =========================

is far less work than would be required for the equivalent functionality with
the unittest module!

    `py.test <http://pytest.org/latest/>`_


Nose2
=====

nose2 is the next generation of nicer testing for Python, based
on the plugins branch of unittest2. nose2 aims to improve on nose by:

 * providing a better plugin api
 * being easier for users to configure
 * simplifying internal interfaces and processes
 * supporting Python 2 and 3 from the same codebase, without translation
 * encouraging greater community involvement in its development

    `nose2 <https://nose2.readthedocs.org/en/latest/>`_


tox
===

tox is a tool for automating test environment management and testing against
multiple interpreter configurations.

tox allows you to configure complicated multi-parameter test matrices via a
simple ini-style configuration file.

    `tox <http://testrun.org/tox/latest/>`_


Unittest2
=========

unittest2 is a backport of Python 2.7's unittest module which has an improved
API and better assertions over the one available in previous versions of Python.

If you're using Python 2.6 or below, you can install it with pip


You may want to import the module under the name unittest to make porting code
to newer versions of the module easier in the future.

This way if you ever switch to a newer Python version and no longer need the
unittest2 module, you can simply change the import in your test module without
the need to change any other code.

    `unittest2 <http://pypi.python.org/pypi/unittest2>`_


mock
====

:mod:`unittest.mock` is a library for testing in Python. As of Python 3.3, it is
available in the
`standard library <https://docs.python.org/dev/library/unittest.mock>`_.

It allows you to replace parts of your system under test with mock objects and
make assertions about how they have been used.

    `mock <http://www.voidspace.org.uk/python/mock/>`_