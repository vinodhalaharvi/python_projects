# Credit: http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python
def send_email():
            import smtplib, getpass, sys

            gmail_user = "vinod.halaharvi@gmail.com"
            #gmail_pwd = getpass.getpass()
            gmail_pwd = 'bkabovsodltmldpb'
            FROM = 'vinod.halaharvi@gmail.com'
            TO = ['vinod.halaharvi@gmail.com'] #must be a list
            SUBJECT = "Testing sending using gmail"
            #TEXT = "Testing sending mail using gmail servers"
            TEXT = sys.stdin.read()

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER) 
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print 'successfully sent the mail'
            except:
                        raise
                        print "failed to send mail"

send_email()
