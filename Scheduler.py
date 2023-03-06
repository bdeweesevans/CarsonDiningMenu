'''Notes:
Run this file to initiate the program to execute automatically.
'''
# Import statements.
import schedule, time, Main

job = Main.main()
schedule.every().day.at('10:00').do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)