.. _`pip check`:

=========
pip check
=========

.. contents::


Usage
=====

.. tabs::

   .. group-tab:: Unix/macOS

      .. pip-command-usage:: check "python -m pip"

   .. group-tab:: Windows

      .. pip-command-usage:: check "py -m pip"


Description
===========

.. pip-command-description:: check


Examples
========

#. If all dependencies are compatible:

   .. tabs::

      .. group-tab:: Unix/macOS

         .. code-block:: console

            $ python -m pip check
            No broken requirements found.
            $ echo $?
            0

      .. group-tab:: Windows

         .. code-block:: console

            C:\> py -m pip check
            No broken requirements found.
            C:\> echo %errorlevel%
            0

#. If a package is missing:

   .. tabs::

      .. group-tab:: Unix/macOS

         .. code-block:: console

            $ python -m pip check
            pyramid 1.5.2 requires WebOb, which is not installed.
            $ echo $?
            1

      .. group-tab:: Windows

         .. code-block:: console

            C:\> py -m pip check
            pyramid 1.5.2 requires WebOb, which is not installed.
            C:\> echo %errorlevel%
            1

#. If a package has the wrong version:

   .. tabs::

      .. group-tab:: Unix/macOS

         .. code-block:: console

            $ python -m pip check
            pyramid 1.5.2 has requirement WebOb>=1.3.1, but you have WebOb 0.8.
            $ echo $?
            1

      .. group-tab:: Windows

         .. code-block:: console

            C:\> py -m pip check
            pyramid 1.5.2 has requirement WebOb>=1.3.1, but you have WebOb 0.8.
            C:\> echo %errorlevel%
            1
