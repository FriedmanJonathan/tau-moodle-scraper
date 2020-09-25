from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Chrome by default opens PDFs in a viewer instead of downloading, so
# we'll change the settings to fix that.
chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

# Inputting the driver path and the site we'd like to access (Moodle)
DRIVER_PATH = r'C:/Users/yonif/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.get('https://moodle.tau.ac.il/login/index.php')


def downloadAllPDFs():
    # First we have to login again to the 2019 site.
    url = 'https://moodle.tau.ac.il/2019/login/index.php'
    driver.get(url)
    # Then we can access the page(s) we want to download from.
    url = 'https://moodle.tau.ac.il/2019/course/view.php?id=1231221132'
    driver.get(url)
    # Finally, we can find all of the PDF, WORD, and PPT elements, which
    # are conveniently classified in Moodle as קובץ (='file').
    activities = driver.find_elements_by_class_name('activityinstance')
    for activity in activities:
        if 'קובץ' in activity.text:
            activity.click()

foundTargetUrl = False
timeElapsed = 0
while not foundTargetUrl and timeElapsed < 60:
    time.sleep(1)
    timeElapsed += 1
    if driver.current_url == r"https://moodle.tau.ac.il/my/":
        downloadAllPDFs()
        foundTargetUrl = True
