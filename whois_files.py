import os
from ipwhois import IPWhois
import socket
import ast
from pprint import pprint
import csv


'''def get_whois(victim, i):
    path = os.getcwd()
    name = path + '/' + victim + '/whois_file' + str(i) + '.txt'
    try:
        c = csv.writer(name, 'wb')
    except Exception as error:
        print('Error in output file', error)
    else:
        c.writerow(['IP Adress', 'Country', 'State', 'City', 'Description', 'Name', 'Emails', 'Range'])



    try:
        with open(path + '/' + victim + '/domains.txt') as f:
            data = f.read()

        lista_datos = []
        lista_datos.extend(data)
        data_2 = eval(data)
        variable = 'www.' + str(data_2[i][0])

        ip = socket.gethostbyname(variable)
        obj = IPWhois(ip)
        out = obj.lookup()

        f = out['nets'][0]['city']
        a = out['nets'][0]['country']
        g = out['nets'][0]['description']
        b = out['nets'][0]['abuse_emails']
        h = out['nets'][0]['name']
        ranges = out['nets'][0]['range']
        e = out['nets'][0]['state']

        c.writerow([ip, a, e, f, g, h, b, ranges])

    except Exception as error_content:
        print('Error in content section: ', error_content)'''



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