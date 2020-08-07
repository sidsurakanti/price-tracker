#importing
import requests
from bs4 import BeautifulSoup as soup
import smtplib

#url for the product that I want to track the price for and my user agent string
url = """https://www.amazon.com/BenQ-proprietary-borderless-Brightness-GW2480/dp/B072XCZSSW/ref=sr_1_8?dchild=1&keywords=monitor&qid=1596831655&s=electronics&sr=1-8&th=1"""
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

#gets and parses the contents of the page
page = requests.get(url, headers=header)
contents = soup(page.content, 'lxml') #parses the html of the page


#function that sends the mail
def send_email():
    email = "YOUR EMAIL"

    #server connection
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls() #encrypt connection
    server.ehlo()

    #login to gmail
    server.login(email, "YOUR PASSWORD")

    #email
    subject = 'SUBJECT'
    body = f"Link to product: {url}"

    #sends email
    server.sendmail(email, email, f"Subject: {subject}\n\n{body}")
    server.quit() #closes the connection with the server

#function that gets product name, and price
def price_checker():
    title = contents.find(id="productTitle").get_text() #gets title as a string object
    price = contents.find(id="priceblock_ourprice").get_text() #gets price as a string object
    int_price = int(price[1:4])  #converts price into a integer
    
    #checks if (int_price) meets the threshold. if yes send an email
    if (int_price < 100):
        send_email()
        print('Email has been sent!')

print(price_checker()) #runs the function


    