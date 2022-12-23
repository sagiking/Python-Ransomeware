#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv
import logging


class S(BaseHTTPRequestHandler):
    def _get_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        with open("index.html", 'r') as file:
            data = file.read()
        self.wfile.write(data.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        with open(".logs", 'a') as file:
            file.write(
                str(f'\n\n\nHeaders:\n{self.headers}Path:{self.path}\n\nData:\n{post_data}'))
        self._get_response()
        self.wfile.write("Post Request for {}".format(
            self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=80):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

