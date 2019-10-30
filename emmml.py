import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email(email, content):
    port = 465  # For SSL
# Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("thisisada69@gmail.com", "Coulson1")
        server.sendmail("thisisada69@gmail.com", email, content.as_string())
        server.close()

list = open('shoppingList.txt').readlines()
print(list)
items = ["\n    <li>{}</li>".format(s) for s in list]
items = "".join(items)

list1 = '''\
<html>
<head>
</head>
<ul style="font-family: trebuchet;">
<h2>Hi! Here's the shopping list:</h2>
<ul style="border: 1px solid black"; padding: 10px;>
{}
</ul>
</body>
</html>
'''.format(items)

list1 = MIMEText(list1, 'html')
email(email='thdnkns@gmail.com', content=list1)

