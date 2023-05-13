class TV:
    #Default values for channel, volumelevel, and TV state
    def __init__(self):
        self.channel = 1
        self.volumelevel = 1
        self.on = False

    #Turn on the TV
    def turnOn(self):
        self.on = True

    #Turn off the TV
    def turnoff(self):
        self.on = False

    #Get the current channel
    def getChannel(self):
        return self.channel
    
    #Set a new channel
    def setChannel(self,channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    #Gets the volume level
    def getVolume(self):
        return self.volumelevel
    
    #Sets a new volume level
    def sefVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumelevel = volumeLevel

    #Increases the channel number by 1
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    #Decreases the channel number by 1
    #Increases the volume level by 1
    #Decreases the volume level by 1
