import os
def send_mail(name, email, query):
    import smtplib
    from email.mime.text import MIMEText as text

    gmail_user = "thelinutix@gmail.com" # set environment variable as your email id
    gmail_password = "eipi+1=0" # set environment variable as corresponding password
    sent_from = email
    to = ['', gmail_user]
    subject = 'Query Submission - ' + name 

    text_message = """
    From: %s
    Query: \n\t%s
    """ % (sent_from, query)

    email_text = text(text_message)

    email_text['From'] = sent_from
    email_text['To'] = ", ".join(to)
    email_text['Subject'] = subject
    

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, email_text.as_string())
        server.close()
        return True
    except:
        return False

