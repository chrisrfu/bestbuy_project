from uszipcode import SearchEngine
import time
#Simple assignment
from selenium.webdriver import Chrome

search_zipcode = SearchEngine()
driver = Chrome(executable_path='./chromedriver')

#Or use the context manager
from selenium.webdriver import Chrome

def search(zipcode):
    driver.get('https://www.bestbuy.com/site/store-locator')

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/form/fieldset/div/input').send_keys(zipcode)

    try:
        driver.find_elemeny_by_xpath('/html/body/div[6]/div/div/div[3]/button[2]').click()
    except:
        pass
    
    driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/form/fieldset/div/button').click()

    time.sleep(3)
    #make this your store
    try:
        driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[1]/div/div/ul/li[1]/div[1]/div/div[2]/div/div/div/div[2]/button').click()
    except:
        try:
            driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[1]/div/div/ul/li[2]/div[1]/div/div[2]/div/div/div/div[2]/button').click()
        except:
            try:
                driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[1]/div/div/ul/li[1]/div[1]/div/div[2]/div/div/div/div[2]/a').click()
            except:
                driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[1]/div/div/ul/li[2]/div[1]/div/div[2]/div/div/div/div[2]/a').click()

    driver.get("https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=condition_facet%3DCondition~Open-Box&st=6418597"
    )

    time.sleep(3)

    try:   
        available = driver.find_element_by_xpath('/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[4]/div/div[6]/ol/li[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/a')
    except:
        try:
            available = driver.find_element_by_xpath('/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[5]/ol/li[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/a')
        except:
            try:
                available = driver.find_element_by_xpath('/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[4]/div/div[6]/ol/li[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/button')
            except:
                available = driver.find_element_by_xpath('/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[5]/ol/li[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/button')

    print(available.text)

    if available.text != 'Unavailable Nearby':
        city_name = search_zipcode.by_zipcode(int(zipcode)).major_city
        state_abbr = search_zipcode.by_zipcode(int(zipcode)).state_abbr
        print("IN STOCK in: {zipcode} ({city_name}, {state_abbr})".format(zipcode = zipcode,
        city_name = city_name, state_abbr = state_abbr))

zipcodes = open("zipcodes.txt", "r")

for aline in zipcodes:
    values = aline.split()
    print(values[0], type(values[0]))
    search(values[0])
zipcodes.close()



