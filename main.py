#in PyCharm you can se the results faster thn Vs!
from selenium import webdriver


chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


#driver.get("https://www.amazon.com/-/de/dp/B083J8NYYF/ref=sr_1_134?keywords=amazonbasics&pd_rd_r=d1548ed9-a0cd-41be-ac23-2be05fed1962&pd_rd_w=kUhUM&pd_rd_wg=2hjMV&pf_rd_p=f629053b-dba8-4e72-8876-38e8cf31e925&pf_rd_r=QRAYHR6P4N7NV9N0MQGR&qid=1662105198&sr=8-134&th=1")
#price = driver.find_element_by_id("corePrice_feature_div")
#print(price.text)

search_bar = driver.get("https://www.python.org")
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)
#driver.find_element_by_id("content")
#driver.find_element_by_name("search-button")
#print(search_bar.get_attribute("title")
#print(search_bar.get_attribute("placeholder")

#documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
#print(documentation_link.text)

#bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link)