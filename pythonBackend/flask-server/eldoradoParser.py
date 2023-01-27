import requests
from bs4 import BeautifulSoup

def get_eldoradoPrice(url):


    headers = {
        'authority': 'www.eldorado.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'ab_user=5290022200100; ab_segment=52; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; _ym_d=1653080656; _ym_uid=1646916846182449716; rcuid=62794a315368be00013f140a; _userGUID=0:l3exjhin:aky0SL8A6iRIrNWK0IOpiZRG6mXsQQf9; clickcake_id=39156396-462f-5324-2e93-187b555ea4e4; flocktory-uuid=a7f416f4-8fec-4d63-bf11-ab16107794ab-8; USER_AUTH_GTM=0; BITRIX_SM_ELD_TZ_OFFSET=-300; unauthorizedId=kn9bw5clnw0rgbxxf7b7aqcywi91ulvge1dt4dpk84rd17op2zqvi49oes5dxb1vdy2zfq2l4bebym9n8ztyhwkibqpwq8zhwiln4lqnt7i45gl4qlsckzp5ald7ja6ue0v309tngxm98fnxxhdotx0ervqb2t81qjidsi4tlwf9mjeeoi5kl5hb1jm2qqbud717dg2cvpod0uutd2p9w2offxn64s5b6udpw4030f8ocjt94yzjzywr8ghtq3r3; tmr_lvidTS=1654251967484; tmr_lvid=68e609e5605b57a0376fc85a37e6bf94; iRegionSectionId=11297; __ttl__widget__ui=1654255879186-c16a4c460827; uxs_uid=fb40b2f0-e592-11ec-a863-af0c48082e98; clickcake_max=31; __utma=267034714.1731704728.1653080655.1655550022.1655759494.9; _ga=GA1.1.1325209849.1653080656; clickcake_total=35; clickcake_sid=8d1d2bc1-d41a-9f98-3c19-4efbe3ce0cad; clickcake_current=1; tmr_reqNum=196; _ga_4P3TZK55KZ=GS1.1.1656218574.11.0.1656218578.0; rrpvid=221429758278146; _dy_soct=1009413.1015421.1653080655.uref17rcbxio1wcqvurf0oxq7rv89z9b*1025826.1047956.1653080655.uref17rcbxio1wcqvurf0oxq7rv89z9b*1020255.1036211.1653080656.uref17rcbxio1wcqvurf0oxq7rv89z9b*1020255.1036208.1653141508.uref17rcbxio1wcqvurf0oxq7rv89z9b*1052902.1130398.1653141515.uref17rcbxio1wcqvurf0oxq7rv89z9b*1020255.1036212.1654255766.uref17rcbxio1wcqvurf0oxq7rv89z9b*1052902.1130394.1654256017.uref17rcbxio1wcqvurf0oxq7rv89z9b*1015626.1026717.1660069226*1025518.1047157.1660069226*1025792.1047912.1660069226*1026313.1049036.1660069226*1029321.1056990.1660069226*1039851.1089695.1660069226*1062106.1161327.1660069226*1066273.1175622.1660069226*1070188.1311680.1660069226*1070841.1192041.1660069226*1102865.1306744.1660069226*1110180.1328521.1660069226*1003181.1004426.1660069226*1068649.1184397.1660069226*1028959.1056222.1660069226*1025449.1090858.1660069229; ek_ab_test=B; _slid=63487f7d197be9d2a6051725; iGeneralRegionSectionId=15632; grs=15632; _slid_server=63487f7d197be9d2a6051725; digi-SearchVisitor=10%3A1; BITRIX_SM_SALE_UID=31276335317; BITRIX_SM_SALE_UID_CS=cde0a49a2e9a71572f2d8463a75dc43d; bCNT=0%3A0; dt=1; PHPSESSID=uinqg4mu74pq1hvcq49hn3j32b; ABT_test=A; show_region_popup=0; __cap_p_=1,0; __cap_=f2a52de6f014d14848bb66797a897c11; __hash_=e880611ff28f592b65cb4b8d83d6d499; dSesn=86b45270-8c49-1345-53e2-b46c776e806d; _dvs=0:ldewexcr:GX7yjFWn4QkOA4NIhPnYVERr4sJIciNj; gssc157=; __lhash_=4e96c204cbcbab407051a7dcfc8b6f12; cfidsgib-w-eldorado=ek3HGxFOInvcS25wklrXHCm3vlGFCnTEcqMnaIB6TQ6RkUoBGLY66Rs2NFHh6chB46XMdNhWRRQjNS5N8a9ho3Z++x1w55Z/oGwbhqNelqvvwiUFD+BLKTvBko5hAbSZWSTwwpiGdghaxBOhENyesBrJN0dgVUAXNwhM0A8=; gsscgib-w-eldorado=JnGNyYvvvxh+1PU/Cg/B9aWHuynhM87lJcPNLIcvCfQ8hefxhAYff5C0042FFcxKhz+t5EOBKY2/iJl4ZvGFvE4eBu5jyZJC+G6eRwb0K+mKhKkGWQXgzWG1oKo3563CkZ1cf7NthU94a/5l9+ni7rg8pdDxG3V2MsY8ilN0vGUkWtU60Ty5m1AhzbTFtwpDKJKx/q83yxWVQn0iMXl1dSZDQKI3T+mL+brbKs+LAHzSpBiVD+Is/yqA4rIkp9kMJx0=; gsscgib-w-eldorado=JnGNyYvvvxh+1PU/Cg/B9aWHuynhM87lJcPNLIcvCfQ8hefxhAYff5C0042FFcxKhz+t5EOBKY2/iJl4ZvGFvE4eBu5jyZJC+G6eRwb0K+mKhKkGWQXgzWG1oKo3563CkZ1cf7NthU94a/5l9+ni7rg8pdDxG3V2MsY8ilN0vGUkWtU60Ty5m1AhzbTFtwpDKJKx/q83yxWVQn0iMXl1dSZDQKI3T+mL+brbKs+LAHzSpBiVD+Is/yqA4rIkp9kMJx0=; cfidsgib-w-eldorado=ek3HGxFOInvcS25wklrXHCm3vlGFCnTEcqMnaIB6TQ6RkUoBGLY66Rs2NFHh6chB46XMdNhWRRQjNS5N8a9ho3Z++x1w55Z/oGwbhqNelqvvwiUFD+BLKTvBko5hAbSZWSTwwpiGdghaxBOhENyesBrJN0dgVUAXNwhM0A8=; __zzatgib-w-eldorado=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VudCteHkseZEpZFUImUVcyNCdYP0led0RvLRs3V10cESRYDiE/C2lbVjRnFRtASBgvS255MD9tIWVMYSVFW1Z1F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NEhY=UhPfpg==; fgsscgib-w-eldorado=6OMUfdc7964443dbf623126d05e6aba07f1539cd; fgsscgib-w-eldorado=6OMUfdc7964443dbf623126d05e6aba07f1539cd',
        'if-modified-since': 'Fri, 27 Jan 2023 00:01:00 GMT',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    req = requests.get(url, headers=headers)

    with open("eldoradoItem.html", "w") as file:
        file.write(req.text)

    with open("eldoradoItem.html") as file:
        src = file.read()    
       
    #soup = BeautifulSoup(req.text, "lxml")
    #soup =BeautifulSoup(req.text('utf-8','ignore'))
    soup = BeautifulSoup(req.content, "html.parser")

    print("Encoded method :", soup.original_encoding)

    #print(soup)
    try:
        priceTag = soup.find_all("div", {"class": "product-box-price__active"})
        #priceTag2 = soup.find_all('span',{"class":"discount-value"}) #<div class="product-box-price__active">10&nbsp;999&nbsp;�.</div>
        description = soup.find_all("div", {"class": "q-item-main-description"})[0].text
        print("ПРАЙСТЕГ", priceTag)
        print("описание:", description)
        priceDirty = priceTag[0].text
        priceNormal = ''.join(x for x in priceDirty if x.isdigit())
    except:
        description = ""
        priceNormal = "0"       
    
    print(priceNormal)
    return(priceNormal)
