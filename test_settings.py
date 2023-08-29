import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

user="test@22au"
password="Test@123"
name='niyog'
mail='niyog@google.com'
invalidmail='niyog@sarva'
cardno='4242424242424242'
expiry='0428'
cvv='555'
zip='55555'

class Test_setting():

    @pytest.fixture()
    def test_invoke(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://qa-dev.iome.ai')
        self.driver.maximize_window()
        self.driver.find_element(By.TAG_NAME, 'button').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(user)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//div[@class="flex justify-center pt-6"]/button').click()
        time.sleep(6)

    def test_nodetails(self,test_invoke):
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check1=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check1.text=='All fields are mandatory'

    def test_onlyname(self,test_invoke):
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Name"]').send_keys(name)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check2=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check2.text=='All fields are mandatory'

    def test_onlymail(self,test_invoke):
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys(mail)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check3=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check3.text=='All fields are mandatory'

    def test_onlycard(self,test_invoke):
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        time.sleep(2)
        iframe=self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
        card=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')))
        self.driver.execute_script('arguments[0].click()',card)
        card.send_keys(cardno)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]/span/span/input').send_keys(expiry)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]/span/span/input').send_keys(cvv)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div[2]/span[2]/span[3]/span/span/input').send_keys(zip)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check4=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check4.text=='All fields are mandatory'

    def test_nameandmailonly(self,test_invoke):
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Name"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys(mail)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check5=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="mt-4"][2]/div/article')))
        check5.click()
        assert check5.text=='Your card number is incomplete.'

    def test_nameandcardonly(self,test_invoke):
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Name"]').send_keys(name)
        iframe=self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input').send_keys(cardno)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]/span/span/input').send_keys(expiry)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]/span/span/input').send_keys(cvv)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div[2]/span[2]/span[3]/span/span/input').send_keys(zip)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check6=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check6.text=='All fields are mandatory'

    def test_mailandcardonly(self,test_invoke):
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys(mail)
        iframe=self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input').send_keys(cardno)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]/span/span/input').send_keys(expiry)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]/span/span/input').send_keys(cvv)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div[2]/span[2]/span[3]/span/span/input').send_keys(zip)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check7=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check7.text=='All fields are mandatory'

    def test_invalidmail(self,test_invoke):
        self.driver.find_element(By.TAG_NAME, 'span').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Settings').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Name"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys(invalidmail)
        iframe=self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input').send_keys(cardno)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]/span/span/input').send_keys(expiry)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]/span/span/input').send_keys(cvv)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div[2]/span[2]/span[3]/span/span/input').send_keys(zip)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)
        check8=self.driver.find_element(By.XPATH, '//div[@class="mt-4"][2]/div/article')
        assert check8.text=='Invalid email address'

    # def test_ValidCred(self,test_invoke):
    #     self.driver.find_element(By.TAG_NAME, 'span').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.LINK_TEXT, 'Settings').click()
    #     self.driver.find_element(By.XPATH, '//input[@placeholder="Name"]').send_keys(name)
    #     self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys(mail)
    #     time.sleep(2)
    #     iframe=self.driver.find_element(By.TAG_NAME, 'iframe')
    #     self.driver.switch_to.frame(iframe)
    #     self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input').send_keys(cardno)
    #     self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]/span/span/input').send_keys(expiry)
    #     self.driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]/span/span/input').send_keys(cvv)
    #     self.driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div[2]/span[2]/span[3]/span/span/input').send_keys(zip)
    #     self.driver.switch_to.default_content()
    #     self.driver.find_element(By.TAG_NAME, 'button').click()
    #     time.sleep(10)
