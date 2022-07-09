import re

def addurl(url):
  with open('./url.txt', 'a') as f:
    f.write('\n')
    f.write(url)


def read_str():
    with open('./url.txt', 'r') as f:
      pool = f.read()
      
    return pool
  