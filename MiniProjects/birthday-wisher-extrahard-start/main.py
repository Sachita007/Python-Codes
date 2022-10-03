

import pandas as pd
import smtplib
import datetime as dt
import random
import os

MY_EMAIL ="sachita.nand@yahoo.com"
MY_PASSWORD ="ftxldmwlfacozfdf"


current_date = dt.datetime.now()
today_tuple = (current_date.month, current_date.day)

data = pd.read_csv("birthdays.csv")
birthday_data = {(row["month"], row["day"]): row  for (index, row) in data.iterrows()}


# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthday_data:

    # 3. If step 2 is true, pick a random letter from letter templates
    # and replace the [NAME] with the person's actual name from birthdays.csv

    random_num= random.randint(1,3)
    with open(f"./letter_templates/letter_{random_num}.txt") as file:
        letter = file.read()
        updated_letter = letter.replace("[NAME]", birthday_data[today_tuple]["name"])
        person_email = birthday_data[today_tuple]["email"]



    # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person_email, msg=f"Subject: Birthday Wish\n\n{updated_letter}")
