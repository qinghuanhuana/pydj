# coidng=utf-8
import yaml,os
cur = os.path.dirname(os.path.dirname(__file__))
def readtoken(yamlName="token.yaml"):
    p = os.path.join(cur,"Data",yamlName)
    with open(p,'r') as f:
        t = yaml.load(f.read())
    return t["Cookie"]

if __name__ == "__main__":
    print(readtoken())
