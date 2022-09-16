import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        random_quotes = random.choice(quotes)

    my_email = "sachita.nand@yahoo.com"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="ftxldmwlfacozfdf")
        connection.sendmail(from_addr=my_email, to_addrs="sachita.nand.6202@gmail.com",
                            msg=f"Subject:Motivational Quotas\n\n{random_quotes}")
