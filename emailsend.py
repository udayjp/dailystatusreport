import smtplib,ssl
from email.mime.text import MIMEText
import config

class EmailSend:

    def send(email_body):
        try:
            context = ssl.create_default_context()
            host=config.EMAIL_HOST
            port=config.EMAIL_PORT
            sender_email = config.EMAIL_HOST_USER
            receiver_email_list = config.EMAIL_RECEIVER_LIST
            password=config.EMAIL_HOST_PASSWORD
                    
            th=''
            for field in email_body['field_names']:
                th+='<th>'+field+'</th>'

            td=''
            for record in email_body['record']:
                td+='<td>'+record+'</td>'

            email_body_html=''
            with open('report.html','r',encoding = 'utf-8') as html_file:
                email_body_html=html_file.read().format(doc_title=config.EMAIL_SUBJECT,th=th,td=td)

            message=MIMEText(email_body_html,'html')
            message['Subject'] = config.EMAIL_SUBJECT
            message['From'] = sender_email        

            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(sender_email, password)
                for receiver_email in receiver_email_list:
                    message['To'] = receiver_email
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    print("\nEmail sent successfully to email id: ",receiver_email)
        except Exception as e:
            print(e)
