# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime

# import smtplib


URL = 'https://www.amazon.in/Veirdo-Oversized-Printed-t-Shirt-XX-Large/dp/B09P65DPKZ/ref=sr_1_4?pf_rd_i=11400137031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=0d3288f2-b644-494e-ad90-2c53ee8f7255%2Cc80bcc3a-9e3e-4b50-a7b1-ec9aa8ee6395&pf_rd_r=G1CM120JBRZB0Y0KN6RR%2CH02BNAY4XCKZ1WAMW56A&pf_rd_s=merchandised-search-6&pf_rd_t=30901&qid=1685603190&refinements=p_85%3A10440599031%2Cp_n_feature_nineteen_browse-bin%3A11301357031%7C14852585031%7C27064186031%2Cp_72%3A1318476031&rnid=1318475031&rps=1&s=apparel&sr=1-4'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()
print(title)

price = soup2.find_all("span")
for i in price:
    try:
        if i['class'] == ['a-price-whole']:
            price = f"${str(i.get_text()[:-1])}"
            break
    except KeyError:
        continue

print(price)



price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


import datetime

today = datetime.date.today()

print(today)


# Create CSV and write headers and data into the file


import csv
header = ['Title', 'Price', 'Date']
data = [title, price, today]
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

import pandas as pd

df = pd.read_csv(r"C:\\Users\\DELL\\Desktop\\AmazonWebScraperDataset.csv")

print(df)

# Appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.in/Veirdo-Oversized-Printed-t-Shirt-XX-Large/dp/B09P65DPKZ/ref=sr_1_4?pf_rd_i=11400137031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=0d3288f2-b644-494e-ad90-2c53ee8f7255%2Cc80bcc3a-9e3e-4b50-a7b1-ec9aa8ee6395&pf_rd_r=G1CM120JBRZB0Y0KN6RR%2CH02BNAY4XCKZ1WAMW56A&pf_rd_s=merchandised-search-6&pf_rd_t=30901&qid=1685603190&refinements=p_85%3A10440599031%2Cp_n_feature_nineteen_browse-bin%3A11301357031%7C14852585031%7C27064186031%2Cp_72%3A1318476031&rnid=1318475031&rps=1&s=apparel&sr=1-4'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find_all("span")
    for i in price:
        try:
            if i['class'] == ['a-price-whole']:
                price = f"${str(i.get_text()[:-1])}"
                break
        except KeyError:
            continue



    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()

    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    """
    if (price<300):
        send_mail()
    """

# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)

import pandas as pd

df = pd.read_csv(r"C:\\Users\\DELL\\Desktop\\AmazonWebScraperDataset.csv")

print(df)



# sending yourself an email (just for fun) when a price hits below a certain level

"""
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    # server.starttls()
    server.ehlo()
    server.login('nivedhamv983@gmail.com', 'XXXXXXXXX' )

    subject = "The Shirt you want is below 300! Now is your chance to buy!"
    body = "This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.in/Veirdo-Oversized-Printed-t-Shirt-XX-Large/dp/B09P65DPKZ/ref=sr_1_4?pf_rd_i=11400137031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=0d3288f2-b644-494e-ad90-2c53ee8f7255%2Cc80bcc3a-9e3e-4b50-a7b1-ec9aa8ee6395&pf_rd_r=G1CM120JBRZB0Y0KN6RR%2CH02BNAY4XCKZ1WAMW56A&pf_rd_s=merchandised-search-6&pf_rd_t=30901&qid=1685603190&refinements=p_85%3A10440599031%2Cp_n_feature_nineteen_browse-bin%3A11301357031%7C14852585031%7C27064186031%2Cp_72%3A1318476031&rnid=1318475031&rps=1&s=apparel&sr=1-4 "

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nivedhamv983@gmail.com.com',
        msg

    )
"""