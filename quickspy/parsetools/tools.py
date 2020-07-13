def urlrepaire(relpath, url):
    '''repaire url relpath 相对路径'''
    _url = url.strip()
    if url[-1] == '/':
        _url[-1] == ''
    if not url[:8] == 'https://':
        if not url[:7] == 'http://':
            _url = 'http:/' + _url


def urlsrepaire(relpath, urls):
    pass