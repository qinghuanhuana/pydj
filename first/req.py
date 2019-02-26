# coidng=utf-8
from zope.interface import Interface
from zope.interface.declarations import implementer
import zope.interface
class IHost(Interface):
    '''momingqimiao'''
    x = zope.interface.Attribute('''xxxxxx''')
    def goodmorning(host):
        """say good morning to host"""
@implementer(IHost)
class Host:
    def goodmorning(self,guest):
        """say good morning to guest"""
        print("good morning,%s"% guest)
if __name__ == "__main__":
    p = Host()
    hi = p.goodmorning('yang')
    x = IHost['x']
    print(type(x))