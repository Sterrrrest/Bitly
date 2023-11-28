import requests


import argparse


import os
from dotenv import load_dotenv, find_dotenv

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
    parser = argparse.ArgumentParser(description='cut links')
    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    link = args.link
    load_dotenv(find_dotenv())
    token = os.environ['BITLY_TOKEN']
    if is_bitlink(token, link):
        try:
            print('Количество кликов:', count_clicks(token, link))
        except requests.exceptions.HTTPError:
            print("Количество кликов недоступно: неверная ссылка")
    else:
        try:
            print('Битлинк', shorten_link(token, link))
        except requests.exceptions.HTTPError:
            print('Битлинк: Неверная ссылка')



