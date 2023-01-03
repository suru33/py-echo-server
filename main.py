import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
port = 9000

encoding = "utf-8"
type_json = "application/json"


class PyEchoServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", type_json)
        self.end_headers()
        test_data = {
            "int": 100,
            "str": "Hello World",
            "bool": False,
            "array": [1, 2, 3, 4],
            "obj": {
                "key": "value"
            }
        }
        self.wfile.write(bytes(json.dumps(test_data), encoding))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", type_json)
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    webServer = HTTPServer((host_name, port), PyEchoServer)
    print(f"Server started at: http://{host_name}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
