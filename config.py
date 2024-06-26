# change the data
appium_url = "http://localhost:4723"
desired_caps = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='your_emulator_name', #default: emulator-5554
    appPackage='com.code2lead.kwad',
    appActivity='.MainActivity',
    language='en',
    locale='US'
)

# dont change this data
loginButtonId = 'com.code2lead.kwad:id/Login'
emailId = 'com.code2lead.kwad:id/Et4'
passwordId = 'com.code2lead.kwad:id/Et5'
submitButtonId = 'com.code2lead.kwad:id/Btn3'
successLoginId = '//android.widget.TextView[@text="Enter Admin"]'