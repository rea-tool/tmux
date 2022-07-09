import os
import re
import requests
import time

def read_txt():
  with open('./url.txt', 'r') as f:
    pool = f.read()
  pool=re.findall("https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",pool)#使用正则表达式查找订阅链接并创建列表
  # pool = pool.split()
  # print(pool,type(pool))
  return pool

def subcheck(url_list):
  status = []
  headers = {'User-Agent': 'ClashforWindows/0.18.1'}
  # 检查参数是否正确
  try:
    for url in url_list:
      # 检查链接是否可以访问
      try:
        res=requests.get(url,headers=headers,timeout=10)#设置5秒超时防止卡死
      except:
        status.append(0)
        continue
      if res.status_code == 200:
        try:
          info = res.headers['subscription-userinfo']
          info_num = re.findall('\d+',info)
          time_now=int(time.time())
          # 剩余流量大于10MB
          if int(info_num[2])-int(info_num[1])-int(info_num[0])>10485760:
            # 有时间信息
            if len(info_num) == 4:
              # 没有过期
              if time_now <= int(info_num[3]):
                status.append(1)
              # 已经过期
              else:
                status.append(0)
            # 没有时间信息
            else:
              status.append(1)
          # 流量小于10MB
          else:
            status.append(0)        
        except:
          status.append(0)   
          # output_text='无流量信息捏'
      else:
        status.append(0)
  except:
    status.append(0)
  return status

def write(url_list,status):
  with open('./url.txt', 'w') as f:
    f.write('')
  for i in range(len(url_list)):
    if status[i]==1:
      print(i)
      with open('./url.txt', 'a') as f:
        f.write(url_list[i])
        f.write('\n')

def sub(url,status):
  text = ''
  for i in range(len(status)):
    if status[i]==0:
      continue
    text = text+url[i]+'|'
  text = text.strip('|')
  return text


def init():
  pool = read_txt()
  status = subcheck(pool)
  write(pool,status)
  return status

def get_url():
  api = 'api.v1.mk'
  pool = read_txt()
  status = subcheck(pool)
  text = sub(pool,status)
  text = 'https://'+api+'/sub?target=mixed&url='+text+'&insert=false&emoji=true&list=false&udp=false&tfo=false&expand=true&scv=false&fdn=false'
  os.system('wget -O base64.txt \"%s\"'%(text))
  return text

def del_url(i):
  pool = read_txt()
  status = subcheck(pool)
  status[i] = 0
  write(pool,status)
  