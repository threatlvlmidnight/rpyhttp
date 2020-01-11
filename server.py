from http.server import BaseHTTPRequestHandler, HTTPServer
from gpiozero import CPUTemperature
import socketserver
import os
import time
import subprocess # to get ip address from device
import displayset #local module
import utils #local module
import Timer #local module
from rgbmatrix import graphics
from MatrixBase import MatrixBase
from samplebase import SampleBase


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
            		
                <br>
            <form action="" method="post" style="font-family:Helvetica;">
				<h3>Start Timer</h3>
                    
		    Start 15 minute timer:
		    <br>
		    <br>
                    <input type="submit" name="onButton" value="Start" />
                    <input type="submit" name="offButton" value="Stop" />
		    <br>
		    <br>
		    <br>
		    <b>Enter a custom duration:</b>
		    <br>
                    <input type="text" name="duration"><br>
                    <br>
            </form>
            </body>
        </html> '''
        self.do_HEAD()
        # Display the IP address in the HTML
        self.wfile.write(html.format(host=host_name).encode("utf-8"))
       
    
    
    # Gets and parses text and button input from webpage. Needs to be migrated to its own function/module at somepoint
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length).decode("utf-8")
        print(post_body)
        displayPower = utils.postParser(post_body)
        displayText = RunText()
        
        
            #displayText.run()
            
        if displayPower == "Start":
            run_text = RunText()
        if (not run_text.process()):
            run_text.print_help()
        
        #displayset.showMessage(post_body)
        
        
        self._redirect('/')

class RunText(MatrixBase):
    name = "test"
    
    #offscreen_canvas = self.matrix.CreateFrameCanvas()
    
    #def __init__(self, *args, **kwargs):
        #super(RunText, self).__init__(*args, **kwargs)
        #self.parser.add_argument("-t", "--text", help="The text to display on the RGB Matrix", default="A0:00")
        
    #@classmethod    
    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        #offscreen_canvas = CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/9x15B.bdf")
        textColor = graphics.Color(0, 255, 0) # <--- Turn into input
        pos = 0 
        #my_text = self.args.text
        when_to_stop = 15 * 60 #abs(int(input(" "))) * 60
        # Update to adjust time calibration
        delay = 0
        
            
        while True:
            
            while when_to_stop >= 0:

                m, s = divmod(when_to_stop, 60)
                h, m = divmod(m, 60)
                time_left = str(m).zfill(2) + ":" + str(s).zfill(2)       
                time.sleep(1)
                when_to_stop -= 1
                mins = str(m).zfill(2)
                secs = str(s).zfill(2)
                offscreen_canvas.Clear()
                thisClass = utils.RunText()
                print(mins + secs)
                graphics.DrawText(offscreen_canvas, font, 8, 13, textColor, mins)
                graphics.DrawText(offscreen_canvas, font, 8, 29, textColor, secs)
                
                
                time.sleep(delay)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                
                if when_to_stop == 0:
                    when_to_stop -= 1
                
            graphics.DrawText(self.offscreen_canvas, font, 8, 13, textColor, 00)
            graphics.DrawText(self.offscreen_canvas, font, 8, 29, textColor, 00)
    
    
    
if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts = %s:%s" % (host_name, host_port))
    
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


        
    

    




