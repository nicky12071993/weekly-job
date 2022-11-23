import smtplib, ssl
from email.message import EmailMessage

receiver_emails = input('enter receiver email list seperated by commas ') #['nicky09058@gmail.com']
receiver_emails_list = receiver_emails.split(',')

sender_email = input('enter sender email ')
sender_password = input('enter sender email password ') #'mkuskpjjliwkdnqo'

email_subject = input('enter email message subject ') #'hi subject from python code!'
email_body = input('enter email message body ') #hi there email1 from python code
            
email_server_address = input('enter email server address ') #'smtp.gmail.com'
email_server_port_number = input('enter email server port number ') #587

email_message = EmailMessage()
email_message['From'] = sender_email
email_message['To'] = ", ".join(receiver_emails_list)
email_message['Subject'] = email_subject
email_message.set_content(email_body)

try:
    smtp_server = smtplib.SMTP(email_server_address, email_server_port_number)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    smtp_server.sendmail(sender_email, receiver_emails_list, email_message.as_string())
    print('email sent to {}'.format(receiver_emails_list))
except smtplib.SMTPException as e:
    print('error occurred')
    raise e
finally:
    smtp_server.quit()