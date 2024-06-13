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
aerolinea="latam"
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

all_handles = bot.window_handles

bot.switch_to.window(all_handles[-1])
time.sleep(5)

precio1 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 1 es de: " + precio1)

time.sleep(3)


precio2 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 2 es de: " + precio2)

time.sleep(3)

precio3 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 3 es de: " + precio3)

time.sleep(3)

precio4 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 4 es de: " + precio4)

time.sleep(3)

precio5 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 5 es de: " + precio5)

time.sleep(3)

precio6 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 6 es de: " + precio6)

time.sleep(3)

precio7 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 7 es de: " + precio7)

time.sleep(3)


precio8 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 8 es de: " + precio8)

time.sleep(3)

precio9 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 9 es de: " + precio9)

time.sleep(3)

precio10 = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(3)
print("El precio del paquete 10 es de: " + precio10)

time.sleep(3)

opcionesavanzadas = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
opcionesavanzadas.click()
time.sleep(3)

aerolineainput = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolineainput.click()
aerolineainput.send_keys(aerolinea)
time.sleep(3)

latam= bot.find_element(By.XPATH,'/html/body/ul[3]/li[2]/a')
latam.click()
time.sleep(3)

buscarporaerolinea = bot.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscarporaerolinea.click()
time.sleep(25)

precio11 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio12 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio13 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio14 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text

with open('paquetes.txt','w') as file:
    file.write("El precio del paquete 1 de latam es de: " + precio11 + "\n" +
               "El precio del paquete 2 de latam es de: " + precio12 + "\n" +
               "El precio del paquete 3 de latam es de: " + precio13 + "\n" +
               "El precio del paquete 4 de latam es de: " + precio14 + "\n")
    
bot.save_screenshot("Captura.png")
bot.quit()