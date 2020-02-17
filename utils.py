##### General Utility Functions for rpyhttp ###
#import displayset # local module
import time
#import showText2
from rgbmatrix import graphics
import utils
from MatrixBase import MatrixBase
from samplebase import SampleBase
        
def postParser(post_body):
    post_body = post_body.split("&")
    post_start = post_body[0].split("=")
    start = post_start[1]
    
    return start
    
    
    #post_c = post_body[1]
    #post_p = post_body[3]
    #post_m = post_body[0]
    #post_r = post_body[2]
    #post_c = post_c.split("=")
    #post_p = post_p.split("=")
    #post_m = post_m.split("=")
    #post_r = post_r.split("=")
    #color = post_c[1]
    #power = post_p[1]
    #message = post_m[1]
    #rotation = int(post_r[1])
    #message2 = message.split("+")
    #message = (' '.join(message2))#.encode("utf-8")
    
    #color = displayset.returnRGB(color)
    
    #return color, message, power, rotation

# class RunText(MatrixBase):
#     def __init__(self, *args, **kwargs):
#         super(RunText, self).__init__(*args, **kwargs)
#         self.parser.add_argument("-t", "--text", help="The text to display on the RGB Matrix", default="A0:00")
#     
# 
#     def timer(self):
#         offscreen_canvas = self.matrix.CreateFrameCanvas()
#         font = graphics.Font()
#         font.LoadFont("fonts/9x15B.bdf")
#         textColor = graphics.Color(0, 0, 255) # <--- Good candidate for new function
#         pos = 0 #offscreen_canvas.width
#     
#         while True:
#             uin = abs(int(input(" ")))
#         
#             try:
#                 when_to_stop = uin
#             except KeyboardInterrupt:
#                 break
#         #except when_to_stop == 0:
#             #break
#             except:
#                 print("Invalid input")
#             
#             while when_to_stop >= 0:
#                 #print(when_to_stop)
#                 m, s = divmod(when_to_stop, 60)
#                 h, m = divmod(m, 60)
#                 time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
#             #return time_left
#                 #print(time_left + '\r', end="")
#                 #graphics.DrawText(offscreen_canvas, font, 4, 13, textColor, time_left)
#                 #graphics.DrawText(offscreen_canvas, font, 20, 13, textColor, q2)
#                 #graphics.DrawText(offscreen_canvas, font, 4, 29, textColor, q3)
#                 #graphics.DrawText(offscreen_canvas, font, 20, 29, textColor, q4)
#             
#             #return time_left
#                 time.sleep(1)
#                 when_to_stop -= 1
            
        
        
