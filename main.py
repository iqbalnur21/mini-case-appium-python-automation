from appium import webdriver
from appium.options.android import UiAutomator2Options
from actions import action
from config import desired_caps, appium_url, loginButtonId, emailId, passwordId, submitButtonId, successLoginId

if __name__ == "__main__":       
    try:
        driver = webdriver.Remote(appium_url, options=UiAutomator2Options().load_capabilities(desired_caps))
        while True:
            action(driver, 5, "id", loginButtonId, "click", "")
            print("\nPilihan:")
            print("0. Tutup driver")
            print("1. Lakukan otomasi dengan kredensial default")
            print("2. Masukkan email dan password oleh pengguna")
            
            option = int(input("Masukkan pilihan (0/1/2): "))
            
            # react differently based on option
            if option == 0:
                driver.quit()
                break
            elif option == 1:        
                action(driver, 5, "id", emailId, "text", "admin@gmail.com")
                action(driver, 5, "id", passwordId, "text", "admin123")
                action(driver, 5, "id", submitButtonId, "click", "")
                print("Login Berhasil!")
            elif option == 2:
                while True:
                    email = input("Masukkan email: ")
                    password = input("Masukkan password: ")
                    action(driver, 5, "id", emailId, "text", email)
                    action(driver, 5, "id", passwordId, "text", password)
                    action(driver, 5, "id", submitButtonId, "click", "")
                    print("Loading ... ")
                    
                    # check if there is the element that appear when login success
                    status = action(driver, 3, "xpath", successLoginId, "getText", "")
                    
                    # if login success, while loop stop
                    if status:
                        print("Login Berhasil!")
                        break
                    print("\nEmail atau password salah!, coba masukkan kembali")
            else:
                print("Pilihan tidak valid")
    
            input("klik enter untuk melanjutkan ... ")
            # back twice to reset input in input element
            driver.back()
            driver.back()
    except Exception as e:
        print(f"error: {str(e)}")
