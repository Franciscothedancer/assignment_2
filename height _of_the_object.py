# Created by: Francisco Lee
# Created on : Oct 2017
# Created for: ICS3U
# This program calculates the height of the object 

import ui

def calculate_button_touch_up_inside(sender):
    # calculate the height of the object
	
    # constants
    GRAVITY = 9.81
    
    #input
    seconds = (view['height_textbox'].text)
    
    #process
    height = (100-1/2)*(GRAVITY*seconds**2)
    
    #output
    view['answer_label'].text = 'the heigt of object is:'

view= ui.load_view()
view.present('full_screen')
