import re
import datetime 

class Validation:

    def is_alpha_numeric(input_str):
        regex = '[a-zA-Z0-9_]'
        return bool(re.match(regex, input_str))     

    def is_alpha_numeric_specialchar(input_str):
        regex="^[a-zA-Z0-9_ !@#$&()\\-`.+,/\"]*$"
        return bool(re.match(regex, input_str))  

    def is_valid_date(input_date):      
        
        valid_date = True
        try :                   
            day,month,year = input_date.split('/')                      
            entered_date=datetime.date(int(year),int(month),int(day))
            today = datetime.date.today() 
            date_difference= today-entered_date
            if int(date_difference.days) < 0:
                valid_date = False
        except ValueError :
            valid_date = False
        
        return valid_date
