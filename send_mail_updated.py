import smtplib
from email.message import EmailMessage

def send_email(email_server_address, email_server_port_number, sender_email, sender_password, receiver_emails_list, email_message):
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

if __name__ == '__main__':
    receiver_emails_list = ['nicky09058@gmail.com','nicky12071993@gmail.com']

    sender_email = 'acekuber@gmail.com'
    sender_password = 'mkuskpjjliwkdnqo'

    email_subject = 'hi subject from jenkins python code!'
    email_body = 'hi there email from jenkins python code'
                
    email_server_address = 'smtp.gmail.com'
    email_server_port_number = 587

    email_message = EmailMessage()
    email_message['From'] = sender_email
    email_message['To'] = ", ".join(receiver_emails_list)
    email_message['Subject'] = email_subject
    email_message.set_content(email_body)

    send_email(email_server_address, email_server_port_number, sender_email, sender_password, receiver_emails_list, email_message)