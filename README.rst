djangotestxmlrpc
=======================================

.. image:: https://secure.travis-ci.org/msabramo/djangotestxmlrpc.png?branch=master
   :target: http://travis-ci.org/msabramo/djangotestxmlrpc

Test Django XML-RPC views using the `Django test client
<https://docs.djangoproject.com/en/dev/topics/testing/#module-django.test.client>`_.
Because you're using the Django test client, you're not actually sending HTTP
requests and don't
need a server running.


Example usage
-------------

.. code:: python

    from djangotestxmlrpc import DjangoTestClientXMLRPCTransport

    class TestXmlRpc(django.test.TestCase):
        ...

        def test_list_package(self):
            pypi = xmlrpclib.ServerProxy("http://localhost/pypi/", transport=DjangoTestClientXMLRPCTransport(self.client))
            pypi_hits = pypi.list_packages()
            expected = ['foo']
            self.assertEqual(pypi_hits, expected)


Supported Python versions
-------------------------

- Python 2.5
- Python 2.6
- Python 2.7
- PyPy 1.9
- Python 3.1
- Python 3.2

or says `tox <http://tox.testrun.org/>`_::

    ~/dev/git-repos/djangotestxmlrpc$ tox
    ...
      py25: commands succeeded
      py26: commands succeeded
      py27: commands succeeded
      pypy: commands succeeded
      py31: commands succeeded
      py32: commands succeeded
      congratulations :)

You also can check the `latest Travis CI results
<http://travis-ci.org/msabramo/djangotestxmlrpc>`_, but
Travis doesn't build all of the above platforms.


Issues
------

Send your bug reports and feature requests to https://github.com/msabramo/djangotestxmlrpc/issues

