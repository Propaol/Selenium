class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def get_cookies(self):
        return self.driver.get_cookies()

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()


