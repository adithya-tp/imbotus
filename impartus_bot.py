import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()

driver.get("https://a.impartus.com/login/#/")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

#insert username and password here...
username.send_keys("<enter_your_user_name_here>")
password.send_keys("<enter_your_password_here")

login = driver.find_element_by_class_name("iu-btn")
login.click()

# these delays are only introduced in case the page takes some time to load up.
# you may remove or modify these delays according how fast your webpages load up.
time.sleep(5)

flag = 0
# this works out to selecting the first live class on the list.
class_button = driver.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[3]/dashboard-interests/div/live-streaming-lectures/md-card/md-list/div[1]/div[1]/div[2]/button')
# if the join button is live join the class
if class_button.is_enabled():
    class_button.click()
    time.sleep(5)

    # click on join button inside class
    driver.switch_to.window(driver.window_handles[1])
    #join_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/button[2]')
    join_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/button[2]')
    join_button.click()
    time.sleep(5)

    # send a message on chat. You're not a bot ofcourse sooo....
    chat_message = driver.find_element_by_xpath('//*[@id="imus-chat-input-editor"]')
    if int(time.ctime().split()[3][:2]) < 12:
        chat_message.send_keys("Good Morning!")
    else:
        chat_message.send_keys("Good Afternoon!")
    # send typed message
    send_button = driver.find_element_by_xpath('/html/body/div[1]/div/ng-include/div/div[3]/div/div[3]/i')
    send_button.click()

	# Check if class is over every minute (Sometimes classes get over early,
	# so hardcoding a waiting time before exiting is probably not advisable).
    while(flag == 0):
        try:
            class_ended_button = driver.find_element_by_xpath('/html/body/div[4]/md-dialog/md-dialog-actions/button')
            class_ended_button.click()
            flag = 1
        except:
            time.sleep(60)

    driver.switch_to.window(driver.window_handles[0])

# find the dropdown menu
dropdown_menu_button = driver.find_element_by_xpath('//*[@id="header"]/div[4]/div[4]/header-settings-menu/div/md-menu/div')
dropdown_menu_button.click()

time.sleep(5)

# find logout button and logout
logout_button = driver.find_element_by_xpath('//*[@id="menu_container_1"]/md-menu-content/md-menu-item[6]/button')
logout_button.click()
time.sleep(5)

driver.quit()
