Documentation Fundamentals
**************************

:Last Reviewed: 2015-11-17

.. contents::
   :local:
   :depth: 3

reStructuredText
================

http://sphinx-doc.org/rest.html

Sphinx
======

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.

It was originally created for the new Python documentation, and it has excellent facilities for the documentation of Python projects. The following features should be highlighted:

* Output formats: HTML (including Windows HTML Help), LaTeX (for printable PDF versions), ePub, Texinfo, manual pages, plain text
* Extensive cross-references: semantic markup and automatic links for functions, classes, citations, glossary terms and similar pieces of information
* Hierarchical structure: easy definition of a document tree, with automatic links to siblings, parents and children
* Automatic indices: general index as well as a language-specific module indices
Code handling: automatic highlighting using the Pygments highlighter
* Extensions: automatic testing of code snippets, inclusion of docstrings from Python modules (API docs), and more
* Contributed extensions: more than 50 extensions contributed by users in a second repository; most of them installable from PyPI
* Sphinx uses reStructuredText as its markup language, and many of its strengths come from the power and straightforwardness of reStructuredText and its parsing and translating suite, the Docutils. http://docutils.sourceforge.net/

QuickStart
==========

http://sphinx-doc.org/tutorial.html

Setting up the documentation sources
------------------------------------

Sphinx comes with a script called sphinx-quickstart that sets up a source directory and creates a default conf.py with the most useful configuration values from a few questions it asks you. Just run::

    $ sphinx-quickstart

and answer its questions. (Be sure to say yes to the “autodoc” extension.)


Defining document structure
---------------------------

The main function of the master document (``index.rst`` by default) is to serve as a welcome page, and to contain the root of the “table of contents tree” (or toctree).

http://sphinx-doc.org/markup/toctree.html#toctree-directive

Running the build
-----------------

To build the docs::

    $ sphinx-build -b html sourcedir builddir

or using the Makefile::

    $ make html
