==========
Quickstart
==========

First, :doc:`install pip <installing>`.

Install a package from `PyPI`_:

.. tabs::

   .. group-tab:: Unix/macOS

      .. code-block:: console

         $ python -m pip install SomePackage
         [...]
         Successfully installed SomePackage

   .. group-tab:: Windows

      .. code-block:: console

         C:\> py -m pip install SomePackage
         [...]
         Successfully installed SomePackage


Install a package that's already been downloaded from `PyPI`_ or
obtained from elsewhere. This is useful if the target machine does not have a
network connection:

.. tabs::

   .. group-tab:: Unix/macOS

      .. code-block:: console

         $ python -m pip install SomePackage-1.0-py2.py3-none-any.whl
         [...]
         Successfully installed SomePackage

   .. group-tab:: Windows

      .. code-block:: console

         C:\> py -m pip install SomePackage-1.0-py2.py3-none-any.whl
         [...]
         Successfully installed SomePackage


Show what files were installed:

.. tabs::

   .. group-tab:: Unix/macOS

      .. code-block:: console

         $ python -m pip show --files SomePackage
         Name: SomePackage
         Version: 1.0
         Location: /my/env/lib/pythonx.x/site-packages
         Files:
         ../somepackage/__init__.py
         [...]

   .. group-tab:: Windows

      .. code-block:: console

         C:\> py -m pip show --files SomePackage
         Name: SomePackage
         Version: 1.0
         Location: /my/env/lib/pythonx.x/site-packages
         Files:
         ../somepackage/__init__.py
         [...]

List what packages are outdated:

.. tabs::

   .. group-tab:: Unix/macOS

      .. code-block:: console

         $ python -m pip list --outdated
         SomePackage (Current: 1.0 Latest: 2.0)

   .. group-tab:: Windows

      .. code-block:: console

         C:\> py -m pip list --outdated
         SomePackage (Current: 1.0 Latest: 2.0)

Upgrade a package:

.. tabs::

   .. group-tab:: Unix/macOS

      .. code-block:: console

         $ python -m pip install --upgrade SomePackage
         [...]
         Found existing installation: SomePackage 1.0
         Uninstalling SomePackage:
         Successfully uninstalled SomePackage
         Running setup.py install for SomePackage
         Successfully installed SomePackage

   .. group-tab:: Windows

      .. code-block:: console

         C:\> py -m pip install --upgrade SomePackage
         [...]
         Found existing installation: SomePackage 1.0
         Uninstalling SomePackage:
         Successfully uninstalled SomePackage
         Running setup.py install for SomePackage
         Successfully installed SomePackage

Uninstall a package:

.. tabs::

   .. group-tab:: Unix/macOS

      .. code-block:: console

         $ python -m pip uninstall SomePackage
         Uninstalling SomePackage:
         /my/env/lib/pythonx.x/site-packages/somepackage
         Proceed (y/n)? y
         Successfully uninstalled SomePackage

   .. group-tab:: Windows

      .. code-block:: console

         C:\> py -m pip uninstall SomePackage
         Uninstalling SomePackage:
           /my/env/lib/pythonx.x/site-packages/somepackage
         Proceed (y/n)? y
         Successfully uninstalled SomePackage


.. _PyPI: https://pypi.org/
