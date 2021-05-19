import smtplib as st
import datetime as dt
import random
with open("C:\\Users\\Dell\\Desktop\\worksta\\Python Practice\\Foldr\\Day32SMTP\\quotes.txt",mode="r") as qoutes:
    qt=qoutes.readlines()
mg=random.choice(qt)   
usName="yatin.18bcon268@jecrcu.edu.in"
passw="tonystarkironman"
with st.SMTP("smtp.jecrcu.edu.in",port=587) as obs:
    obs.starttls()
    obs.login(user= usName,password=passw)
    obs.sendmail(from_addr=usName,
    to_addrs=usName,
    msg=f"Subject:Qoute of the day\n\n{mg}")

