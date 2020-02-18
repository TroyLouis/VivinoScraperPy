from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

def red_wine():

    driver = webdriver.Firefox()
    red_wine_web_address = 'https://www.vivino.com/explore?e=eJwNybEKgCAUBdC_ubNR6936g2iKiJeZCKmhYvX3uZzl-MQO3gUqeHk5KAX9cZ6gGyPutvZkleRMkQtxZ5Ligs2bVJPEGkQeJms8ZVnZI1PLD4MgHDE='
    driver.get(red_wine_web_address)
    timeout = 3
    red_wine_number = 0
    red_wine_list = []
    red_df = pd.DataFrame(columns=['Name', 'Rating', 'Price', 'NumberOfRatings', 'Country', 'Winery'])

    while True:

        red_wine_number += 1

        if red_wine_number % 24 == 0:

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                element_present = EC.presence_of_element_located(
                    (By.XPATH, f'//*[@id="explore-page-app"]/div/div/div[2]/div[2]/div[1]/div[{red_wine_number + 24}]'))
                WebDriverWait(driver, timeout).until(element_present)

            except:
                print("NOT 24 WINES")
                red_df.to_excel('sparkling_wine_0to400_anyrating.xlsx', encoding='utf8')
                driver.close()
                return False

        else:
            try:
                data_elements = driver.find_elements_by_xpath(
                    f'//*[@id="explore-page-app"]/div/div/div[2]/div[2]/div[1]/div[{red_wine_number}]')[0]
                data = data_elements.text.splitlines()
                red_df = red_df.append({'Name': data[1], 'Rating': data[5], 'Price': data[7], 'Country': data[2],
                                'NumberOfRatings': data[6], 'Winery': data[0]}, ignore_index=True)

                red_wine_list.append(data[0] + ' ' + data[1])
                for item in red_wine_list:
                    if red_wine_list.count(item) > 2:
                        print(item)
                        red_df.to_excel('sparkling_wine_0to400_anyrating.xlsx', encoding='utf8')
                        print("Done")
                        driver.close()
                        return False

            except IndexError:
                red_df = red_df.append({'Name': '', 'Rating': '', 'Price': '', 'Country': '',
                                'NumberOfRatings': '', 'Winery': ''}, ignore_index=True)


if __name__=='__main__':
    red_wine()
