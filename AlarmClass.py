import os
import datetime

class Alarm:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.volume = "100%"
        self.alarmMessage = 'Wake\ up\ you\ sleepy\ bastard!'
        self.soundPath = "sound/bomb.mp3"
        self.closeFlag = True

    def setWakeUpTime(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.closeFlag = False

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def setCloseFlag(self, closeFlag):
        self.closeFlag = closeFlag

    def playSound(self):
        os.system("mpg123 {}".format(self.soundPath))

    def espeakMessage(self):
        os.system("espeak {}".format(self.alarmMessage))

    def setMasterVolume(self):
        os.system("amixer sset Master {}".format(self.volume))

    def getCurrentDay(self):
        currentDay = datetime.date.today().day
        return currentDay

    def getCurrentTime(self):
        currentHour = datetime.datetime.now().hour
        currentMinute = datetime.datetime.now().minute
        return currentHour, currentMinute

    def isClosed(self):
        return self.closeFlag

    def printWakeUpTime(self):
        print("\n[*] Alarm set at {} : {}".format(self.hour, self.minute))

    def printFinishMessage(self):
        print("\n[*] Alarm finished successfully.")
        print("\n[*] Closing in 20 seconds.\n")

    def clearScreen(self):
        os.system("clear")
