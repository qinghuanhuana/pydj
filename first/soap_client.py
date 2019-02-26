# coidng=utf-8
from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import
# suds_jurko: https://bitbucket.org/jurko/suds
# web sevice: http://www.webxml.com.cn/zh_cn/web_services.aspx
url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'
imp = Import('http://www.w3.org/2001/XMLSchema',location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
client = Client(url,plugins = [ImportDoctor(imp)])
# print(client)
result = client.service.getWeather('深圳')
print (result)