from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time


# Replace with full path to chromedriver.exe on your machine
chromedriver = 'path to chromedriver'
driver = webdriver.Chrome(chromedriver)

# Replace with VSCO account name
accountName = 'accountname' #'olibiz'

# Change according to where you want the photos saved
folder = f'vsco-{accountName}/'
url = f'https://vsco.co/{accountName}/gallery'

driver.get(url)

btn = driver.find_element_by_class_name('css-1a1rsew-SxButton-LoadMoreButton')
btn.click()

numScroll = 0
lastDist = distanceToTop = driver.execute_script("return window.scrollY;")
while True:
    numScroll += 1
    driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
    time.sleep(0.3) # Wait for content to load
    print(f'Scrolling...{numScroll}')
    distanceToTop = driver.execute_script("return window.scrollY;")
    if lastDist==distanceToTop: # Try to wait for content once more
        driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
        time.sleep(2)
        temp = driver.execute_script("return window.scrollY;")
        if distanceToTop == temp: # Position hasn't changed
            print('Reached end')
            break
        else: # False alarm
            lastDist = temp
    else:
        lastDist = distanceToTop

print('Scrolled to bottom')
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

print('Begin downloading images...')
num = 0
for fig in soup.find_all(class_='disableSave-mobile'):
    num+=1
    addr = fig.get('src')[2:-6]
    
    name = addr.split('/')[-1]
    name = f'{folder}{name}'
    
    addr = f'http://{addr}'
    print(name)
    r = requests.get(addr)
    with open (name, 'wb') as f:
        f.write(r.content)
    #print('success')
    print()

print(f'Succesfully downloaded {num} images')
time.sleep(5)

#driver.close()