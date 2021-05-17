import csv
import os
import config
from userinput import UserInput
from emailsend import EmailSend

class DailyStatusReport:    
    
    def create_daily_status_report(self):  
        try:
            report_file= config.FILE_PATH+"\\"+config.FILE_NAME  
            field_names = (
                            'Topics', 
                            'Content',
                            'Start Date',
                            'End Date',
                            'Progress (Completed, In progress)',
                            'Confidence Level 1.High – Ready to work on deliverables 2.Medium – Understood but have some queries 3.Low – No confidence',
                            'Team Member',
                            'Comments',                
            )
                
            with open(report_file,'a',encoding = 'utf-8') as csv_file:
                    
                writer = csv.writer(csv_file, delimiter = config.DELIMETER)

                if os.stat(report_file).st_size == 0:
                    writer.writerow(field_names)
                
                record=UserInput.user_input()
                writer.writerow(record)

                email_body={'field_names':field_names,'record':record}
                EmailSend.send(email_body)
                print("\n********Daily Status Report Created Successfully*******\n")
        except Exception as e:
            print(e)

if __name__=="__main__":
    print("\n*****Daily Status Report*****\n")
    
    status_report=DailyStatusReport()

    while True:
        print("To create daily status report press 1")
        print("To exit press anyother key \n")
        choice=input("Enter your choice: ")

        if choice=="1":
            status_report.create_daily_status_report()
        else:
            break
