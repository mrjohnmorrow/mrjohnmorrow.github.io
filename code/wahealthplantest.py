from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
import os

username = "username"
password = "password"
#set up profile
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/pgn")

#create driver with profile settings
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://www.chess.com/home/my_archive")
#login if you have to
if "Login" in driver.title:
    usernamefield  = driver.find_element_by_name("c1")
    usernamefield.send_keys(username)
    passwordfield  = driver.find_element_by_name("loginpassword")
    passwordfield.send_keys(password)
    passwordfield.send_keys(Keys.RETURN)
else:
    #do nothing for now
	assert "My Chess" in driver.title
#get the td element containing the link
lastgame_td = driver.find_element_by_id("c18_row0_6")
#link is always the first child on td element
lastgame_link = lastgame_td.find_elements_by_xpath(".//*")[0]
game_link = lastgame_link.get_attribute("href")
driver.get(game_link)
game_id  = re.search('[0-9]*\Z', game_link).group(0)
pgn_link = "http://www.chess.com/echess/download_pgn?lid=" + game_id
print pgn_link
driver.get(pgn_link)
#driver.close()
