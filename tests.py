import sys

try:
    from xmlrpclib import ServerProxy, ProtocolError
except ImportError:
    from xmlrpc.client import ServerProxy, ProtocolError

from six import b

import unittest

from mock import Mock

from djangotestxmlrpc import DjangoTestClientXMLRPCTransport


class SimpleTests(unittest.TestCase):

    def setUp(self):
        self.client = self.get_mock_client()
        self.server_proxy = ServerProxy(
            'http://fakeserver/RPC2',
            transport=DjangoTestClientXMLRPCTransport(self.client))

    def get_mock_client(self):
        mock_client = Mock()
        response = mock_client.post.return_value
        response.status_code = 200
        response.content = """<methodResponse><params><param><value><string>South Dakota</string></value></param></params></methodResponse>"""
        return mock_client

    def test_200(self):
        state_name = self.server_proxy.examples.getStateName(41)
        self.client.post.assert_called_with(
            '/RPC2',
            b("<?xml version='1.0'?>\n<methodCall>\n<methodName>examples.getStateName</methodName>\n<params>\n<param>\n<value><int>41</int></value>\n</param>\n</params>\n</methodCall>\n"),
            'text/xml')
        self.assertEqual(state_name, 'South Dakota')

    def test_500(self):
        self.client.post.return_value.status_code = 500
        self.client.post.return_value.items.return_value = [('Content-Type', 'text/xml')]

        try:
            self.server_proxy.examples.getStateName(41)
        except ProtocolError:
            e = sys.exc_info()[1]
            self.assertEqual(e.errcode, 500)
            self.assertEqual(e.headers, {'Content-Type': 'text/xml'})
            self.assertEqual(e.url, 'fakeserver/RPC2')

        self.client.post.assert_called_with(
            '/RPC2',
            b("<?xml version='1.0'?>\n<methodCall>\n<methodName>examples.getStateName</methodName>\n<params>\n<param>\n<value><int>41</int></value>\n</param>\n</params>\n</methodCall>\n"),
            'text/xml')
