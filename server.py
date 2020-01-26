from http.server import HTTPServer, SimpleHTTPRequestHandler
from io import BytesIO

# создает сервер
class Server(SimpleHTTPRequestHandler):
# создает get
    def do_Get(self):
        if self.path == '/':
            self.path = 'index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
# создает post
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_len)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("data", post_data)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        self.wfile.write(response.getvalue())


#запустить сервер
httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()
