##### General Utility Functions for rpyhttp ###
import displayset # local module
        
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
    
        
        
