from flask import Flask
import flask

import requests
import urllib
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

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/search/<string:text>")
def search(text):
    #Добыча ссылок на товар с помощью поисковой системы
    mvideoLinks = scrape_google("site:mvideo.ru/products " + text )
    # eldoradoLinks = scrape_google("site:https://www.eldorado.ru/cat/detail/ " + text )
    # dnsLinks = scrape_google("site:https://www.dns-shop.ru/product/ " + text )
    # citilinkLinks = scrape_google("site:https://www.citilink.ru/product/ " + text )
    # # return(mvideoLinks)
    # return(mvideoLinks + eldoradoLinks + dnsLinks + citilinkLinks)

    # allLinks = []
    # allLinks.append(mvideoLinks[0])
    # allLinks.append(eldoradoLinks[0])
    # allLinks.append(dnsLinks[0])
    # allLinks.append(citilinkLinks[0])
    # return(allLinks)

    #парсинг
    
    #mvideoLink = "https://www.mvideo.ru/products/smartfon-xiaomi-redmi-10-4-64gb-sea-blue-30059026"
    #mvideoLink = "https://www.mvideo.ru/products/nabor-podpisok-i-servisov-yandeks-plus-multi-na-3-mesyaca-6013781"
    #mvideoLink = "https://www.mvideo.ru/products/smartfon-xiaomi-redmi-6-32gb-black-30040792"
    #mvideoLink = "https://www.mvideo.ru/products/stiralnaya-mashina-bosch-waj2018sme-20084388"
    
    mvideoLink = mvideoLinks[0]

    print(mvideoLink)
    
    
    eldoradoLink = "https://www.eldorado.ru/cat/detail/smartfon-xiaomi-redmi-10-2022-64gb-sea-blue/"

    mvideoId = max(re.findall(r'\d+', mvideoLink), key=len) #Айди товара в мвидео

    #Данные о товаре
    mvideoData=get_mvideoData(mvideoLink, mvideoId) 
    

    #Есть ли в наличии, True - распродано, False - в наличии 
    mvideoName = (mvideoData["body"]["name"]) #Название
    mvideoIsSoldOut = (mvideoData["body"]["status"]["soldOut"]) #Наличие товара
    mvideoDescription = (mvideoData["body"]["description"]) #Описание товара
    
    print(mvideoName)

    #return mvideoData
    
    #Данные о цене товара
    mvideoPriceData=get_mvideoPrice(mvideoLink, mvideoId)
    #return mvideoPriceData

    mvideoSalePrice=(mvideoPriceData["body"]["materialPrices"][0]["price"]["salePrice"])
    mvideoBasePrice=(mvideoPriceData["body"]["materialPrices"][0]["price"]["basePrice"])
    mvideoPromoPrice=(mvideoPriceData["body"]["materialPrices"][0]["price"]["basePromoPrice"])
    

    mvideoPrice = 0 if (mvideoSalePrice is None) else mvideoSalePrice #Цена товара
    print(mvideoPrice)

    #return(mvideoPriceData)

    #Загрузка картинки в первую очередь   
    myFile = {'files':('testImage.png', open('testImage.png', 'rb'), 'images/png')}
    res1 = requests.post('http://localhost:1337/api/upload', files=myFile) 
    rJson=res1.json()
    pictureID=rJson[0]["id"] #ID картинки в Strapi (указывать в тег image, добавляет предмету картинку)
    #print(pictureID)

    #Добавление Item
    res2 = requests.post('http://localhost:1337/api/items', json={ "data": {"name":mvideoName, "price":mvideoPrice, "category":"Смартфоны", "shortDescription":mvideoDescription, "longDescription":mvideoDescription, "image":pictureID}})
    
    idOfItem = res2.json()["data"]["id"]
    #print(idOfItem)

    #Добавляем цены
    res3 = requests.post('http://localhost:1337/api/item-shop-prices', json={ "data": {"itemID":str(idOfItem), "mvideoPrice":mvideoPrice, "mvideoLink":mvideoLink, "eldoradoPrice":mvideoPrice, "eldoradoLink":mvideoLink, "dnsPrice":0, "dnsLink":"", "citilinkPrice":0, "citilinkLink":"", }})
    #print(res3.json())
    

    response = flask.jsonify(res2.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

    #Добавить itemMinPrice? Чисто за актуальную дату накидывать
    



@app.route("/test/<string:text>")
def text(text):
    #res3 = requests.post('http://localhost:1337/api/item-shop-prices', 
    # json={ "data": {"itemID":"0", 
    # "mvideoPrice":0, "mvideoLink":"", 
    # "eldoradoPrice":0, "eldoradoLink":"", 
    # "dnsPrice":0, "dnsLink":"", 
    # "citilinkPrice":0, "citilinkLink":"", }})
    #print(res3.json())
    return("test")

if __name__ == "__main__":
    app.run(debug=True)


