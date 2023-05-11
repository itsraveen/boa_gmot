from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import sqlite3


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        form_data = urllib.parse.parse_qs(post_data)

        client = form_data["client"][0]
        clientCommissionTolerance = form_data["commission"][0]
        clientGrossAmountTolerance = form_data["gross_amount"][0]

        #print("Client:", client)
        #print("Commission:", clientCommissionTolerance)
        #print("Gross Amount:", clientGrossAmountTolerance)

        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Specify the values to be inserted into the database
        val = (client, clientCommissionTolerance, clientGrossAmountTolerance)
        
        # Prepare the SQL query to insert data
        sql = "INSERT INTO client_config (client, commission, gross_amount) VALUES (?, ?, ?)"
        cursor.execute(sql, val)
        
        # Commit the changes to the database
        conn.commit()

def run_server():
    server_address = ("", 5501)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Starting server...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
