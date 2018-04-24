import asyncio
import uvloop
# import httptools
# from datetime import datetime, timezone

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# _RESP_CACHE = {}

# class HttpRequest:
#     __slots__ = ('_protocol', '_url', '_headers', '_version')

#     def __init__(self, protocol, url, headers, version):
#         self._protocol = protocol
#         self._url = url
#         self._headers = headers
#         self._version = version


# class HttpResponse:
#     __slots__ = ('_protocol', '_request', '_headers_sent')

#     def __init__(self, protocol, request):
#         self._protocol = protocol
#         self._request = request
#         self._headers_sent = False

#     def write(self, data):
#         self._protocol._transport.write(b'\r\n'.join([
#             b'HTTP/1.1 200 OK',
#             b'Content-Type: text/plain',
#             b'Content-Length: 4',
#             b'',
#             data
#         ]))

# class HttpProtocol(asyncio.Protocol):

#     __slots__ = ('_loop',
#                  '_transport', '_current_request', '_current_parser',
#                  '_current_url', '_current_headers')

#     def __init__(self, *, loop=None):
#         if loop is None:
#             loop = asyncio.get_event_loop()
#         self._loop = loop
#         self._transport = None
#         self._current_request = None
#         self._current_parser = None
#         self._current_url = None
#         self._current_headers = None

#     def on_url(self, url):
#         self._current_url = url

#     def on_header(self, name, value):
#         self._current_headers.append((name, value))

#     def on_headers_complete(self):
#         self._current_request = HttpRequest(
#             self, self._current_url, self._current_headers,
#             self._current_parser.get_http_version()
#         )

#         self._loop.call_soon(
#             self.handle,
#             self._current_request,
#             HttpResponse(self, self._current_request)
#         )

#     def connection_made(self, transport):
#         self._transport = transport
#         sock = transport.get_extra_info('socket')
#         try:
#             sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
#         except (OSError, NameError):
#             pass

#     def connection_lost(self, exc):
#         self._current_request = self._current_parser = None

#     def data_received(self, data):
#         if self._current_parser is None:
#             assert self._current_request is None
#             self._current_headers = []
#             self._current_parser = httptools.HttpRequestParser(self)

#         self._current_parser.feed_data(data)

#     def handle(self, request, response):
#         response.write(b"echo")
#         if not self._current_parser.should_keep_alive():
#             self._transport.close()
#         self._current_parser = None
#         self._current_request = None

# class Request(object):
#     __slots__ = ('_loop', '_transport', '_current_parser', '_callback')

#     def __init__(self, transport, loop=None, callback=None):
#         self._loop = loop
#         self._transport = transport
#         self._callback = callback
#         # self._headers_complete = False
#         self._current_parser = httptools.HttpRequestParser(self)
    
#     def feed_data(self, data):
#         return self._current_parser.feed_data(data)

#     def on_headers_complete(self):
#         # self._headers_complete = True
#         self._loop.create_task(self.handle())

#     # def is_headers_complete(self):
#     #     return self._headers_complete

#     async def handle(self):
#         self._transport.write(
#             b'\r\n'.join([
#                 b'HTTP/1.1 200 OK',
#                 b'Content-Type: text/plain',
#                 b'Content-Length: 4',
#                 b'',
#                 b'echo'
#             ])
#         )
#         if not self._current_parser.should_keep_alive():
#             self._transport.close()
#         if self._callback is not None:
#             self._callback()
        # self._current_parser = None

class HttpProtocol(asyncio.Protocol):
    __slots__ = ('_loop', '_transport')

    def __init__(self, *, loop=None):
        self._loop = loop
        self._transport = None
        # self._requset = None

    def connection_made(self, transport):
        self._transport = transport

    # def connection_lost(self, exc):
    #     self._requset = None
    
    def data_received(self, data):
        self._transport.write(
            b'\r\n'.join([
                b'HTTP/1.1 200 OK',
                b'Content-Type: text/plain',
                b'Content-Length: 4',
                b'',
                b'echo'
            ])
        )
        self._transport.close()
        # if self._requset is None:
        #     self._requset = Request(self._transport, self._loop, self.callback)
        # self._requset.feed_data(data)
    
    # def callback(self):
    #     self._requset = None

async def main(loop):
    await loop.create_server(lambda: HttpProtocol(loop=loop), host="0.0.0.0", port=5000)
    # await asyncio.sleep(60000)

if __name__ == "__main__":
    base_loop = asyncio.get_event_loop()
    base_loop.run_until_complete(main(base_loop))
    base_loop.run_forever()