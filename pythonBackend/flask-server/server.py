from flask import Flask
import flask

import requests
import urllib
import urllib.request
import os
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from flask import Response

import json
import io


import re 

from PIL import Image

from googleParser import scrape_google
from mvideoParser import get_mvideoData, get_mvideoPrice
from eldoradoParser import get_eldoradoPrice
from rbtParser import get_rbtData
from sberParser import get_sberData

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/search/<string:text>")
def search(text):
    #Добыча ссылок на товар с помощью поисковой системы
    mvideoLinks = scrape_google("site:mvideo.ru/products " + text )
    eldoradoLinks = scrape_google("site:https://www.eldorado.ru/cat/detail/ " + text)
    dnsLinks = scrape_google("site:https://www.dns-shop.ru/product/ " + text + " купить")
    citilinkLinks = scrape_google("site:https://www.citilink.ru/product/ " + text )
    # # return(mvideoLinks)
    # return(mvideoLinks + eldoradoLinks + dnsLinks + citilinkLinks)

    
    #парсинг
    
    #mvideoLink = "https://www.mvideo.ru/products/smartfon-xiaomi-redmi-4-prime-32gb-gray-30027791"

    try:
        mvideoLink = mvideoLinks[0]
        eldoradoLink = eldoradoLinks[0]
        dnsLink = dnsLinks[0]
        citilinkLink = citilinkLinks[0]
        print(mvideoLink)
        print(eldoradoLink) 
        print(dnsLink)
        print(citilinkLink) 
    except:
        print("Не сработал гугл парсер")

     
    

    #Данные о товаре в МВИДЕО
    mvideoId = max(re.findall(r'\d+', mvideoLink), key=len) #Айди товара в мвидео
    mvideoData=get_mvideoData(mvideoLink, mvideoId) 

    #Есть ли в наличии, True - распродано, False - в наличии 
    mvideoName = (mvideoData["body"]["name"]) #Название
    mvideoIsSoldOut = (mvideoData["body"]["status"]["soldOut"]) #Наличие товара
    mvideoDescription = (mvideoData["body"]["description"]) #Описание товара
    #print("Категория", mvideoData["body"]["category"]["name"]) 
    if (mvideoData["body"]["category"]["name"] == "Смартфоны"): #Присвоить категорию из существующих в данный момент
            mvideoCategory = "Смартфоны"
    elif mvideoData["body"]["category"]["name"] == "Ноутбуки":
            mvideoCategory = "Ноутбуки"
    else: mvideoCategory = "Бытовая техника"
    #mvideoCategory = "Смартфоны" if (mvideoData["body"]["category"]["name"]) ==  "Смартфоны" else "Бытовая техника"
    mvideoImageUrl = "http://static.mvideo.ru/" + (mvideoData["body"]["image"]) #Url к апи с картинкой
    urllib.request.urlretrieve(mvideoImageUrl, 'mvideoImg.jpg') #загрузка картинки

        
    #Данные о цене товара в МВИДЕО
    mvideoPriceData=get_mvideoPrice(mvideoLink, mvideoId)
    mvideoSalePrice=(mvideoPriceData["body"]["materialPrices"][0]["price"]["salePrice"])
    mvideoBasePrice=(mvideoPriceData["body"]["materialPrices"][0]["price"]["basePrice"])
    mvideoPromoPrice=(mvideoPriceData["body"]["materialPrices"][0]["price"]["basePromoPrice"])
    
    mvideoPrice = 0 if (mvideoSalePrice is None ) else mvideoSalePrice #Цена товара
    mvideoPrice = 1 if (mvideoIsSoldOut ) else mvideoSalePrice
    

    #Получение цены из эльдорадо!
    eldoradoPrice = get_eldoradoPrice(eldoradoLink)


    #Загрузка картинки в первую очередь   
    myFile = {'files':('mvideoImg.jpg', open('mvideoImg.jpg', 'rb'), 'images/img')}
    res1 = requests.post('http://localhost:1337/api/upload', files=myFile) 
    rJson=res1.json()
    pictureID=rJson[0]["id"] #ID картинки в Strapi (указывать в тег image, добавляет предмету картинку)
    #print(pictureID)

    #Добавление Item
    res2 = requests.post('http://localhost:1337/api/items', json={ "data": {"name":mvideoName, "price":mvideoPrice, "category":mvideoCategory, "shortDescription":mvideoDescription, "longDescription":mvideoDescription, "image":pictureID}})
    idOfItem = res2.json()["data"]["id"]

    #Добавляем цены!
    res3 = requests.post('http://localhost:1337/api/item-shop-prices', json={ "data": {"itemID":str(idOfItem), "mvideoPrice":mvideoPrice, "mvideoLink":mvideoLink, "eldoradoPrice": eldoradoPrice, "eldoradoLink":eldoradoLink, "dnsPrice":0, "dnsLink":dnsLink, "citilinkPrice":0, "citilinkLink":citilinkLink, }})
    

    #Тестово добавляем цены
    #res3 = requests.post('http://localhost:1337/api/item-shop-prices', json={ "data": {"itemID":str(idOfItem), "mvideoPrice":mvideoPrice, "mvideoLink":mvideoLink, "eldoradoPrice":0, "eldoradoLink":"", "dnsPrice":0, "dnsLink":"", "citilinkPrice":0, "citilinkLink":"", }})
    

    response = flask.jsonify(res2.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

    

@app.route("/testEldorado/<string:text>")
def eldorado(text):
    
    price = get_eldoradoPrice("https://www.eldorado.ru/cat/detail/smartfon-xiaomi-redmi-10c-4gb-64gb-blue/")
    print(price)
    #print("ДАННЫЕ", data)
    return("в разработке")


@app.route("/test/<string:text>")
def text(text):
        #urllib.request.urlretrieve('http://static.mvideo.ru/Pdb/30063081b.jpg', 'mvideoImg.jpg')
    return("test")

@app.route("/testRBT/<string:text>")
def rbt(text):
    
    data = get_rbtData()
    print("ДАННЫЕ", data)
    return("в разработке")

@app.route("/testSber/<string:text>")
def sber(text):
    data = get_sberData()
    print("ДАННЫЕ", data.json())
    return("в разработке")

if __name__ == "__main__":
    app.run(debug=True)




