##### General Utility Functions for rpyhttp ###
import displayset # local module
import time
        
def postParser(post_body):
    post_body = post_body.split("&")
    post_c = post_body[1]
    post_p = post_body[3]
    post_m = post_body[0]
    post_r = post_body[2]
    post_c = post_c.split("=")
    post_p = post_p.split("=")
    post_m = post_m.split("=")
    post_r = post_r.split("=")
    color = post_c[1]
    power = post_p[1]
    message = post_m[1]
    rotation = int(post_r[1])
    message2 = message.split("+")
    message = (' '.join(message2))#.encode("utf-8")
    
    color = displayset.returnRGB(color)
    
    return color, message, power, rotation
    
    

def timer():
    while True:
        uin = input(">> ")
        uin = abs(int(uin))
        try:
            when_to_stop = int(uin)
        except KeyboardInterrupt:
            break
        #except when_to_stop == 0:
            #break
        except:
            print("Invalid input")
            
        while when_to_stop >= 0:
            #print(when_to_stop)
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            #return time_left
            print(time_left + '\r', end="")
            time.sleep(1)
            when_to_stop -= 1
            
        
        
