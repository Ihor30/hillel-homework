class Url:

    def __init__(self, scheme='', authority='', path='', query='', fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment


    def __eq__(self, other):
        return self.__str__() == str(other)

    def __str__(self):
        result = f'{self.scheme}://{self.authority}'


        if self.path != '':
            result += '/' + '/'.join(self.path)

        if self.query != '':
            result += '?'
            for key, value in self.query.items():
                result += f'{key}={value}&'
            result = result[:-1]

        if self.fragment != '':
            result = '#' + self.fragment

        return result


class HttpsUrl(Url):

    def __init__(self, authority='', path='', query='', fragment=''):
        super().__init__('https', authority, path, query, fragment)


class HttpUrl(Url):

    def __init__(self, authority='', path='', query='', fragment=''):
        super().__init__('http', authority, path, query, fragment)


class GoogleUrl(HttpsUrl):

    def __init__(self, path='', query='', fragment=''):
        super().__init__('google.com', path, query, fragment)


class WikiUrl(HttpsUrl):

    def __init__(self, path='', query='', fragment=''):
        super().__init__('wikipedia.org', path, query, fragment)



assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
