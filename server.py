from http.server import BaseHTTPRequestHandler, HTTPServer
from sense_hat import SenseHat # hardware library
from gpiozero import CPUTemperature
import socketserver
import os
import time
import subprocess # to get ip address from device
import displayset #local module
import utils #local module


# Gets the IP address of the PI
IP = subprocess.check_output(["hostname", "-I"]).split()[0]

# Assigns the hostname from above and sets the port number
host_name = str(IP.decode('utf-8'))


# ENTER a host port, 8000, 8080 work. 
host_port = 8000

# Get CPU temp from GPIOzero library
cpu = CPUTemperature()
cpuTemp = cpu.temperature

# SenseHat setup, REMOVE in final build
    # Moved to displayset module


# F U N C T I O N S

# Assings RGB values to text color inputs
    # Moved to displayset module





# Initializes a simple HTTP server using the custom BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):
    
    # HEAD function
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    # Basic redirect
    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()
        
    # GET function, includes the main HTML of the web page    
    def do_GET(self):
        html = '''
        <html>
            <head>
                <title>SmartTimer</title>
            </head>
            <body style="width:960px; margin: 20px auto;">
                <h1  style="font-family:Helvetica;">Welcome to the CLGX SmartTimer</h1>
            		<h2  style="font-family:Helvetica;">SmartTimer Status:</h2>
		    <ul style="font-family:Helvetica;">
			    <li>Address: {host}</li>
			    <li>Connection: Online</li>
			    <li>Current Timer: Idle</li>
			    <li>CPU Temp: C</li>
		    </ul>
                <br>
            <form action="" method="post" style="font-family:Helvetica;">
				<h3>Timer Controls:</h3>
                    <b>Enter your message:</b>
                    <br>
                    <input type="text" name="message"><br>
                    <br>
                    <b>Color:</b>
                    <br>
                    <input type="text" name="color"><br>
                    <br>
                    <b>Rotation:</b>
                    <br>
                    <input type="text" name="rotation"><br>
                    <br>
                    Turn the light on or off: <br>
                    <input type="submit" name="onButton" value="On" />
                    <input type="submit" name="offButton" value="Off" />
            </form>
            </body>
        </html>
        '''
        self.do_HEAD()
        # Display the IP address in the HTML
        self.wfile.write(html.format(host=host_name).encode("utf-8"))
        # Display the device connection status
        
        # Display the status of the current timer
        
        # Display the current cpu temp
        #self.wfile.write(html.format(cpu=cpuTemp).encode("utf-8"))
    
    
    # Gets and parses text and button input from webpage. Needs to be migrated to its own function/module at somepoint
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length).decode("utf-8")
        print(post_body)
        
        displayset.showMessage(post_body)
        
        self._redirect('/')
        
    
    
    
if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts = %s:%s" % (host_name, host_port))
    
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


        
    

    




