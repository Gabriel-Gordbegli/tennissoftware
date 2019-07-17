#dependent on #sudo apt-get install #sudo apt-get install libxml2-dev libxslt-dev python-dev #pip install lxmln #pip install pyautogui #pip install Xlib
# login_token found on log in page ctrl-f for it, cookie found after loggin in under network --> xhml or html, copy the whole thing
import requests
import lxml
from lxml import html
from pykeyboard import PyKeyboard
k=PyKeyboard()

loginname = raw_input("Enter your login/email then click enter: \n")
loginpassword = raw_input("Enter your password then click enter: \n")
thelogintoken = raw_input("Paste in the login token then click enter: \n")
thecookie = raw_input("Paste in the cookie string then click enter: \n")
print ("\n")


#uses the name attribute
payload = {
    "login": str(loginname),
    "pass-text": str(loginpassword),
    "login_token": str(thelogintoken)
}

session_requests = requests.session()

login_url = "https://brtc.clubautomation.com/"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='login_token']/@value")))[0]

result = session_requests.post(
	login_url,
	data = payload,
	headers = dict(referer=login_url)
)

webpage = raw_input("Paste in the url of the rooster whose members you would like to copy, then press enter. You will have 10 seconds to click the search box of the rooster in which you would like to paste the names. \n")
headers = {
        'Cookie': str(thecookie)
        }
page = requests.get(webpage, headers=headers)
tree = html.fromstring(page.content)

selector = '//*[@class="pull-left"]/text()'
content = str(tree.xpath(selector))

k.tap_key(' ',n=2,interval=10)#10 seconds before program starts

x = 4 #skips garbage at begginging

while x<=(len(content)):

    if content[(x+1)] == "\'":
        x = x+6
        k.tap_key(" ",n=1,interval=7)
        k.tap_key('Down',n=1,interval=1)
        k.tap_key('Return',n=1,interval=7)

    if x>=(len(content)):
        break

    else:
        x = x+1
        k.tap_key(str(content[x]))
