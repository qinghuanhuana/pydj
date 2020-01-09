from jpype import *
import os.path
startJVM("D:\\Program Files\\Java\\jdk1.8\\jre\\bin\\server\\jvm.dll", "-ea", convertStrings=True)
java.lang.System.out.println("hello World")
shutdownJVM()