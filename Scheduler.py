'''Notes:
Run this file to initiate the program to execute automatically.
'''
# Import statements.
import schedule, time, Main

execution_time = '08:00'

print(f'Program Started at {time.ctime()}')
print(f'Program will run at {execution_time}.')

schedule.every().day.at(execution_time).do(Main.main)  #Must be in UTC Time if run on EC2 Instance, unless run locally.

while True:
    schedule.run_pending()
    time.sleep(1)