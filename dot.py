from microbit import *

x_offset = 2
y_offset = 2

x = 0
napravlenie = "right"
while True:    
    display.set_pixel(x,2,9)
    sleep(200)
    display.clear()
    if x == 4 or (x != 0 and button_a.was_pressed()):
        napravlenie = "left"
    elif x == 0 or (x != 4 and button_b.was_pressed()):
        napravlenie = "right"
    if napravlenie == "right":
        x = x + 1
    else:
        x = x - 1
                
    
    
 #   x = int(accelerometer.get_x() / 500 + x_offset)
 #   y = int(accelerometer.get_y() / 500 + x_offset)
  #  display.set_pixel(x,y,9)
 #   sleep(200)
 #   display.clear()