"""
Tools for testing Django XML-RPC views using the Django test client

This is an extension of code taken from a blog post from Forest Bond at
http://www.alittletooquiet.net/blog/2009/11/01/testing-django-xml-rpc-interfaces/
"""

try:
    from httplib import responses
except ImportError:
    from http.client import responses

try:
    from xmlrpclib import getparser, ProtocolError
except ImportError:
    from xmlrpc.client import getparser, ProtocolError


class DjangoTestClientXMLRPCTransport(object):
    """Designed to be passed into the `transport` argument of
    `xmlrpclib.ServerProxy`, this class accepts a `django.test.TestClient`
    object and uses it as the transport.

    """

    client = None

    def __init__(self, client):
        self.client = client

    def request(self, host, handler, request_body, verbose = False):
        parser, unmarshaller = getparser()

        response = self.client.post(handler, request_body, 'text/xml')

        if response.status_code != 200:
            raise ProtocolError(
              '%s%s' % (host, handler),
              response.status_code,
              responses.get(response.status_code, ''),
              dict(response.items()),
            )

        parser.feed(response.content)

        return unmarshaller.close()

