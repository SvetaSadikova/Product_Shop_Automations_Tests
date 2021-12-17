class ShopApplication:
    def __init__(self, driver, url):
        self.MyDriver = driver
        self.MyUrl = url

    def quit(self):
        self.MyDriver.quit()

    def open_page(self):
        self.MyDriver.get(self.MyUrl)

