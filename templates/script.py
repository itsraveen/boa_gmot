from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        form_data = urllib.parse.parse_qs(post_data)

        client = form_data["client"][0]
        commission = form_data["commission"][0]
        gross_amount = form_data["gross_amount"][0]

        print("Client:", client)
        print("Commission:", commission)
        print("Gross Amount:", gross_amount)

        clientCommission = 0
        clientGrossAmount = 0
        clientCommissionTolerance = 0
        clientGrossAmountTolerance = 0

        if abs(clientCommission - int(commission)) > clientCommissionTolerance:
            error_message = "Commission exceeds the client's commission."
            self.send_error_response(error_message)
            return

        if abs(clientGrossAmount - int(gross_amount)) > clientGrossAmountTolerance:
            error_message = "Gross amount exceeds the client's gross amount."
            self.send_error_response(error_message)
            return

        print("Client:", client)
        print("Commission:", commission)
        print("Gross Amount:", gross_amount)

        self.send_success_response()

    def send_success_response(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_data = json.dumps({"status": "success"})
        self.wfile.write(response_data.encode("utf-8"))

    def send_error_response(self, error_message):
        self.send_response(400)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_data = json.dumps({"status": "error", "message": error_message})
        self.wfile.write(response_data.encode("utf-8"))


def run_server():
    server_address = ("", 5501)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Starting server...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
