import requests
from bs4 import BeautifulSoup

def get_eldoradoPrice(url):


    headers = {
        'authority': 'www.eldorado.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'dt=1; PHPSESSID=7tqj0kjhgiakd5tjtfk11mce9b; ek_ab_test=B; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; ABT_test=B; _slid=63cfc1fd7f044e00eb063725; flocktory-uuid=680316f6-734a-4333-bb8f-ad97fc4d21a2-5; _gcl_au=1.1.132488179.1674560018; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=27c61231-ae9e-4f89-953b-9c1d7e3c474e; _ym_uid=1674560018522754848; _ym_d=1674560018; advcake_session_id=72bfa584-0883-b4c3-a913-962380ef2792; advcake_click_id=; adrcid=AMSwog0y-Bw5gzU2IXb8SbQ; _userGUID=0:lda5ssp2:2bWwsbLHPQ0nwZfmZiW2RCSTRASdP6N5; uxs_uid=f2e345b0-9bda-11ed-bef8-83a5c16e8abf; iRegionSectionId=11297; grs=15632; _slid_server=63cfc1fd7f044e00eb063725; USER_AUTH_GTM=0; bCNT=0%3A0; mindboxDeviceUUID=00625d15-8eb8-4b1c-be89-5cee98b945ad; directCrm-session=%7B%22deviceGuid%22%3A%2200625d15-8eb8-4b1c-be89-5cee98b945ad%22%7D; BITRIX_SM_ELD_TZ_OFFSET=-300; rrpvid=737661284696074; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; rcuid=63cadf60f3258d66d2178d82; digi-SearchVisitor=10%3A8; unauthorizedId=pwzakxzh7zlgkd5tqbah3fnw1fg958yrf7r3acvse1bbdzy6ialiffsqzqfnzwc5dx801f4qk5qsxzemocnbn8yxufopzdgjoz50a9mjkwh75vkd21jum066eajq97xs6f9e1elpvux6s5vefp2fqcbgt5jdb4uzesnqu6w249d0fe0vg8xphlb2arbu27dqu316ly4p1dmpr7fewe3t2b6dofw4c7ybpwfv2egz5293408d0inlhixb0ol7bd7z; __js_p_=216,300,0,1,0; show_region_popup=0; _gid=GA1.2.2024001696.1674809048; tmr_lvid=9d140f2905b154dda54e15eddf7e831d; tmr_lvidTS=1674809047939; ab_user=1062223040100; ab_segment=10; BITRIX_SM_SALE_UID=31325043535; BITRIX_SM_SALE_UID_CS=3c81cbe72d32adb97197854abaf27c4f; utm_campaign=cn%3Amg_model_api_price-action_p_all-rf_18-01-2023_21_03_31%7Ccid%3A82313579; advcake_trackid=d5a9c3b3-8169-8359-650e-9da755424523; advcake_track_url=https%3A%2F%2Fwww.eldorado.ru%2Fcat%2Fdetail%2Fsmartfon-xiaomi-12t-256gb-black%2F%3Futm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_model_api_price-action_p_all-rf_18-01-2023_21_03_31%257Ccid%3A82313579%26utm_term%3D%25D1%2581%25D0%25BC%25D0%25B0%25D1%2580%25D1%2582%25D1%2584%25D0%25BE%25D0%25BD%2520xiaomi%252012t%2520256gb%2520black%26utm_content%3Dph%3A42937120238%257Cre%3A42937120238%257Ccid%3A82313579%257Cgid%3A5116379357%257Caid%3A13346184711%257Cadp%3Ano%257Cpos%3Apremium2%257Csrc%3Asearch_none%257Cdvc%3Adesktop%257Ccoef_goal%3A0%257Cregion%3A54%257C%25D0%2595%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%26etext%3D2202.wPBYq7BFZzzFmcfEWH_wOkkkab0OWuk1nVVVB4kbTI7W5I09_1135ue1mBsdHkGiaGZkdGh6Y3Vnc2htbHprZQ.1c05ec74c9250722037707bdd3de17cc78a241a8%26yclid%3D179606966360925192; advcake_utm_partner=cn%3Amg_model_api_price-action_p_all-rf_18-01-2023_21_03_31%257Ccid%3A82313579; advcake_utm_webmaster=ph%3A42937120238%257Cre%3A42937120238%257Ccid%3A82313579%257Cgid%3A5116379357%257Caid%3A13346184711%257Cadp%3Ano%257Cpos%3Apremium2%257Csrc%3Asearch_none%257Cdvc%3Adesktop%257Ccoef_goal%3A0%257Cregion%3A54%257C%25D0%2595%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3; __lhash_=86145d641a6584cd3f11c60ae3de43d9; last_source=127.0.0.1%3A3000; _slsession=98420F60-23E6-4F04-B1FB-61EB88EE5B7F; dSesn=88e67dcc-8935-bd5b-16da-12a6c8f64244; _dvs=0:ldfhml4u:2C6~ftOddRKRNfv1xz3SCEDBDq0rjJKG; _sp_ses.3135=*; _sp_id.3135=b9b76610-2a30-45cf-96cb-9322ef015767.1674560018.11.1674882217.1674862334.03d5d9fc-1a17-4a79-8757-e952808e4c43.1494f43d-cc3a-45ba-a6fe-c2cd20f5381f.c7054858-9cd2-460e-8bb0-c89be7cb85fc.1674882216553.3; _ga_4P3TZK55KZ=GS1.1.1674882216.12.0.1674882216.0.0.0; _ga=GA1.1.1324404813.1674560018; _ym_isad=2; _dc_gtm_UA-44012634-4=1; cfidsgib-w-eldorado=ONsH3KForUPz1/MUEOGTOTd46k6BWoI4Kj+qpIsSRYXZwuHgJlFUINnWQPYEKNHKzXpV1qagqNDeDX3PVvU79U7HtfeJvPtaLyPvGIsiB+eUezHo9Gwz59vocfvmN+OlxvsfVKLCqyf5K1xyHNz36m1kJQcYFD0///VP710=; gsscgib-w-eldorado=rUSg3FnABPtnQY9X+UbCl5R/iheYVw6jv99PSGN7lDm2uXyeB3XxJ53Fb/QxsQQdGll9VlVufn/cIB86IweCvrT6inE6fdj5YQn+EWWNvSnhxEU++jpYUuaDZBUhMKlTtmpOa+ipM5ge/jJcPE1EwzTWKSQhk4xj6RYSuEMsthW4KKUlP+2qSD1ksjaN6U+gqbirV3ECldHQK6QpsIO6Jb8ATW+TmwgCnueO5wk3TOeGAgDfDmx3Yi0KLL1+6Q==; gsscgib-w-eldorado=rUSg3FnABPtnQY9X+UbCl5R/iheYVw6jv99PSGN7lDm2uXyeB3XxJ53Fb/QxsQQdGll9VlVufn/cIB86IweCvrT6inE6fdj5YQn+EWWNvSnhxEU++jpYUuaDZBUhMKlTtmpOa+ipM5ge/jJcPE1EwzTWKSQhk4xj6RYSuEMsthW4KKUlP+2qSD1ksjaN6U+gqbirV3ECldHQK6QpsIO6Jb8ATW+TmwgCnueO5wk3TOeGAgDfDmx3Yi0KLL1+6Q==; tmr_detect=0%7C1674882226179; digi_uc=W1sidiIsIjcxNjU1MTI4IiwxNjc0ODYyMzM1OTMzXSxbInYiLCI3MTY0NDc4MiIsMTY3NDg2MjI5NTc0Ml0sWyJ2IiwiNzE2NTk1OTUiLDE2NzQ4ODIyNTQzNjFdLFsidiIsIjcxNjIzNjUwIiwxNjc0ODYxOTg3NjU1XSxbInYiLCI3MTYyMzY0OCIsMTY3NDg2MTU4NTEzOF0sWyJ2IiwiNzE2NTUxMjkiLDE2NzQ4NjE0MDEwMjhdLFsidiIsIjcxNjIzNjQ2IiwxNjc0ODYxMjM3NTI1XSxbInYiLCI3MTY0MTA2OCIsMTY3NDg2MTE3ODc4Nl0sWyJ2IiwiNzE2NDkxOTQiLDE2NzQ4NTkyNTgyMzFdLFsidiIsIjcxNjYzMDQxIiwxNjc0ODU4MDgxOTg3XV0=; cfidsgib-w-eldorado=ONsH3KForUPz1/MUEOGTOTd46k6BWoI4Kj+qpIsSRYXZwuHgJlFUINnWQPYEKNHKzXpV1qagqNDeDX3PVvU79U7HtfeJvPtaLyPvGIsiB+eUezHo9Gwz59vocfvmN+OlxvsfVKLCqyf5K1xyHNz36m1kJQcYFD0///VP710=; __zzatgib-w-eldorado=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2Uwfy5XXwobV3oWfjxZHlU5N1kSCAwgcHZ2LRs3V10cESRYDiE/C2lbVjRnFRtASBgvS255MD9tImZIWSVEXFR1F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NEhY=6pKCNA==; fgsscgib-w-eldorado=tMj059ded6ece6c5a1283ff52f29f9466e74752d; fgsscgib-w-eldorado=tMj059ded6ece6c5a1283ff52f29f9466e74752d',
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

    #print("Encoded method :", soup.original_encoding)

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
