from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
time.sleep(3)
input = "ElDorado"
destin = "punta cana"
bot.get("https://www.viajesexito.com/")

time.sleep(6)
iframe = bot.find_element(By.XPATH, '/html/body/div[6]/div/div/iframe')
bot.switch_to.frame(iframe)

time.sleep(3)

close_button = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]')

close_button.click()

time.sleep(2)

bot.switch_to.default_content()

time.sleep(2)

hotelvuelo = bot.find_element(By.XPATH, '//*[@id="paquetesTooltips"]/a')
time.sleep(2)

hotelvuelo.click()
time.sleep(2)


origen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')


origen.click()
time.sleep(4)

origeninput = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origeninput.click()
origeninput.send_keys(input)
time.sleep(2)

seleccionarorigen = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li[1]/div')
seleccionarorigen.click()
time.sleep(3)

destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destino.click()
time.sleep(3)

destinoinput = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destinoinput.click()
destinoinput.send_keys(destin)

seleccionardestino = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul')
seleccionardestino.click()
time.sleep(3)


fechasalida = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
fechasalida.click()
time.sleep(3)
dia = bot.find_element(By.XPATH,'/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[4]/div[2]/div[1]')

dia.click()
time.sleep(3)

regreso = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]/div[1]')
regreso.click()
time.sleep(3)

aceptar = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')

aceptar.click()
time.sleep(3)

abrirhabitaciones = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div')
abrirhabitaciones.click()
time.sleep(3)

agregarhabitacion = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
agregarhabitacion.click()
time.sleep(2)

aplicar = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
aplicar.click()
time.sleep(2)

buscar = bot.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a')
buscar.click()
time.sleep(30)