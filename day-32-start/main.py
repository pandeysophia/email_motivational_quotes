import smtplib
import datetime as dt
import random
PORT = 587
my_email = "avanepali@gmail.com"
password = "Anepali1!"

now = dt.datetime.now()
day = now.weekday()
if day == 3:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivational Quotes\n\n {quote}".encode("utf-8"))



