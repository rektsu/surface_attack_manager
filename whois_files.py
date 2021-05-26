import os
from ipwhois import IPWhois
import socket
import ast
from pprint import pprint
import csv

def get_whois(victim, i):

    path = os.getcwd()
    with open(path + '/' + victim + '/domains.txt') as f:
       data = f.read()

    lista_datos = []
    lista_datos.extend(data)
    data_2 = eval(data)
    variable = 'www.' + str(data_2[i][0])
    print(variable)

    ip = socket.gethostbyname(variable)
    obj = IPWhois(ip)
    res = obj.lookup()

    res["nets"][0]['country']
    res["nets"][0]['abuse_emails']

    return res
