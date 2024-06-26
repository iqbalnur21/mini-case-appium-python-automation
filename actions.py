from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def action(driver, waitTime, findBy, value, action, text):
    wait = WebDriverWait(driver, waitTime)
    
    # using try catch function to prevent error
    try:
        # if else statement react based on findBy value
        if(findBy == "id"):
            element = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, value))
            )
        elif(findBy == "xpath"):
            element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, value))
            )
        else:
            print("Parameter tidak valid")
            
        
        # if else statement react based on action value
        if(action == "click"):
            element.click()
        elif(action == "text"):
            element.send_keys(text)
        elif(action == "getText"):
            return element.text
        else:
            print("Parameter tidak valid")
    except:
        return False