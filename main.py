from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import smtplib

DRIVER_PATH = '/usr/local/bin/chromedriver'
SOURCE_EMAIL_ADDRESS =
SOURCE_EMAIL_PASSWORD =
DESTINATION_EMAIL_ADDRESS = ''

options = Options()
options.headless = True

def main():
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("")
    h1 = driver.find_element(By.CLASS_NAME, 'sectionDetails')
    inner_text = h1.get_attribute('innerText')
    inner_text = ' '.join(inner_text.split())
    ind = inner_text.find('Waitlist')
    capacity, num_waiting = inner_text[ind+10], inner_text[ind+14]
    print(capacity, num_waiting)
    if num_waiting < capacity:
        print("Sent mail!")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(SOURCE_EMAIL_ADDRESS, SOURCE_EMAIL_PASSWORD)
            subject='Check explorecourses'
            body = f''
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(SOURCE_EMAIL_ADDRESS, DESTINATION_EMAIL_ADDRESS, msg)
    while True:
        time.sleep(600)
        driver.close()
        main()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
