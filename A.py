import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
driver=Chrome('D:\\selenium_Drivers\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.facebook.com/campaign/landing.php?campaign_id=1653993517&extra_1=s%7Cc%7C318504236057%7Ce%7Cfacebook%7C&placement=&creative=318504236057&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1653993517%26adgroupid%3D63066387003%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D1007768%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMI847Y1fSz5QIVFoiPCh2VfAOlEAAYASAAEgKREPD_BwE')


month=driver.find_element_by_name('birthday_month')
monthse=Select(month)
# it is used to capture dropdown value
lst=monthse.options
for i in lst:
    print(i.text)

for j in range(0,len(lst)):
    print(lst[j].text)