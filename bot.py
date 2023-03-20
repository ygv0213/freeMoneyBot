import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

users = ["davidfreelancer2328@proton.me", "davidfree67lancer2328@proton.me", "davidfreelancer28@proton.me", "davidfreelancer28@gmail.com", "ygv.vgy28@proton.me"]
passwords = ["C69VY@+PTfpBP4&fgv", "C69VY@+65PTfpBP4&fgv", "C69VY@+PTfpBP4&", "C69VY@+PTfpBP4&", "hgdfhgFGHFgfj@$#@"]
i = 0

links = ["https://s4.wintub.com/dashboard.php?", "https://s4.wintub.com/dashboard.php?v=2", "https://s4.wintub.com/dashboard.php?v=3", "https://s4.wintub.com/dashboard.php?v=4", "https://s4.wintub.com/dashboard.php?v=5"]

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

options.binary_location = brave_path

# Create new automated instance of Brave
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def watch_vid(u, p, l):
    from selenium.common.exceptions import NoSuchElementException
    
    driver.get("https://s4.wintub.com/login.php")
    driver.find_element("name", "email").send_keys(u)
    driver.find_element("name", "password").send_keys(p)
    driver.find_element(By.CSS_SELECTOR, ".btn").click()

    for link in l:

        driver.get(link)
        time.sleep(4)

        try:
            driver.find_element(By.ID, "playerif").click()
            time.sleep(40)
            driver.find_element(By.CLASS_NAME, "strat1").click()
            time.sleep(5)
        except NoSuchElementException:
            try:
                driver.find_element(By.ID, "playerif").click()
                time.sleep(40)
                driver.find_element(By.CLASS_NAME, "strat1").click()
                time.sleep(5)
            except NoSuchElementException:
                continue
            continue

for user, password in zip(users, passwords):
    watch_vid(user, password, links)
    print("secsefully finish user" + str(i))
    i = i+1
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "LogOut").click()
    time.sleep(1)

driver.quit()

#frist version done