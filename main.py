import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com:465')

server.ehlo()


with open('password.txt', 'r') as f:
    password = f.read()

server.login("flashc0de404@gmail.com", "***************")

msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'signaturesignat@gmail.com'
msg['Subject'] = 'Just a Text'

with open ('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'img.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Context-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('flashc0de404@gmail.com', 'signaturesignat@gmail.com', text)

