import pandas as pd
import requests
from bs4 import BeautifulSoup

# creating list for scraping fields
Names = []
Prices = []
Description = []
Reviews = []

for i in range(2, 17):
    url = "https://www.flipkart.com/search?q=mobiles+under+15000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_13_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+15000%7CMobiles&requestId=8336782d-2d53-42de-b2e6-e67dc296fcd1&as-searchtext=mobiles+under&page="+str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    # print(soup)
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")  # creating a box to find only the item inside box

    # finding names of product
    # now we will find inside box only
    ProductNames = box.find_all("div", class_="_4rR01T")
    # print(Names)

    # filtering name of each product from Names
    for i in ProductNames:
        name = i.text
        Names.append(name)

    # print(Names)
    # print(len(Names))
    # print(len(Product_name))

    # find price
    productPrice = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in productPrice:
        name = i.text
        Prices.append(name)

    # print(Prices)
    # print(len(Prices))

    desc = box.find_all("ul", class_="_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)

    # print(Description)
    # print(len(Description))

    reviews = box.find_all("div", class_="_3LWZlK")

    for i in reviews:
        name = i.text
        Reviews.append(name)

# creating dataframe using pandas
df = pd.DataFrame({"product Name": Names, "Prices": Prices, "Description": Description, "Reviews": Reviews})
#print(df)

df.to_csv("D:/websraping/flipkart_mobiles_under_5000_5.csv")
