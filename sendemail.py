def sendemail(subject, msg):
        import smtplib, getpass, sys
        gmail_user = "vinod.halaharvi@gmail.com"
        gmail_pwd = 'bkabovsodltmldpb'
        FROM = 'vinod.halaharvi@gmail.com'
        TO = ['vinod.halaharvi@gmail.com'] 
        SUBJECT = subject
        TEXT = msg

        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
                server = smtplib.SMTP("smtp.gmail.com", 587) 
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                server.close()
                print 'successfully sent the mail'
        except:
                raise
                print "failed to send mail"

send_email()
