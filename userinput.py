from datetime import datetime
from validation import Validation
import config


class UserInput:

    def user_input():
        print("\n*****User Input*****\n")

        user_data=[] 
        while True:       
            topics=input("Enter topics: ")
            if len(topics)>0 and len(topics)<256 and Validation.is_alpha_numeric_specialchar(topics):
                user_data.append(topics)
                break
            else:
                print("Accepts only alphaNumeric, special characters. Max Len:255 Chars ")
        
        while True:       
            content=input("Enter contents: ")
            if len(content)>0 and len(content)<256 and Validation.is_alpha_numeric_specialchar(content):
                user_data.append(content)
                break
            else:
                print("Accepts only alphanumeric, special characters. Max Len:255 Chars ")

        while True:       
            start_date=input("Enter start date in format DD/MM/YYYY : ")            
            if Validation.is_valid_date(start_date):
                start_date_object = datetime.strptime(start_date, "%d/%m/%Y")
                start_date=start_date_object.strftime(config.DATE_FORMAT)
                user_data.append(start_date)
                break
            else:
                print("Date format should be DD/MM/YYYY, Do not accept future dates ")

        while True:       
            end_date=input("Enter end date in format DD/MM/YYYY : ")
            if Validation.is_valid_date(end_date):
                end_date_object = datetime.strptime(end_date, "%d/%m/%Y")
                end_date=end_date_object.strftime(config.DATE_FORMAT)
                date_difference=end_date_object-start_date_object
                if date_difference.days>=0:
                    user_data.append(end_date)
                    break
                else:
                    print("End date should be greater than equal to start date")
            else:
                print("Date format should be DD/MM/YYYY, Do not accept future dates ")

        while True:     
            progress=input("Progress (Completed, In-Progress). \nfor Completed press 1, for In-Progress press 2 : ")
            if progress=="1":
                user_data.append("Completed")
                break
            elif progress=="2":
                user_data.append("In-Progress")
                break
            else:
                print("Accepts only values [ Completed, In-Progress] ")
        
        while True:  
            confidence_level=input("Enter confidence level (High, Medium, Low)\nPress 1 for High, Press 2 for Medium, Press 3 for Low : ")   
            if confidence_level=="1":
                user_data.append("High")
                break
            elif confidence_level=="2":
                user_data.append("Medium")
                break
            elif confidence_level=="3":
                user_data.append("Low")
                break
            else:
                print("Accepts Only Values [ High, Medium, Low] ")
        
        while True:       
            team_member=input("Enter team member name: ")
            if len(team_member)>0 and len(team_member)<101 and Validation.is_alpha_numeric(team_member):
                user_data.append(team_member)
                break
            else:
                print("Accepts only alphaNumeric. Max Len: 100 Chars ")
        
        while True:       
            comments=input("Enter comments: ")
            if len(comments)>0 and len(comments)<1025 and Validation.is_alpha_numeric_specialchar(comments):
                user_data.append(comments)
                break
            else:
                print("Accepts only alphaNumeric and special characters. Max Len:255 Chars ")

        
        return tuple(user_data)

