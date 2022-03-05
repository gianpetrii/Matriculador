import autoit
from time import sleep
from selenium import webdriver
import os


username = "test.erapp" #Enter your username
password = "basquet1" #Enter your password
"""directorioActual = os.getcwd()
imagen = directorioActual + "\prueba.png"
imagen.replace("\\", "\ ")"""
image_path = r"C:\Users\gianp\PycharmProjects\INSTAGRAM\prueba.jpg" #The written path is just an example, Delete the path and Enter the Path of your image. #1. path should not start with a back slash
caption = "Enter photo caption here" #Enter the caption
etiquette = "Enter account"#if no etiquette leave empty
location = "Enter location"#if no location leave empty

mobile_emulation = { "deviceName": "Pixel 2" }
opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", mobile_emulation)

directorioActual = os.getcwd()
driver = webdriver.Chrome(directorioActual + "\chromedriver_win32\chromedriver.exe", options=opts)
main_url = "https://www.instagram.com"
driver.get(main_url)

sleep(4)

def login():
    login_button = driver.find_element_by_xpath("//button[contains(text(),'Iniciar sesión')]")
    login_button.click()
    sleep(3)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(password)
    password_input.submit()

login()

sleep(4)

def close_reactivated():
    try:
        sleep(2)
        not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Ahora no')]")
        not_now_btn.click()
    except:
        pass

close_reactivated()

def close_notification():
    try:
        sleep(2)
        close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Ahora no')]")
        close_noti_btn.click()
        sleep(2)
    except:
        pass

close_notification()

def close_add_to_home():
    sleep(3)
    close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancelar')]")
    close_addHome_btn.click()
    sleep(1)

close_add_to_home()

sleep(3)

close_notification()


def instaNewPost():#"""etiquette, location"""

    new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
    sleep(5)

    autoit.win_wait_active("Abrir")
    autoit.control_send("Abrir", "Edit1", image_path)
    autoit.control_click("Abrir", "Button1")

    """autoit.win_active("Open")
    sleep(2)
    autoit.control_send("Open","Edit1",image_path)
    sleep(1.5)
    autoit.control_send("Open","Edit1","{ENTER}")"""

    sleep(2)

    next_btn = driver.find_element_by_xpath("//button[contains(text(),'Siguiente')]").click()

    sleep(1.5)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Escribe un pie de foto o video...']")
    caption_field.send_keys(caption)

    """if etiquette != "":
        etiquetteClick = driver.find_element_by_xpath("//span[contains(text(),'Etiquetar personas')]")
        etiquetteClick.click()
        etiquetteClick.click()
    """







    share_btn = driver.find_element_by_xpath("//button[contains(text(),'Compartir')]").click()




instaNewPost()#"""etiquette, location"""

sleep(5)


driver.close()