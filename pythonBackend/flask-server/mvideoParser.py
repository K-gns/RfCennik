import requests
import json
import io

def get_mvideoData(url, id):
    #Данные о товаре
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; _ym_d=1674809069; _ym_uid=1674809069855103262; _ga=GA1.3.168813493.1674809069; _gid=GA1.3.859910314.1674809069; _gid=GA1.2.859910314.1674809069; sub_id1_c=94563; sub_id2_c=551df83ec6c0471245780673ad926cdd480b3d90; partnerSrc=advcake; advcake_session_id=ce93c9d5-49b4-0156-555c-23c5a0ae477b; __lhash_=7a64b64ec33193cf9297ded8e1862904; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2030; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6600000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=5; MVID_REGION_SHOP=S953; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_lvid=858c52c0a674708866e67a691b221eb6; tmr_lvidTS=1674809203407; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=27c61231-ae9e-4f89-953b-9c1d7e3c474e; cookie_ip_add=37.145.34.140; uxs_uid=202ba760-9e1f-11ed-8da4-b73a07882ba4; afUserId=d9dc168b-498a-4ed1-b47b-27dfaf7f474b-p; AF_SYNC=1674809203932; flocktory-uuid=1135415e-35da-4baa-8e78-593eb0286175-7; flacktory=no; BIGipServeratg-pilot-pool=924822026.20480.0000; bIPs=-966280329; SMSError=; authError=; partnerSrc=yandex; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; advcake_click_id=; admitad_uid=%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%20xiaomi%2012t%20256gb%20black; utm_term=%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%20xiaomi%2012t%20256gb%20black; advcake_track_id=3268639e-c93f-2354-71a1-5e4356d48d59; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Fsmartfon-xiaomi-12t-256gb-black-30065233%3Futm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_model_api_price-action_p_all-rf_17-01-2023_23_04_35%7Ccid%3A82282635%26utm_term%3D%25D1%2581%25D0%25BC%25D0%25B0%25D1%2580%25D1%2582%25D1%2584%25D0%25BE%25D0%25BD%2520xiaomi%252012t%2520256gb%2520black%26utm_content%3Dph%3A42922505979%7Cre%3A42922505979%7Ccid%3A82282635%7Cgid%3A5115784503%7Caid%3A13346565628%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A54%7C%25D0%2595%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%26etext%3D2202.wPBYq7BFZzzFmcfEWH_wOkkkab0OWuk1nVVVB4kbTI7W5I09_1135ue1mBsdHkGiaGZkdGh6Y3Vnc2htbHprZQ.1c05ec74c9250722037707bdd3de17cc78a241a8%26yclid%3D179606463359541803; advcake_utm_partner=cn%3Amg_model_api_price-action_p_all-rf_17-01-2023_23_04_35%7Ccid%3A82282635; advcake_utm_webmaster=ph%3A42922505979%7Cre%3A42922505979%7Ccid%3A82282635%7Cgid%3A5115784503%7Caid%3A13346565628%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A54%7C%25D0%2595%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3; admitad_deduplication_cookie=other_referral; __SourceTracker=http%3A%2F%2F127.0.0.1%3A3000%2F__referral; mindboxDeviceUUID=00625d15-8eb8-4b1c-be89-5cee98b945ad; directCrm-session=%7B%22deviceGuid%22%3A%2200625d15-8eb8-4b1c-be89-5cee98b945ad%22%7D; _sp_ses.d61c=*; _dc_gtm_UA-1873769-1=1; _ym_isad=2; _ga=GA1.2.168813493.1674809069; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=0bc47c4d-9cfb-496d-9588-0a2524b93890.1674809069.11.1674882217.1674862335.ad0f3a8e-8714-43a0-84d4-57bcfb437711.4579ecf6-a1e7-40f8-941a-517636e4cb90.e5c90e40-b166-4e82-8b9a-1fc2ad10b52e.1674882213764.6; tmr_detect=0%7C1674882221189; MVID_ENVCLOUD=prod2; _ga_BNX5WPP3YK=GS1.1.1674882214.6.0.1674882225.49.0.0; _ga_CFMZTSS5FM=GS1.1.1674882214.6.0.1674882225.0.0.0',
        'referer': url,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }



    params = {
        'productId': id,
    }
    

    response = requests.get('https://www.mvideo.ru/bff/product-details', params=params, headers=headers)
    return response.json()


 #цена товара
