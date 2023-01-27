import requests
import json
import io

#def get_rbtData(url, id):
def get_sberData():
    #Данные о товаре
    headers = {
    'authority': 'sbermegamarket.ru',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'cookie': 'spid=1674239833653_b5df08ce3226363dcd2a6fc0cd1e70bf_sjhoi6k0ix1hvj4e; analytics_session_id=a433f1df-bb72-4bdd-9618-6800c9716284; _ym_uid=1674239844768914060; _ym_d=1674239844; oxxfgh=1669989b-f2f5-4141-afd9-b4694ab7f9a8#1#7776000000#5000#1800000; KFP_DID=0219d1c4-1531-09e4-99f9-19295035b74b; ssaid=7bd1ca00-98f1-11ed-8e3f-95cf8129b87f; sbermegamarket_token=e53b0b17-85b7-4b73-9971-dac342a5d45b; adspire_uid=AS.914437571.1674239845; atm_marketing=%7B%22id%22%3A7501%2C%22mid%22%3A8881%2C%22aid%22%3A%22AS.914437571.1674239845%22%2C%22cookie_time%22%3A1674239845184%2C%22priority%22%3A0%7D; adtech_uid=1ca388bb-6e07-49f9-a511-70ed3b571daf%3Asbermegamarket.ru; top100_id=t1.6795753.988251555.1674239846392; rrpvid=280409189208710; _gcl_au=1.1.766358179.1674239849; rcuid=63cadf60f3258d66d2178d82; _sa=SA1.c5a4afa2-8847-4f93-8456-0b44df717700.1674239849; uxs_uid=7ea694e0-98f1-11ed-8790-f5f0c65e460b; adrcid=AMSwog0y-Bw5gzU2IXb8SbQ; __exponea_etc__=a1a83e07-937b-47ed-b09a-938248a513b0; tmr_lvid=eeadd858d2f526131d01e285a6bba110; tmr_lvidTS=1674239853076; flocktory-uuid=1efdcfb2-7a2c-4f0c-bb94-b62a80c6e509-4; isOldUser=true; spsc=1674809972684_fe614a2947a088d6882c82c02ee5dcb6_a5476469b72f558bb72e6aae99c6a060; _ym_visorc=b; __zzatw-smm-t=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UbN1ddHBEkWA4hPwsXXFU+NVQOPHVXLw0uOF4tbx5lTl0nRFVNeSUiFHpnFRtQSxgvS18+bX0yUCs5Lmw=S4JFQA==; _ym_isad=2; region_info=%7B%22displayName%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22kladrId%22%3A%225000000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A55.755814%2C%22lon%22%3A37.617635%7D%2C%22id%22%3A%2250%22%7D; _ga=GA1.2.1040302747.1674239846; _gid=GA1.2.1847519076.1674810002; last_visit=1674792002618%3A%3A1674810002618; __exponea_time2__=-25.64344573020935; _gpVisits={"isFirstVisitDomain":true,"todayD":"Fri%20Jan%2027%202023","idContainer":"10002472"}; tmr_detect=0%7C1674810012160; __tld__=null; _gp10002472={"hits":1,"vc":1,"ac":1}; _ga_W49D2LL5S1=GS1.1.1674810000.3.1.1674810064.56.0.0; _gat_UA-89387429-1=1; t3_sid_6795753=s1.1588661397.1674810002551.1674810065642.2.9; cfidsw-smm-t=QfIofAv10DDh6909m3qt2h9KhCH9j8VxUODM5UijvSlrthj1dyWRS1qUkAVrFu6bEZUuWj8tZt5eBdzsSRcMibVblwT/y8bwD3oxbwtmGRvggItP1edWcH6Z/nPsA95wbrJTV+pfN/mKcOz5n78DFXHa7bKsyddbMZVN5Zg=; cfidsw-smm-t=QfIofAv10DDh6909m3qt2h9KhCH9j8VxUODM5UijvSlrthj1dyWRS1qUkAVrFu6bEZUuWj8tZt5eBdzsSRcMibVblwT/y8bwD3oxbwtmGRvggItP1edWcH6Z/nPsA95wbrJTV+pfN/mKcOz5n78DFXHa7bKsyddbMZVN5Zg=',
    'origin': 'https://sbermegamarket.ru',
    'referer': 'https://sbermegamarket.ru/catalog/details/smartfon-xiaomi-redmi-10c-4-128gb-gray-38594-100031749181/',
    'sec-ch-ua': '"Chromium";v="108", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
    'addressId': '',
    'auth': {
        'locationId': '50',
        'appPlatform': 'WEB',
        'appVersion': 1674702256,
        'deviceId': 'a433f1df-bb72-4bdd-9618-6800c9716284',
        'analyticsDeviceId': 'a1a83e07-937b-47ed-b09a-938248a513b0',
        'experiments': {
            '1': '2',
            '8': '2',
            '15': '2',
            '21': '3',
            '30': '2',
            '38': '2',
            '40': '2',
            '43': '3',
            '46': '2',
            '53': '1',
            '55': '2',
            '58': '1',
            '60': '2',
            '66': '3',
            '68': '1',
            '69': '1',
            '71': '3',
            '77': '1',
            '78': '2',
            '82': '2',
            '83': '2',
            '94': '1',
            '5779': '2',
            '20121': '2',
            '43568': '2',
            '67062': '1',
            '67972': '2',
            '69032': '3',
            '70070': '2',
            '72674': '3',
            '75567': '3',
            '80283': '2',
            '81724': '2',
            '85160': '2',
            '86296': '2',
            '86323': '2',
            '86356': '2',
            '90172': '3',
            '91562': '1',
        },
        'os': 'UNKNOWN_OS',
    },
    }

    response = requests.post(
    'https://sbermegamarket.ru/api/mobile/v2/customerRecentlyViewedService/goods/list',
    headers=headers,
    json=json_data,
    )

    return response

