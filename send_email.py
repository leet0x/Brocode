import smtplib

sender = "krekuenida@gmail.com"
receiver = "likuhimself@gmail.com"
password = "36432,bibi@."
subject = "python script email test"
body = "i wrote an email! :D"

message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


try:
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, receiver, message)
    print("email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