def get_mvideoPrice(url, id):   
    headers2 = {
    'authority': 'www.mvideo.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; _ym_d=1674809069; _ym_uid=1674809069855103262; _ga=GA1.3.168813493.1674809069; _gid=GA1.3.859910314.1674809069; _gid=GA1.2.859910314.1674809069; sub_id1_c=94563; sub_id2_c=551df83ec6c0471245780673ad926cdd480b3d90; partnerSrc=advcake; advcake_session_id=ce93c9d5-49b4-0156-555c-23c5a0ae477b; __lhash_=7a64b64ec33193cf9297ded8e1862904; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2030; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6600000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=5; MVID_REGION_SHOP=S953; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_lvid=858c52c0a674708866e67a691b221eb6; tmr_lvidTS=1674809203407; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=27c61231-ae9e-4f89-953b-9c1d7e3c474e; cookie_ip_add=37.145.34.140; uxs_uid=202ba760-9e1f-11ed-8da4-b73a07882ba4; afUserId=d9dc168b-498a-4ed1-b47b-27dfaf7f474b-p; AF_SYNC=1674809203932; flocktory-uuid=1135415e-35da-4baa-8e78-593eb0286175-7; flacktory=no; BIGipServeratg-pilot-pool=924822026.20480.0000; bIPs=-966280329; SMSError=; authError=; partnerSrc=yandex; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; advcake_click_id=; admitad_uid=%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%20xiaomi%2012t%20256gb%20black; utm_term=%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%20xiaomi%2012t%20256gb%20black; advcake_track_id=3268639e-c93f-2354-71a1-5e4356d48d59; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Fsmartfon-xiaomi-12t-256gb-black-30065233%3Futm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_model_api_price-action_p_all-rf_17-01-2023_23_04_35%7Ccid%3A82282635%26utm_term%3D%25D1%2581%25D0%25BC%25D0%25B0%25D1%2580%25D1%2582%25D1%2584%25D0%25BE%25D0%25BD%2520xiaomi%252012t%2520256gb%2520black%26utm_content%3Dph%3A42922505979%7Cre%3A42922505979%7Ccid%3A82282635%7Cgid%3A5115784503%7Caid%3A13346565628%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A54%7C%25D0%2595%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%26etext%3D2202.wPBYq7BFZzzFmcfEWH_wOkkkab0OWuk1nVVVB4kbTI7W5I09_1135ue1mBsdHkGiaGZkdGh6Y3Vnc2htbHprZQ.1c05ec74c9250722037707bdd3de17cc78a241a8%26yclid%3D179606463359541803; advcake_utm_partner=cn%3Amg_model_api_price-action_p_all-rf_17-01-2023_23_04_35%7Ccid%3A82282635; advcake_utm_webmaster=ph%3A42922505979%7Cre%3A42922505979%7Ccid%3A82282635%7Cgid%3A5115784503%7Caid%3A13346565628%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A54%7C%25D0%2595%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3; admitad_deduplication_cookie=other_referral; __SourceTracker=http%3A%2F%2F127.0.0.1%3A3000%2F__referral; mindboxDeviceUUID=00625d15-8eb8-4b1c-be89-5cee98b945ad; directCrm-session=%7B%22deviceGuid%22%3A%2200625d15-8eb8-4b1c-be89-5cee98b945ad%22%7D; _sp_ses.d61c=*; _dc_gtm_UA-1873769-1=1; _ym_isad=2; _ga=GA1.2.168813493.1674809069; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=0bc47c4d-9cfb-496d-9588-0a2524b93890.1674809069.11.1674882217.1674862335.ad0f3a8e-8714-43a0-84d4-57bcfb437711.4579ecf6-a1e7-40f8-941a-517636e4cb90.e5c90e40-b166-4e82-8b9a-1fc2ad10b52e.1674882213764.6; tmr_detect=0%7C1674882221189; MVID_ENVCLOUD=prod2; _ga_BNX5WPP3YK=GS1.1.1674882214.6.0.1674882225.49.0.0; _ga_CFMZTSS5FM=GS1.1.1674882214.6.0.1674882225.0.0.0',
    'referer': url,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params2 = {
        'productIds': id,
        'isPromoApplied': 'false',
        'addBonusRubles': 'false',
    }

    response2 = requests.get('https://www.mvideo.ru/bff/products/prices',
     params=params2, headers=headers2)
    return response2.json()