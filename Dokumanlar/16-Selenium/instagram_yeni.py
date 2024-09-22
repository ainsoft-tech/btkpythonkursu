from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(options=self.browserProfile)  # 'chromedriver.exe' kısmını kaldırdım
        self.username = username
        self.password = password

    def signin(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameinput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordinput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)
        passwordinput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getfollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog] ul")
        followercount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))

        print(f"First count: {followercount}")

        action = webdriver.ActionChains(self.browser)

        while followercount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newcount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))

            if followercount != newcount:
                followercount = newcount
                print(f"Second count: {newcount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements(By.CSS_SELECTOR, "li")

        followerlist = []
        i = 0
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            followerlist.append(link)
            i += 1
            if i == max:
                break

        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerlist:
                file.write(item + "\n")

    def followuser(self, username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        followbutton = self.browser.find_element(By.TAG_NAME, "button")
        if followbutton.text != "Following":
            followbutton.click()
            time.sleep(2)
        else:
            print("Already following")

    def unfollowuser(self, username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME, "button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH, '//button[text()="Unfollow"]').click()
        else:
            print("Not following")


instgrm = Instagram(username, password)
instgrm.signin()
instgrm.getfollowers(50)
# instgrm.followUser('kod_evreni')
# instgrm.unFollowUser('kod_evreni')

# list = ["kod_evreni", "another_user"]

# for user in list:
#     instgrm.followUser(user)
#     time.sleep(3)
