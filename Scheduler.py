'''Notes:
Run this file to initiate the program to execute automatically.
'''
# Import statements.
import schedule, time, Main

schedule.every().day.at('10:00').do(Main.main)

while True:
    schedule.run_pending()
    time.sleep(1)