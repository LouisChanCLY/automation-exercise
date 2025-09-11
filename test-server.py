#!/usr/bin/env python3
"""
Simple HTTP server that serves Jekyll site under /automation-exercises/ path
to mirror GitHub Pages structure
"""
import http.server
import socketserver
import os
from urllib.parse import urlparse

class SubdirectoryHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="docs", **kwargs)

    def translate_path(self, path):
        # Remove the /automation-exercises prefix if present
        if path.startswith('/automation-exercises'):
            path = path[len('/automation-exercises'):]
            if not path:
                path = '/'

        # Call parent's translate_path with modified path
        result = super().translate_path(path)
        return result

    def end_headers(self):
        # Add CORS headers for testing
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    PORT = 8000
    Handler = SubdirectoryHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}/automation-exercises/")
        print(f"Serving files from: {os.path.abspath('docs')}")
        httpd.serve_forever()
