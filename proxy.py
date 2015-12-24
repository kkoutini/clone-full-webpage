from miproxy.proxy import RequestInterceptorPlugin, ResponseInterceptorPlugin, AsyncMitmProxy
from mimetools import Message
from StringIO import StringIO
import json
from pprint import pprint


koko=open("urlss", "a")
class DebugInterceptor(RequestInterceptorPlugin, ResponseInterceptorPlugin):

        def do_request(self, data):
            data = data.replace('Accept-Encoding: gzip\r\n', 'Accept-Encoding:\r\n', 1)
            print "request got"
            print data
            koko.write(data+'\n')
            return data

        def do_response(self, data):
            print '<< %s' % repr(data[:100])
            request_line, headers_alone = data.split('\r\n', 1)
            headers = Message(StringIO(headers_alone))
            print "Content type: %s" %(headers['content-type'])
            if headers['content-type'] == 'text/x-comma-separated-values':
                f = open('data.csv', 'w')
                f.write(data)
            pprint( self)
            return data

if __name__ == '__main__':
    proxy = AsyncMitmProxy()
    proxy.register_interceptor(DebugInterceptor)
    try:
        proxy.serve_forever()
    except KeyboardInterrupt:
        koko.close()
        proxy.server_close()