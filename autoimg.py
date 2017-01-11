import easygui
import urllib.request
import os
import time

number_of_images = easygui.integerbox("How many images?")
image_width = easygui.integerbox("Width of the image?", "", "", 0, 5000)
image_height = easygui.integerbox("Height of the image?", "", "", 0, 5000)
base_url = "https://unsplash.it/" #/500/500?random
#Read back args to user to ensure they are correct
if easygui.ccbox("You choose "+str(number_of_images)+" images. With a width of "+str(image_width)+" and a height of "+str(image_height)+". Is this correct?", "Please confirm"):
	#Select folder for images
	image_dir = easygui.diropenbox()
	#MAGIC TIME
	for i in range(1, number_of_images+1):
		urllib.request.urlretrieve(base_url+str(image_width)+"/"+str(image_height)+"?random", os.path.join(image_dir, "placeholder"+str(i)+".jpg"))
		urllib.request.urlcleanup()
	easygui.msgbox("All done, your images are located in "+image_dir+" . Click OK to quit.")
else:
	easygui.msgbox("Script aborted. Please re-run to try again. Okey dokey bye bye.")