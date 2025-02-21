import base64
import hashlib
import http.server
import json
import os
import secrets
import socketserver
import urllib.parse

import requests

PORT = int(os.environ.get("PORT", 8080))

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    last_code = None

    def do_GET(self):
        # Check if this is the callback URL
        if self.path.startswith('/?'):

            url_parts = urllib.parse.urlparse(self.path)
            query_params = urllib.parse.parse_qs(url_parts.query)
            code = query_params.get('code')

            if code:
                SimpleHTTPRequestHandler.last_code= code[0] # store for later use
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"<html><body><h1>Authorization successful!</h1><p>You can now close this window.</p></body></html>")
                return

        # Standard HTTP file handling
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()


def run_server():
    """Starts the HTTP server."""
    httpd = socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever() # This will keep running. Use a different method if you want to control termination


if __name__ == "__main__":
    run_server()