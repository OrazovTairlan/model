import http.server
import socketserver

# Define the port number
PORT = 3000

# Define the handler for the HTTP requests
class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    # Override the do_POST method to serve the zip file
    def do_POST(self):
        # Set the response status code
        self.send_response(200)
        # Set the Content-Type header to indicate that the response is a zip file
        self.send_header('Content-Type', 'application/zip')
        # Set the Content-Disposition header to suggest a filename for the downloaded file
        self.send_header('Content-Disposition', 'attachment; filename="example.zip"')
        # End the headers
        self.end_headers()
        # Open and read the zip file
        with open('example.zip', 'rb') as f:
            # Send the contents of the zip file as the response body
            self.wfile.write(f.read())

# Create an HTTP server listening on localhost port 3000
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Server running at port", PORT)
    # Start the server
    httpd.serve_forever()