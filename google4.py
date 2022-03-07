from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import datetime
import json

#chromedriver_path = "D:\Chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome(chromedriver_path, chrome_options=options)

#launch page with the driver google chrome
driver.get("https://www.google.com/maps/place/Chips+and+Chicken+(C%26C)/@3.8588198,11.5024991,17z/data=!4m5!3m4!1s0x108bcf9833bb176d:0xb5bcdad4926bdc45!8m2!3d3.8588198!4d11.5046878")
print("Printed Page. Wait 30 secondes")
driver.implicitly_wait(30) # seconds

# find the button via xpath method and perform a click to open the complete comments page.
button = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span[1]/span[2]/span[1]/button')
print(button.get_attribute('innerHTML'))
button.click()

#find the element on which we are going to scroll everytimes.
print("2e Page affichée. 30 secondes d'attentes")
driver.implicitly_wait(30) # seconds
elem = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[9]/div[1]/div/div[3]/div[2]/div/div/a')
print(elem.get_attribute('innerHTML'))

#we perform the scroll from our current position to the end on the page 34 times by using the send_keys(Keys.END) function
for i in range(34):
    elem.send_keys(Keys.END)
    sleep(2)

#Here we retrieve the cards we need for every comment with xpath method on "//div[@jstcache = '719']" which are xpath of every card in the source of the page.
contents = driver.find_elements_by_xpath("//div[@jstcache = '719']")
comments = [element.get_attribute('innerHTML') for element in contents]  #We get the html content of every cards(contents) 
print("\n")
print(len(comments))

driver.close()

print("\n")

def get_info(comment):

    """
    function get_info: retrieve infos for a comment
    input: comment is a html code containing[name(author),stars(the note given by the author),comment(text of comment),replies(number of like)]
    output: data a dictionary (data{"name": name, "stars": stars, "comment": stars, "replies": replies})
    """
    soup = BeautifulSoup(comment, 'lxml')
    
    data = {}
    
    #the name is inside a span element with attribute "jstcache"="620"
    name_soup = soup.find("span", attrs={"jstcache" : "620"})
    #Here we retrieve the text and we remove blank space bafore anf after the text
    name = name_soup.text.strip()
    data['name'] = name
    
    #the stars is inside the 'aria-label' attribute value  of a  span element with attribute "jstcache"="432"
    stars_soup = soup.find("span", attrs={"jstcache" : "432"})
    #Here we retrieve the 'aria-label' attribute value and we remove blank space bafore anf after the text, then we take the first element. e.g: " 3&nbsp;étoiles "
    stars = stars_soup['aria-label'].strip()[0]
    data['stars'] = stars
    
    #the time is inside the span element with attribute "jstcache"="433"
    time_soup = soup.find("span", attrs={"jstcache" : "433"})
    #Here we retrieve the text and we remove blank space bafore anf after the text, then we take the first element. e.g: " 3&nbsp;étoiles "
    time = time_soup.text.strip()
    data['time'] = time
    
    #the comment is inside the span element with attribute "jstcache"="437"
    comment_soup = soup.find("span", attrs={"jstcache" : "437"})
    #Here we retrieve the text and we remove blank space bafore anf after the text
    comment = comment_soup.text.strip()
    data['comment'] = comment
    
    #the comment is inside the span element with attribute "jstcache"="540"
    replies_soup = soup.find("span", attrs={"jstcache" : "540"})
    #Here we retrieve the text and we remove blank space bafore anf after the text
    if replies_soup is None:
        replies = '0'
    else: 
        replies = replies_soup.text.strip() or '0'
    data['replies'] = replies
    
   
    
    #name = soup.find("span", class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
    return data

result = [get_info(element) for element in comments]

#Write into a .json file MonthDayYear with a date and time
filename = 'chic_chicken_data-' + '|'.join(str(datetime.datetime.now()).split(' '))+ '.json'

with open(filename, 'w', encoding='utf-8') as f:
    f.write(json.dumps(result, ensure_ascii=False))

#print a log to say that the file has been well created
print(f'Saved file {filename}')


#print(result[0:20])


#attrs={"href" : "setting-up-django-sitemaps"}
