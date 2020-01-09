# coidng=utf-8
import requests
import json

class HttpRequests(object):
    def __init__(self):
        self.session = requests.session()

    def request_send(self, method, url, params_type='form', data=None, **kwargs):
        method = method.upper()
        params_type = params_type.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except:
                data = eval(data)
        if 'GET' == method:
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif 'POST' == method:
            if params_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            elif params_type == 'JSON':
                response = self.session.request(method=method, url=url, json=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, **kwargs)
        else:
            raise ValueError
        return response

    def __call__(self, method, url, params_type='form', data=None, **kwargs):
        return self.request_send(method, url, params_type=params_type, data=data, **kwargs)

    def close_session(self):
        self.session.close()
        try:
            del self.session.cookies['JSESSIONID']
        except:
            pass
request = HttpRequests()

if __name__ == '_main__':
    pass