import requests
from threading import Thread
import threading
import time

def view(prodUrl, index):
    session = requests.Session()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    session.get(prodUrl, headers=headers)
    print("[SUCCESSFULLY VIEWED # " + str(index) + "]" )

def start(numView, productUrl):
    isDone = False
    while (isDone == False):
        #threads = [] 
        for i in range(numView):
            t = Thread(target = view, args = (productUrl,i))
            #threads.append(t)
            t.start()
            time.sleep(0.5)
        isDone=True
        
def loopStart(numTimes, productUrl):
    for i in range(numTimes):
        view(productUrl)
start(100, 'https://www.ebay.com/itm/123481130583')
