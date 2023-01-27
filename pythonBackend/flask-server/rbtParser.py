import requests
import json
import io

#def get_rbtData(url, id):
def get_rbtData():
    #Данные о товаре
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'region=3; PHPSESSID=o9kfjqlk0i8olp6ifpad9mv54f; rerf=AAAAAGPTjxi5kGesAw8TAg==; ipp_uid=1674809108874/FGxbSt2Y3modQNN9/mwOxSNOvoLp1oD8cYeeTqg==; ipp_key=v1674809108874/v33947245ba5adc7a72e273/UbTigSUTPR7rVdmrpufWPA==; _gcl_au=1.1.1745493284.1674809139; scaleo_source=false; _ym_uid=1674809139222952846; _ym_d=1674809139; rrpvid=980590774431008; _ga=GA1.2.935694320.1674809139; _gid=GA1.2.1211018646.1674809139; tmr_lvid=ff64b6adb41becf70066d03c52f19d69; tmr_lvidTS=1674809139480; _userGUID=0:ldea4aq9:gc3zjR7Xs4cxRRht7YfFxQP4mzhDfkf8; dSesn=5fa3d6a5-36b5-a74b-64d3-c021c1ef8871; _dvs=0:ldea4aq9:b~MOOy31Ajg1eswaMfNqxSWDm795GhP8; rcuid=63cadf60f3258d66d2178d82; rr-viewItemId=792117; rrviewed=792117; _ym_isad=2; flocktory-uuid=37dd770e-3683-4aa5-8057-477909ca5f82-2; rrlevt=1674809140013; rr_rcs=eF5j4cotK8lMETA0MTPQNdQ1ZClN9kgzNjc1N09J1k1OszTTNUlKMtA1MTKy0E0xMjM0T7a0MEpNMwMAk_oORw; _ga=GA1.3.935694320.1674809139; _gid=GA1.3.1211018646.1674809139; _ga_NPYSD1BMEH=GS1.1.1674809139.1.0.1674809140.0.0.0; adrdel=1; adrcid=AMSwog0y-Bw5gzU2IXb8SbQ; cto_bundle=l6HYcV85eTB3OU9JTCUyQmIzMUg4OTh2TWNNRm1Ya1FaR2NXaWR3b3BEYXBDSUslMkZmRDVKNTJzbkhaakNuQVlXeSUyQlNPJTJGVWp6QUU0UVVsdGMxR1VhaE1ib0FvZHhnTHIxUDdZclQ3WWdKQWF6RnREcWliT1B5ayUyQlBzYXdhSXlpTVNKdzJMc253OGJWNkc3dVVqVERmekVpazFmeTV3JTNEJTNE; tmr_detect=0%7C1674809142517',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="108", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        'https://ekat.rbt.ru/cat/cifrovye_ustroistva/smartfony/xiaomi_redmi_10c_3_64gb_blue/',
        headers=headers,
    )

    return response

