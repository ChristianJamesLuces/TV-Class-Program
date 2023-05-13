#Import the necessary module
import tkinter as tk
import tkinter.font as tkFont

#Import the TV file
from TV import TV

#Define the TestTV class
class TestTV:
    #Main method to test the class
    def main(self):
        #Create two TV objects
        tv1 = TV()
        tv2 = TV()

        #Turn on TV1 and set its channel and volume level
        tv1.turnOn()
        tv1.setChannel(30)
        tv1.setVolume(3)

        #Turn on TV2 and set its channel and volume level
        tv2.turnOn()
        tv2.setChannel(3)
        tv2.setVolume(2)

        #Output strings for TV1 and TV2
        output1 = f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}"
        output2 = f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}" 

        #Create the root window
        root = tk.Tk()
        root.title("Output Window")
        root.geometry("400x100")

        #Create a custom font object
        font = tkFont.Font(family = "Century Gothic", size = 12)

        #Create a label widget to display the output
        label = tk.Label(root, text = output1 + "\n" + output2, font = font, width = 500, height = 200, bg = "black", fg = "yellow")
        label.pack()

        #Start the tkinter event loop
        root.mainloop()

#Execute the main method of the TestTV class
TestTV().main()