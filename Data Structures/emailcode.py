import smtplib

gmail_user = 'sivanand.vrf52@gmail.com'
gmail_password = 'tensor2378'

sent_from = gmail_user
to = ['anandsista@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what up? '

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
