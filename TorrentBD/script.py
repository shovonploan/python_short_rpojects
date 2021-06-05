from selenium import webdriver
from time import sleep
import pandas as pd
import datetime

now = str(datetime.date.today())
time = []
CuSB = []
SeBR = []


class TBBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.torrentbd.me")
        self.driver.find_element_by_xpath("/html/body/main/div/p/a").click()
        self.login_field = self.driver.find_element_by_xpath(
            "/html/body/main/div/div/div/div/form/div/div/div[1]/div/div[1]/input").send_keys(username)
        self.login_field = self.driver.find_element_by_xpath(
            "/html/body/main/div/div/div/div/form/div/div/div[1]/div/div[2]/input").send_keys(pw)
        self.driver.find_element_by_xpath(
            "/html/body/main/div/div/div/div/form/div/div/div[2]/div/div[1]/button").click()
        self.driver.find_element_by_xpath(
            "/html/body/main/div/div[1]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/a").click()
        CuSB.append(self.driver.find_element_by_xpath(
            '/html/body/main/div/div[2]/div[1]/div[2]/h5/span/b').text)
        SeBR.append(self.driver.find_element_by_xpath(
            '/html/body/main/div/div[2]/div[1]/div[2]/p[1]/a').text)
        self.driver.close()


my_bot = TBBot('TorrentzBD', 'shikipana')
t = datetime.datetime.now()
time.append(t.strftime("%H:%M"))
data = {'Time': time, 'Current Seed Bouns': CuSB, 'Seed Bound Rate': SeBR}
df = pd.DataFrame(data, columns=['Time','Current Seed Bouns', 'Seed Bound Rate'])
df.to_csv(r'C:\Users\Admin\Google Drive\Programming\Python_Prac\Projects\TorrentBD\%s data.csv' % (
    now), index=False, header=True)

for i in range(49):
    sleep(1800)
    t = datetime.datetime.now()
    time.append(t.strftime("%H:%M"))
    my_bot = TBBot('TorrentzBD', 'shikipana')
    df_marks = pd.DataFrame(data)
    new_row = {'Time': time, 'Current Seed Bouns': CuSB,
               'Seed Bound Rate': SeBR}
    df_marks = df_marks.append(new_row, ignore_index=True)
    df_marks.to_csv(f'{now} data.csv', mode='a', header=False)
