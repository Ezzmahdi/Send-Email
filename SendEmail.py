import ssl
import smtplib


email_sender = 'mahdi.a.ezz@gmail.com'
email_password = 'bofb uraj suqy coar'
email_receiver = 'penen77412@fesgrid.com'

message = "Subject: Don't forget to subscribe\n\nDon't forget to hit subscribe."

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, message)