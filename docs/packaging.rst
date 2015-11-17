Packaging Fundamentals
**********************

:Last Reviewed: 2015-11-17

.. contents::
   :local:
   :depth: 3

Tools overview
==============

Installation Tools
------------------

* Use pip to install Python packages from
  PyPI. Depending how pip
  is installed, you may need to also install wheel to get the benefit
  of wheel caching.

* Use virtualenv, or `pyvenv`_ to isolate application specific
  dependencies from a shared Python installation.

* If you're looking for management of fully integrated cross-platform software
  stacks, consider buildout (primarily focused on the web development
  community) or hashdist, or conda (both primarily focused on
  the scientific community).

Packaging Tools
---------------

* Use setuptools to define projects and create Source Distributions.

* Use the ``bdist_wheel`` setuptools extension available from the
  wheel project to create wheels. This is
  especially beneficial, if your project contains binary extensions.

* Use `twine <https://pypi.python.org/pypi/twine>`_ for uploading distributions
  to PyPI.


Working in "Development Mode"
=============================

Although not required, it's common to locally install your project in "editable"
or "develop" mode while you're working on it.  This allows your project to be
both installed and editable in project form.

Assuming you're in the root of your project directory, then run:

::

 pip install -e .


It's fairly common to also want to install some of your dependencies in editable
mode as well. For example, supposing your project requires "foo" and "bar", but
you want "bar" installed from vcs in editable mode, then you could construct a
requirements file like so::

  -e .
  -e git+https://somerepo/bar.git#egg=bar

The first line says to install your project and any dependencies. The second
line overrides the "bar" dependency, such that it's fulfilled from vcs, not
PyPI.

Lastly, if you don't want to install any dependencies at all, you can run::

   pip install -e . --no-deps


For more information, see the `Development Mode
<http://pythonhosted.org/setuptools/setuptools.html#development-mode>`_ section
of the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.


More on Dependencies
====================

Depencencies are declared in setup.py::

    setup(
        ...
        install_requires=['pip_package_name']
        ...
    )
 

If the dependency is not in PyPI, a link to the egg can 
be provided like::

    setup(
        ...
        dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
        ...
    )

Non-python files
================

MANIFEST.in is necessary to tell setuptools to include the non-python files 
when generating source distributions. Otherwise, only Python files will be included.


Scripts
=======

Use the ``console_scripts`` Entry Point method to register command line scripts. 

Setuptools allows modules to register entrypoints which other packages can hook into to provide certain functionality. It also provides a few itself, including the ``console_scripts`` entry point.

This allows Python *functions* (not scripts!) to be directly registered as command-line accessible tools.

The ``main()`` function can then be registered like so::

    setup(
        ...
        entry_points = {
            'console_scripts': ['command=package.command_line:main'],
        }
        ...
    )

Packaging your Project
======================

To have your project installable from a Package Index, you'll need to create a
Distribution Package for your project.


Source Distributions
--------------------

Minimally, you should create a Source Distribution::

 python setup.py sdist


