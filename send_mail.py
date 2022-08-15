import smtplib, ssl

def send_mail(receiver, msg):

    sender_email = ""
    password = ""
    port = 465

    # Create a secure SSL context
    sslcontext = ssl.create_default_context()

    connection = smtplib.SMTP_SSL("smtp.gmail.com", port, context=sslcontext)

    connection.login(sender_email, password)

    connection.sendmail(sender_email, receiver, msg)
