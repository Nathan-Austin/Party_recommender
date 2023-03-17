import asyncio
from time import sleep
from random import randint
from pyppeteer import launch
import json
import subprocess

events=[]
djs=[]
async def main():
    # launch chromium browser in the background
    # open a new tab in the browser
    browser = await launch({"headless": False}, executablePath= "/usr/bin/google-chrome")
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://ra.co/events/de/berlin")
    await page.setViewport({"width": 1600, "height": 900})
    a_list = await page.querySelectorAll('a[data-test-id="event-listing-heading"]')
    links = ([await page.evaluate('(element) => element.href', a) for a in a_list])
    print('found {} link(s)'.format(len(links)))
    events.append(links)
    file1 = open("myfile.txt","w")
    for link in links:
        await page.goto(link)
        await asyncio.sleep(0.5)
        b_list = await page.querySelectorAll('div[data-tracking-id="event-detail-lineup"]>span>a')
        print(b_list)
        
        blinks= set([await page.evaluate('(element) =>element.href', b) for b in b_list])
        for blink in blinks:
            str=repr(blink)
            file1.writelines(str + "\n")
        
        def send_list(blinks):
            list = blinks
            return list
               
        print(blinks)
           
        sleep(randint(1, 3))
        # close the browser
    await browser.close()
    file1.close()
print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