A "source distribution" is unbuilt (i.e, it's not a Built Distribution),
and requires a build step when installed by pip.  Even if the distribution is
pure python (i.e. contains no extensions), it still involves a build step to
build out the installation metadata from ``setup.py``.


Wheels
------

You should also create a wheel for your project. A wheel is a Built Distribution 
that can be installed without needing to go through the "build" process. 
Installing wheels is substantially faster for the end user than installing 
from a source distribution.

If your project is pure python (i.e. contains no compiled extensions) and
natively supports both Python 2 and 3, then you'll be creating what's called a
"Universal Wheel" (see section below).

If your project is pure python but does not natively support both Python 2 and
3, then you'll be creating a "Pure Python Wheel" (see section below).

If you project contains compiled extensions, then you'll be creating what's
called a "Platform Wheel" (see section below).


.. _`Universal Wheels`:

Universal Wheels
~~~~~~~~~~~~~~~~

"Universal Wheels" are wheels that are pure python (i.e. contains no compiled
extensions) and support Python 2 and 3. This is a wheel that can be installed
anywhere by pip.

To build a Universal Wheel:

::

 python setup.py bdist_wheel --universal


You can also permanently set the ``--universal`` flag in "setup.cfg" (e.g., see
`python_project_example/setup.cfg
<https://github.com/garcianavalon/python_project_example/blob/master/setup.cfg>`_)

::

 [bdist_wheel]
 universal=1


Only use the ``--universal`` setting, if:

1. Your project runs on Python 2 and 3 with no changes (i.e. it does not
   require 2to3).
2. Your project does not have any C extensions.

Beware that ``bdist_wheel`` does not currently have any checks to warn you if
use the setting inappropriately.

If your project has optional C extensions, it is recommended not to publish a
universal wheel, because pip will prefer the wheel over a source installation,
and prevent the possibility of building the extension.


.. _`Pure Python Wheels`:

Pure Python Wheels
~~~~~~~~~~~~~~~~~~

"Pure Python Wheels" that are not "universal" are wheels that are pure python
(i.e. contains no compiled extensions), but don't natively support both Python 2
and 3.

To build the wheel:

::

 python setup.py bdist_wheel


`bdist_wheel` will detect that the code is pure Python, and build a wheel that's
named such that it's usable on any Python installation with the same major
version (Python 2 or Python 3) as the version you used to build the wheel.  For
details on the naming of wheel files, see :pep:`425`

If your code supports both Python 2 and 3, but with different code (e.g., you
use `"2to3" <https://docs.python.org/2/library/2to3.html>`_) you can run
``setup.py bdist_wheel`` twice, once with Python 2 and once with Python 3. This
will produce wheels for each version.



.. _`Platform Wheels`:

Platform Wheels
~~~~~~~~~~~~~~~

"Platform Wheels" are wheels that are specific to a certain platform like linux,
OSX, or Windows, usually due to containing compiled extensions.

To build the wheel:

::

 python setup.py bdist_wheel


`bdist_wheel` will detect that the code is not pure Python, and build a wheel
that's named such that it's only usable on the platform that it was built
on. For details on the naming of wheel files, see :pep:`425`

.. note::

  PyPI currently only allows uploads of
  platform wheels for Windows and OS X, NOT linux.  Currently, the wheel tag
  specification (:pep:`425`) does not handle the variation that can
  exist across linux distros.


.. _`Uploading your Project to PyPI`:

Uploading your Project to PyPI
==============================

.. note::

  Before releasing on main PyPI repo, you might prefer training with
  `PyPI test site <https://testpypi.python.org/pypi>`_
  which is cleaned on a semi regular basis. See
  `these instructions <https://wiki.python.org/moin/TestPyPI>`_ on how
  to setup your configuration in order to use it.

Create an account
-----------------

First, you need a PyPI user
account. There are two options:

1. Create an account manually `using the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=register_form>`_.

2. Have an account created as part of registering your first project (see option
   #2 below).


Register your project
---------------------

Next, you need to register your project.  There are two ways to do this:

1. **(Recommended):** Use `the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=submit_form>`_, to upload your
   ``PKG-INFO`` info located in your local project tree at
   ``myproject.egg-info/PKG-INFO``.  If you don't have that file or directory,
   then run ``python setup.py egg_info`` to have it generated. Using the form is
   a secure option over using #2 below, which passes your credentials over
   plaintext.
2. Run ``python setup.py register``.  If you don't have a user account already,
   a wizard will create one for you.


If you created your account using option #1 (the form), you'll need to manually
write a ``~/.pypirc`` file like so.

   ::

    [distutils]
    index-servers=pypi

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <username>
    password = <password>

You can leave out the password line if below you use twine with its
``-p PASSWORD`` argument.


Upload your distributions
-------------------------

Finally, you can upload your distributions to PyPI.

There are two options:

1. **(Recommended):** Use twine

   ::

     twine upload dist/*

   The biggest reason to use twine is that ``python setup.py upload`` (option #2
   below) uploads files over plaintext. This means anytime you use it you expose
   your username and password to a MITM attack. Twine uses only verified TLS to
   upload to PyPI protecting your credentials from theft.

   Secondly it allows you to precreate your distribution files.  ``python
   setup.py upload`` only allows you to upload something that you've created in
   the same command invocation. This means that you cannot test the exact file
   you're going to upload to PyPI to ensure that it works before uploading it.

   Finally it allows you to pre-sign your files and pass the .asc files into the
   command line invocation (``twine upload twine-1.0.1.tar.gz
   twine-1.0.1.tar.gz.asc``). This enables you to be assured that you're typing
   your gpg passphrase into gpg itself and not anything else since *you* will be
   the one directly executing ``gpg --detach-sign -a <filename>``.


2. Use setuptools:

   ::

    python setup.py sdist bdist_wheel upload


Actions overview
================

Install locally::

    $ python setup.py install

Install locally with symlink::

    $ python setup.py develop

Create a Source Distribution::

    $ python setup.py sdist

Register in PyPI::

    $ python setup.py register

Upload to PyPI::

    $ python setup.py sdist upload

Install a package::

    $ pip install package_name


.. _pyvenv: http://docs.python.org/3.4/library/venv.html