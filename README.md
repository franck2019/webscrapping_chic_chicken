# webscrapping_chic_chicken
The task is to scrap data concerning all comments made on the restaurant chic chicken in Yaounde(Cameroon)

### Tools
1- python 3 + librairies
 > * selenium, webdriver
 > * BeautifulSoup from bs4
 > * datetime
 > * sleep
 > * json
 
2- Google Chrome

3- editor (vi, vscode,...)


### Notes

- Make sure you install the driver for google chrome and for your os.

- For windows os, change  the code below
```
driver = webdriver.Chrome(chrome_options=options)
```

by 

```
chromedriver_path = "D:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
```

