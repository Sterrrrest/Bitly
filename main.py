import requests


import os


from dotenv import load_dotenv, find_dotenv


import argparse


parser = argparse.ArgumentParser(description='cut links')
parser.add_argument('link', help='Ссылка')
args = parser.parse_args()
print(args.link)
link = args.link


def shorten_link(token, link):  
  url = 'https://api-ssl.bitly.com/v4/shorten'
  headers = {'Authorization': token}
  payLoad = {'long_url': link}
  response = requests.post(url, json=payLoad, headers=headers)
  response.raise_for_status()
  bitlink = response.json()['id']
  return bitlink
  

def count_clicks(token, bitlink):  
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    count_clicks = response.json()['total_clicks']
    return count_clicks
  

def is_bitlink(token,link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'.format(bitlink=link)
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    return response.ok
        
 
if __name__ == "__main__":
    load_dotenv(find_dotenv())
    token = os.environ['BITLY_TOKEN']
    # print('Insert the link')
    # link = input()
    if is_bitlink(token, link):
      try:
        print('Количество кликов:', count_clicks(token, link))
      except requests.exceptions.HTTPError:
        print("Количество кликов недоступно: неверная ссылка")


    if not is_bitlink(token, link):
      try:
        print('Битлинк', shorten_link(token, link))
      except requests.exceptions.HTTPError:
        print('Битлинк: Неверная ссылка')