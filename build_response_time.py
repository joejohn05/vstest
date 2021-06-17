import datetime
from typing import Any
import requests
from urllib.request import urlopen

url=['https://storefront.originalimpressions.com','https://api.booker-tools.com','https://mmm.originalimpressions.com','https://flblue.originalimpressions.com','https://hsportal.originalimpressions.com','https://Mmmagentstore.com']
#url = 'https://partners.direct-booker.com'

for urlchecker in url :

 
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(urlchecker, timeout=10,headers=headers)
        r.raise_for_status()
        respTime = str(round(r.elapsed.total_seconds(),3))
        currDate = datetime.datetime.now()
        currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
        print("URL:"+urlchecker+ " | " + "Page Load Time:"+ respTime)
        if respTime>= str(1.0):
            print("d")
    except requests.exceptions.HTTPError as err01:
        print ("HTTP error: ", err01)
    except requests.exceptions.ConnectionError as err02:
        print ("Error connecting: ", err02)
    except requests.exceptions.Timeout as err03:
        print ("Timeout error:", err03)
    except requests.exceptions.RequestException as err04:
        print ("Error: ", err04)

    