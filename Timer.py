# from samplebase import SampleBase
from rgbmatrix import graphics
import time
import utils
from MatrixBase import MatrixBase
from samplebase import SampleBase


class RunText(MatrixBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to display on the RGB Matrix", default="A0:00")
        
        
    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/9x15B.bdf")
        textColor = graphics.Color(0, 0, 255) # <--- Turn into input
        pos = 0 
        my_text = self.args.text
        when_to_stop = abs(int(input(" "))) * 60
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
                
            graphics.DrawText(offscreen_canvas, font, 8, 13, textColor, 00)
            graphics.DrawText(offscreen_canvas, font, 8, 29, textColor, 00)
                
        
            max_brightness = self.matrix.brightness
            count = 0
            c = 255

            while True:
                if self.matrix.brightness < 1:
                    self.matrix.brightness = max_brightness
                    count += 1
                else:
                    self.matrix.brightness -= 1

                if count % 4 == 0:
                    self.matrix.Fill(c, 0, 0)
                elif count % 4 == 1:
                    self.matrix.Fill(0, c, 0)
                elif count % 4 == 2:
                    self.matrix.Fill(0, 0, c)
                elif count % 4 == 3:
                    self.matrix.Fill(c, c, c)

                self.usleep(20 * 1000)
    
            



# Main function
#print(__name__)

if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()


