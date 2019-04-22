import argparse
import time
from AlarmClass import Alarm

def credit():
    rulerzCredit =  """ 
                _                ___   __   
     _ __ _   _| | ___ _ __ ____/ _ \ / /_  
    | '__| | | | |/ _ \ '__|_  / (_) | '_ \ 
    | |  | |_| | |  __/ |   / / \__, | (_) |
    |_|   \__,_|_|\___|_|  /___|  /_/ \___/ 
        """
    return rulerzCredit
                                        
def alarmMenuArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=credit())
    parser.add_argument('-s', '--set', help="set the time you want to wake up", action='store_true')
    parser.add_argument("hour", type=int, help="change this with hour you want to wake up")
    parser.add_argument("minute", type=int, help="change this with minutes you want to wake up")
    args = parser.parse_args()
    if args.set:
        alarmLogic(args.hour, args.minute)
    

        
def alarmLogic(hour, minute):
    alarm = Alarm()
    alarm.setWakeUpTime(hour, minute)
    alarm.clearScreen()
    alarm.printWakeUpTime()
    try:
        while alarm.isClosed() is not True:
            currHour, currMinute = alarm.getCurrentTime()
            if currHour == alarm.getHour() and currMinute == alarm.getMinute():
                alarm.setMasterVolume()
                for times in range(30):
                    alarm.espeakMessage()
                    alarm.playSound()
                    alarm.playSound()
                    time.sleep(0.4)
                alarm.setCloseFlag(True)
                alarm.clearScreen()
                alarm.printFinishMessage()
            time.sleep(20)
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    alarmMenuArguments()
    