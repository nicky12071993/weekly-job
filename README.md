# weekly-job

* Create a jenkins pipeline
    * -parameterize with the following parameters of string type
        * receiver_emails
        * sender_email
        * sender_password
        * email_subject
        * email_body
        * email_server_address
        * email_server_port_number
    * -build periodically with schedule; H 9 * * 6
    * -use the jenkins file: Jenkinsfile
    * -use the python file: send_mail_args.py
* Run the job
