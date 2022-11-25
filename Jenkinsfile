pipeline{
agent any
stages {
	stage ('scheduleweekyjob - Checkout') {
	    steps{
 	 checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '0bf33df5-8719-4556-9def-dd2ef9ba3347', url: 'https://github.com/nicky12071993/weekly-job.git']]]) 
	}}
	stage ('scheduleweekyjob - Build') {
	    steps{
sh """ 
/Users/i334235/opt/anaconda3/bin/python /Users/i334235/.jenkins/workspace/scheduleweekyjob/send_mail_args.py $receiver_emails $sender_email $sender_password $email_subject $email_body $email_server_address $email_server_port_number 
 """ 
}}
}}
