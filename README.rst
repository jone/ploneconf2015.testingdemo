=====================================================
 Ploneconference 2015 - testing demo - lighting talk
=====================================================

Here is the example from the lighting talk.

Installation
============

.. code:: bash

   git clone git@github.com:jone/ploneconf2015.testingdemo
   cd ploneconf2015.testingdemo
   ln -s development.cfg buildout.cfg
   python2.7 bootstrap.py
   bin/buildout
   bin/test


References
==========

- https://github.com/4teamwork/ftw.testbrowser
- http://pythonhosted.org/ftw.testbrowser/index.html
- https://github.com/4teamwork/ftw.builder
- http://devblog.4teamwork.ch/blog/2013/05/24/construct-your-testing-data-using-the-builder-pattern/
