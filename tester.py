import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

                #primero tengo que traer el driver, para eso uso la busco desde el archivo actual
directorioActual = os.getcwd()



                #abro driver y voy a la pagina de matriculacion
driver = webdriver.Chrome(directorioActual + "\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.anac.gob.ar/anac/web/index.php/2/215/consulta-de-tramites/consulta-de-tramites-rna")
time.sleep(5)




                #clickeo para seleccionar matricula
driver.execute_script("window.scrollTo(0, 200)") #bajo un poco


                #abro el frame
iframe = driver.find_element_by_tag_name("iframe")
iframe = driver.find_element_by_tag_name("iframe").get_attribute('src')

driver.execute_script("window.open('')")
driver.switch_to.window(driver.window_handles[1])
driver.get(iframe)
time.sleep(5)
driver.find_element_by_id("opmat").click()



        #traigo listado de matriculas
listado = open( "Matriculas.txt", "r")

matricula = listado.readline().rstrip("\n")

while matricula != "0":

    driver.find_elements_by_xpath("//input[@id='txtbuscar']")[0].clear()

    driver.find_elements_by_xpath("//input[@id='txtbuscar']")[0].send_keys(matricula)

    driver.find_elements_by_xpath("//input[@id='txtbuscar']")[0].send_keys(Keys.ENTER)

    time.sleep(5)

    try:
        ver = driver.find_elements_by_link_text("ver")

        ver[len(ver) - 1].click()

        try:
            detalle = driver.find_elements_by_link_text("detalle")

            detalle[len(detalle) - 1].click()
            time.sleep(6)


            driver.switch_to.window(driver.window_handles[2])

            driver.get_screenshot_as_file("Matriculas/" + matricula + ".png")

            driver.close()

            driver.switch_to.window(driver.window_handles[1])

            driver.back()

        except:
            driver.get_screenshot_as_file("Matriculas/" + matricula + ".png")
            driver.back()

        time.sleep(6)

    except:
        driver.get_screenshot_as_file("Matriculas/" + matricula + ".png")




    matricula = listado.readline().rstrip("\n")





driver.quit()