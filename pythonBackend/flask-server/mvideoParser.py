import requests
import json
import io

def get_mvideoData(url, id):
    #Данные о товаре
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; _ym_d=1674809069; _ym_uid=1674809069855103262; _ga=GA1.3.168813493.1674809069; _gid=GA1.3.859910314.1674809069; _gid=GA1.2.859910314.1674809069; sub_id1_c=94563; sub_id2_c=551df83ec6c0471245780673ad926cdd480b3d90; partnerSrc=advcake; advcake_click_id=551df83ec6c0471245780673ad926cdd480b3d90; advcake_utm_partner=94563; advcake_utm_webmaster=gdeslon; __cpatrack=advcake_cpa; __allsource=advcake; __sourceid=advcake; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D94563%26advcake_params%3D551df83ec6c0471245780673ad926cdd480b3d90%26sub_id1%3D94563%26sub_id2%3D551df83ec6c0471245780673ad926cdd480b3d90; advcake_track_id=83f4f8df-e94c-617c-ec05-5ff4c07a1066; advcake_session_id=ce93c9d5-49b4-0156-555c-23c5a0ae477b; _ym_isad=2; __lhash_=7a64b64ec33193cf9297ded8e1862904; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2030; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6600000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=5; MVID_REGION_SHOP=S953; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=http%3A%2F%2F127.0.0.1%3A3000%2F__referral; admitad_deduplication_cookie=other_referral; tmr_lvid=858c52c0a674708866e67a691b221eb6; tmr_lvidTS=1674809203407; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=27c61231-ae9e-4f89-953b-9c1d7e3c474e; cookie_ip_add=37.145.34.140; uxs_uid=202ba760-9e1f-11ed-8da4-b73a07882ba4; afUserId=d9dc168b-498a-4ed1-b47b-27dfaf7f474b-p; AF_SYNC=1674809203932; flocktory-uuid=1135415e-35da-4baa-8e78-593eb0286175-7; flacktory=no; BIGipServeratg-pilot-pool=924822026.20480.0000; bIPs=-966280329; tmr_detect=0%7C1674827626102; mindboxDeviceUUID=00625d15-8eb8-4b1c-be89-5cee98b945ad; directCrm-session=%7B%22deviceGuid%22%3A%2200625d15-8eb8-4b1c-be89-5cee98b945ad%22%7D; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _ga=GA1.1.168813493.1674809069; _sp_id.d61c=0bc47c4d-9cfb-496d-9588-0a2524b93890.1674809069.8.1674846501.1674829168.93e4edd2-a8e5-417c-a546-1f3a22e657ac.4bc8d5e3-30cd-493b-85bf-bb108a3c82a9.83a50dd8-57e1-41cf-976e-fd66afb67f08.1674846499195.6; MVID_ENVCLOUD=prod1; _ga_CFMZTSS5FM=GS1.1.1674846495.3.1.1674846501.0.0.0; _ga_BNX5WPP3YK=GS1.1.1674846495.3.1.1674846501.54.0.0',
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
    'cookie': 'BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; _ym_d=1674809069; _ym_uid=1674809069855103262; _ga=GA1.3.168813493.1674809069; _gid=GA1.3.859910314.1674809069; _gid=GA1.2.859910314.1674809069; sub_id1_c=94563; sub_id2_c=551df83ec6c0471245780673ad926cdd480b3d90; partnerSrc=advcake; advcake_click_id=551df83ec6c0471245780673ad926cdd480b3d90; advcake_utm_partner=94563; advcake_utm_webmaster=gdeslon; __cpatrack=advcake_cpa; __allsource=advcake; __sourceid=advcake; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_content%3Dgdeslon%26utm_medium%3Dcpa%26utm_source%3Dadvcake%26utm_campaign%3D94563%26advcake_params%3D551df83ec6c0471245780673ad926cdd480b3d90%26sub_id1%3D94563%26sub_id2%3D551df83ec6c0471245780673ad926cdd480b3d90; advcake_track_id=83f4f8df-e94c-617c-ec05-5ff4c07a1066; advcake_session_id=ce93c9d5-49b4-0156-555c-23c5a0ae477b; _ym_isad=2; __lhash_=7a64b64ec33193cf9297ded8e1862904; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2030; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6600000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=5; MVID_REGION_SHOP=S953; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=http%3A%2F%2F127.0.0.1%3A3000%2F__referral; admitad_deduplication_cookie=other_referral; tmr_lvid=858c52c0a674708866e67a691b221eb6; tmr_lvidTS=1674809203407; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=27c61231-ae9e-4f89-953b-9c1d7e3c474e; cookie_ip_add=37.145.34.140; uxs_uid=202ba760-9e1f-11ed-8da4-b73a07882ba4; afUserId=d9dc168b-498a-4ed1-b47b-27dfaf7f474b-p; AF_SYNC=1674809203932; flocktory-uuid=1135415e-35da-4baa-8e78-593eb0286175-7; flacktory=no; BIGipServeratg-pilot-pool=924822026.20480.0000; bIPs=-966280329; tmr_detect=0%7C1674827626102; mindboxDeviceUUID=00625d15-8eb8-4b1c-be89-5cee98b945ad; directCrm-session=%7B%22deviceGuid%22%3A%2200625d15-8eb8-4b1c-be89-5cee98b945ad%22%7D; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _ga=GA1.1.168813493.1674809069; _sp_id.d61c=0bc47c4d-9cfb-496d-9588-0a2524b93890.1674809069.8.1674846501.1674829168.93e4edd2-a8e5-417c-a546-1f3a22e657ac.4bc8d5e3-30cd-493b-85bf-bb108a3c82a9.83a50dd8-57e1-41cf-976e-fd66afb67f08.1674846499195.6; MVID_ENVCLOUD=prod1; _ga_CFMZTSS5FM=GS1.1.1674846495.3.1.1674846501.0.0.0; _ga_BNX5WPP3YK=GS1.1.1674846495.3.1.1674846501.54.0.0',
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