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

        #Display the outputs
        print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
        print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())

#Execute the main method of the TestTV class
TestTV().main()