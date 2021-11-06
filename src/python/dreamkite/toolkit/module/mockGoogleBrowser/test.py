from selenium import webdriver
import os


if __name__ == '__main__':
    chromedriver = "C:/Users/DreamKite/AppData/Local/Google/Chrome/Application/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver) #模拟打开浏览器
    driver.get("https://www.baidu.com/") #打开网址
    driver.maximize_window() #窗口最大化（无关紧要哈）
    # driver.quit()