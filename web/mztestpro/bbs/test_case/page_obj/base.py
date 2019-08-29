class Page(object):
    bbs_url = 'https://bbs.meizu.cn/'
    def __init__(self, driver, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        self.driver.get(url)
        assert self.on_page(), 'not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.base_url)

    def on_page(self):
        return self.driver.current_url == self.base_url
    
    def script(self, src):
        return self.driver.execute_script(src)