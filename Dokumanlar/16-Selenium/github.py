from githubUserInfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password
        self.followers = []

    def signin(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[8]").click()

    def loadfollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray.pl-1").text)


    def getfollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        self.loadfollowers()

        while True:
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadfollowers()

                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadfollowers()
                    else:
                        continue


github = Github(username, password)
github.signin()
github.getfollowers()
print(len(github.followers))
print(github.followers)


