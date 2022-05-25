from pynput.mouse import Listener 


#function that writes mouse positions to file mouse
def mouse_position(x,y):
 
    f = open("mouse.txt","a")
    f.write("Current pointer position is: {0} \n ".format((x,y)))
    f.close() 
    
with Listener (on_move=mouse_position) as l_m:
  
  l_m.join()
