
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        print("Got post request\n")

        # Parse the form data posted
        form = cgi.FieldStorage(
                                fp=self.rfile, 
                                headers=self.headers,
                                environ={'REQUEST_METHOD':'POST',
                                         'CONTENT_TYPE':self.headers['Content-Type'],
                                        })
        print("Post Form: %s\n" % str(form))

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')

        # Echo back information about what was posted in the form
        for field in form.keys():
            value = form.getvalue(field)
            print("Key: %s Value: %s" % (str(field),str(value)))

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use  to stop'
    server.serve_forever()