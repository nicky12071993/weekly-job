import sys
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

    receiver_emails = sys.argv[1]
    receiver_emails_list = receiver_emails.split(',')

    sender_email = sys.argv[2]
    sender_password = sys.argv[3]

    email_subject = sys.argv[4]
    email_body = sys.argv[5]
                
    email_server_address = sys.argv[6]
    email_server_port_number = int(sys.argv[7])

    email_message = EmailMessage()
    email_message['From'] = sender_email
    email_message['To'] = ", ".join(receiver_emails_list)
    email_message['Subject'] = email_subject
    email_message.set_content(email_body)

    send_email(email_server_address, email_server_port_number, sender_email, sender_password, receiver_emails_list, email_message)