Contributing
============

* We are interested in various different kinds of improvement for ``number2text``; please feel free to raise an `Issue`_ if you would like to work on something major to ensure efficient collaboration and avoid duplicate effort.
* Create a topic branch from where you want to base your work.
* Make sure you have added tests for your changes.
* Run all the tests to ensure nothing else was accidentally broken.
* Reformat the code by following the formatting section below.
* Submit a pull request.

Unit Testing
------------

Unit tests are performed by `Tox`_.

.. code-block:: bash

  tox

Formatting
----------

The formatting is done using `YAPF`_.

From the root for the project, run:

.. code-block:: bash

  yapf -i -r molecule/

.. _`YAPF`: https://github.com/google/yapf
.. _`Tox`: https://tox.readthedocs.org/en/latest
.. _`Issue`: https://github.com/metacloud/molecule/issues
