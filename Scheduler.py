'''Notes:
Run this file to initiate the program to execute automatically.
'''
# Import statements.
import schedule, time, Main

print(f'Program Started at {time.ctime()}')
schedule.every().day.at('18:00').do(Main.main)  #Must be in UTC Time if run on EC2 Instance, unless run locally.

while True:
    schedule.run_pending()
    time.sleep(1)