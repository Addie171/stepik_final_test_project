class BasePage():
    #конструктор (параметры -- экземпляр драйвера и url адрес)
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # метод, который открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)
