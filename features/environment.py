from selenium import webdriver

def before_feature(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)

def after_feature(context, scenario):
    context.driver.quit()
