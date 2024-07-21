class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set_item(self, key, value):
        script = f"localStorage.setItem('{key}', '{value}');"
        self.driver.execute_script(script)

    def get_item(self, key):
        script = f"return localStorage.getItem('{key}');"
        return self.driver.execute_script(script)

    def remove_item(self, key):
        script = f"localStorage.removeItem('{key}');"
        self.driver.execute_script(script)
