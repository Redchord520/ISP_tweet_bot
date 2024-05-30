from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 1200
PROMIDED_UP = 35
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/?lang=en"
TWITTER_EMAIL = "***"
TWITTER_PW = "***"
TWITTER_USERNAME = "***"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(SPEEDTEST_URL)
        self.provider = "Comcast"
        self.up = 0
        self.down = 0

    def display(self):
        # displays in console results from speed test and composes tweet
        print(
            f"Internet test speed result for {self.provider}:\nUpload speed: {self.up}Mbps\n"
            f"Download speed: {self.down}Mbps")
        TWEET = (f'Hey! @XfinitySupport, why is my upload speed at {self.up} Mbps and my download speed at {self.down} '
                 f'Mbps against your guaranteed upload speed {PROMIDED_UP}Mpbs and download speed {PROMISED_DOWN}Mbps?')
        return TWEET

    def get_internet_speed(self):
        # starts speed test and gathers up and down speeds
        self.driver.find_element(By.CSS_SELECTOR,
                                 value="#container > div > div.main-content > div > div > div > "
                                       "div.pure-u-custom-speedtest > div.speedtest-container.main-row > "
                                       "div.start-button > a > span.start-text").click()
        time.sleep(50)
        self.up = self.driver.find_element(By.CSS_SELECTOR,
                                           value="#container > div > div.main-content > div > div > div > "
                                                 "div.pure-u-custom-speedtest > div.speedtest-container.main-row > "
                                                 "div.main-view > div > div.result-area.result-area-test > div > div "
                                                 "> div.result-container-speed.result-container-speed-active > "
                                                 "div.result-container-data > "
                                                 "div.result-item-container.result-item-container-align-left > div > "
                                                 "div.result-data.u-align-left > span").text
        self.down = self.driver.find_element(By.CSS_SELECTOR,
                                             value="#container > div > div.main-content > div > div > div > "
                                                   "div.pure-u-custom-speedtest > div.speedtest-container.main-row > "
                                                   "div.main-view > div > div.result-area.result-area-test > div > "
                                                   "div > div.result-container-speed.result-container-speed-active > "
                                                   "div.result-container-data > "
                                                   "div.result-item-container.result-item-container-align-center > "
                                                   "div > div.result-data.u-align-left > span").text

    def tweet_at_provider(self):
        # open twitter
        self.driver.get(TWITTER_URL)

        # click login
        time.sleep(2)
        login = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div['
                                         '3]/div[5]/a/div/span')
        login.click()

        # input email
        time.sleep(3)
        email_input = self.driver.find_element(By.TAG_NAME, "input")
        email_input.send_keys(TWITTER_EMAIL, Keys.TAB, Keys.ENTER)

        # input username
        time.sleep(3)
        username_input = self.driver.find_element(By.TAG_NAME, "input")
        username_input.send_keys(TWITTER_USERNAME, Keys.ENTER)

        # input pw
        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PW, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)

        # allow twitter to load, input tweet, & send
        time.sleep(10)
        tweet = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweet.send_keys(TWEET)
        send = self.driver.find_element(By.XPATH,
                                        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                        '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div['
                                        '3]/div/span/span')
        send.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
TWEET = bot.display()
print(TWEET)
bot.tweet_at_provider()
