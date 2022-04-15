##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib, pandas, random, os

today = dt.datetime.now()

day = today.day
month = today.month


data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)
for x in data_dict:
    if x["month"] == month and x["day"] == day:
        template_name = random.choice(os.listdir("./letter_templates"))
        with open(f"./letter_templates/{template_name}") as letter:
            blank_letter=letter.read()
            print(blank_letter)
            quote=blank_letter.replace("[NAME]", x["name"])
            print(quote)

        my_email = "leathersho3@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:  # secures connection to email server
            connection.starttls()
            connection.login(user=my_email, password="pronto334!")  # login to email provider
            connection.sendmail(from_addr=my_email, to_addrs=f"{x['email']}",
                                msg=f"Subject:Happy Birthday {x['name']} \n\n {quote}")



