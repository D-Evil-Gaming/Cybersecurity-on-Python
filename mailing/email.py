import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


ser=smtplib.SMTP("smtp.gmail.com",587)
ser.starttls()
ser.ehlo()

ser.login("degcyber@gmail.com","rklj wjay cdxi pdhp")

msg=MIMEMultipart()
msg['From']="Deg"
msg['To']='degcyber@gmail.com'
msg['Subject']='Test mail by deg'

with open("message.txt", "r") as d:
    m = d.read()


msg.attach(MIMEText(m,"plain"))

file='img.png'
with open(file,"rb") as atta:
    p=MIMEBase("application","octet-stream")
    p.set_payload(atta.read())

encoders.encode_base64(p)
p.add_header("content-disposition",f"attachment;filename={file}")
msg.attach(p)

text=msg.as_string()
ser.sendmail("degcyber@gmail.com","degcyber@gmail.com",text)
ser.quit()
