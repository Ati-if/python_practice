import datetime
import time
import os  # For playing sound (on Windows)

def get_alarm_time():
    alarm_input = input("Set alarm (HH:MM:SS, 24-hour format): ")
    try:
        alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M:%S").time()
        return alarm_time
    except ValueError:
        print("Invalid format. Please use HH:MM:SS (e.g., 07:30:00)")
        return get_alarm_time()

def alarm_clock():
    alarm_time = get_alarm_time()
    print(f"Alarm set for {alarm_time}")

    while True:
        now = datetime.datetime.now().time()
        if now >= alarm_time:
            print("⏰ Alarm! Wake up!")
            try:
                # Plays sound if you have a .wav file
                os.system("start alarm.wav")  # For Windows
                # os.system("afplay alarm.wav")  # macOS
                # os.system("aplay alarm.wav")  # Linux
            except:
                print("Couldn't play alarm sound.")
            break
        time.sleep(1)

alarm_clock()
