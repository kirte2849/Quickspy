class UrlManager:

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return self.new_urls_size() != 0

    def new_urls_size(self):
        return len(self.new_urls)

    def old_urls_size(self):
        return len(self.old_urls)

    def add_new_url(self, url):
        if url is None:
            return

        self.new_urls.add(url)
        # if url not in self.old_urls and url not in self.new_urls:
        #     self.new_urls.add(url)

    def push(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in ulrs:
            self.add_new_url(url)

    def get_url(self):
        if self.new_urls:
            new_url = self.new_urls.pop()
            self.old_urls.add(new_url)
            return new_url
        else:
            return None


