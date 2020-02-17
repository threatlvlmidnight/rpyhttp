from http.server import BaseHTTPRequestHandler, HTTPServer
from gpiozero import CPUTemperature
import socketserver
import os
import time
import subprocess # to get ip address from device
import displayset #local module
import utils #local module
import Timer #local module
import threading
from rgbmatrix import graphics
from MatrixBase import MatrixBase
from samplebase import SampleBase

# TO START THE SERVER:
# OPEN A TERMINAL
# RUN: cd Documents/rpyhttp
# RUN: sudo python server.py --led-slowdown-gpio=2


# Gets the IP address of the PI
IP = subprocess.check_output(["hostname", "-I"]).split()[0]

# Assigns the hostname from above and sets the port number
host_name = str(IP.decode('utf-8'))


# ENTER a host port, 8000, 8080 work. 
host_port = 8080

# # Get CPU temp from GPIOzero library
# cpu = CPUTemperature()
# cpuTemp = cpu.temperature

#Need check button function to run in display loop.



# Initializes a simple HTTP server using the custom BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):
    post_body = " "
    
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
                    <input type="submit" name="pauseButton" value="Pause" />
		    <br>
                    <br>
            </form>
            </body>
        </html> '''
        self.do_HEAD()
        # Display the IP address in the HTML
        self.wfile.write(html.format(host=host_name).encode("utf-8"))
       
    
    
    # Gets and parses text and button input from webpage.
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        self.post_body = self.rfile.read(content_length).decode("utf-8")
        print(self.post_body)
        self.post_Handler()
        self._redirect('/')
    
    # Checks the input of do_POST and controls the flow of the loop
    def post_Handler(self):
        displayPower = utils.postParser(self.post_body)
        print(displayPower)
        
        if displayPower == "Start":
            if globalTimeLeft.pause != True:
                globalTimeLeft.val = 15 * 60
                print('Start')
            else:
                globalTimeLeft.pause = False
            self._redirect('/')
        elif displayPower == "Stop":
            globalTimeLeft.val = 0
            print('Stop')
            self._redirect('/')  
        elif displayPower == "Pause":
            if globalTimeLeft.pause:
                globalTimeLeft.pause = False
            else:
                globalTimeLeft.pause = True
            print('Pause')
            self._redirect('/')  
        
# creates the http server thread    
class myThread (threading.Thread):
    http_server = None
    
    def __init__(self, http_server):
      threading.Thread.__init__(self)
      self.http_server = http_server
      
    def run(self):
#         state = self.http_server.when_to_stop
        print("Server Starts = %s:%s" % (host_name, host_port))
        try:
            self.http_server.serve_forever()
        except KeyboardInterrupt:
            offscreen_canvas.Clear()
            self.http_server.server_close()

# Handles display rendering
class RunText(MatrixBase):
    
#     server = 
    textColor = graphics.Color(0, 255, 0) # <--- Turn into input
    mins = 0
    secs = 0
        
    def run(self):
        print("Running")
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        #offscreen_canvas = CreateFrameCanvas()
        if globalTimeLeft.fontsInit == False:
            globalTimeLeft.font = graphics.Font()
            globalTimeLeft.font.LoadFont("fonts/9x15B.bdf")
            globalTimeLeft.font2 = graphics.Font()
            globalTimeLeft.font2.LoadFont("fonts/5x8.bdf")
            globalTimeLeft.fontsInit = True
        # Update to adjust time calibration
#         delay = 0
        pause = False
        
        offscreen_canvas.Clear()
#         time.sleep(delay)
        if globalTimeLeft.val > 0:
            m, s = divmod(globalTimeLeft.val, 60)
            h, m = divmod(m, 60)
            self.mins = str(m).zfill(2)
            self.secs = str(s).zfill(2)
            graphics.DrawText(offscreen_canvas, globalTimeLeft.font, 8, 13, self.textColor, self.mins)
            graphics.DrawText(offscreen_canvas, globalTimeLeft.font, 8, 29, self.textColor, self.secs)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            if globalTimeLeft.pause == False:
                globalTimeLeft.val -= 1;
            time.sleep(1)
        else:
#             firstIndex = host_name.index('.')
#             first = host_name[:firstIndex]
#             print(first)
#             secondIndex = host_name[firstIndex+1:].index('.')
#             second = host_name[firstIndex:secondIndex]
#             print(second)
#             thirdIndex = host_name[secondIndex+2:].index('.')
#             third = host_name[secondIndex:thirdIndex]
#             print(third)
#             fourthIndex = host_name[thirdIndex+3:].index('.')
#             fourth = host_name[thirdIndex:fourthIndex]
#             print(fourth)
#             graphics.DrawText(offscreen_canvas, font2, 0, 7, self.textColor, str(host_name[:8]))
            graphics.DrawText(offscreen_canvas, globalTimeLeft.font2, 0, 9, self.textColor, str(host_name[:7]))
            graphics.DrawText(offscreen_canvas, globalTimeLeft.font2, 0, 19, self.textColor, str(host_name[6:]))
            graphics.DrawText(offscreen_canvas, globalTimeLeft.font2, 0, 29, self.textColor, ":"+str(host_port))
            print(str(host_name[:7]))
            print(str(host_name[4:]))
            print(":"+str(host_port))
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(1)
   
class globalTimeLeft:
    val = 0
    pause = False
    fontsInit = False
    
    def getVal():
        return globalTimeLeft.val


    
if __name__ == '__main__':
    #displayIP = displayIP()
    print('Main object init')
    #display_IP.displayHost(host_name)

    http_server = HTTPServer((host_name, host_port), MyServer)
#     run_text = RunText()
    thread = myThread(http_server)
    thread.start()
    # DISPLAY host_name ON TIMER
    
    try:
        while True:
            run_text = RunText()
            if (not run_text.process()):
                run_text.print_help()
    except KeyboardInterrupt:
        offscreen_canvas.Clear()
        self.http_server.server_close()
        
    
        
    

    

######## NOTES ######## 


    #offscreen_canvas = self.matrix.CreateFrameCanvas()
    
    #def __init__(self, *args, **kwargs):
        #super(RunText, self).__init__(*args, **kwargs)
        #self.parser.add_argument("-t", "--text", help="The text to display on the RGB Matrix", default="A0:00")