from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os


class Marker():

    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url

    def submit(self, cpf, senha):
        self.driver.get(self.url)
        captcha = self._get_captcha()
        self._setup_fields(cpf, senha, captcha)
        self.driver.find_element(By.ID, 'btOk').click()

    def _get_captcha(self):
        return self.driver.get_cookies()[0]['value']

    def _setup_fields(self, cpf, senha, captcha):
        Select(self.driver.find_element(By.ID,'cboCampo')).select_by_value('2')
        try:
            self.driver.find_element(By.ID,'txtValor').send_keys(cpf)
            self.driver.find_element(By.ID,'txtSENHA').send_keys(senha)
        except KeyError:
            raise KeyError('CPF ou Senha nao configurados como variavel de ambiente')
        
        self.driver.find_element(By.ID,'captchacode').send_keys(captcha)
        return
    

if __name__ == '__main__':
    try:
        cpf, senha, url = os.environ['PONTO_CPF'], os.environ['PONTO_SENHA'], os.environ['PONTO_URL']
        marker = Marker(webdriver.Safari(), url)
        marker.submit(cpf,senha)
    except KeyError:
        raise KeyError('CPF ou Senha nao definidos como variaveis de ambiente')



