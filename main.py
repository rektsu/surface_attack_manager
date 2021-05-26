import argparse, general, VulkaN, whois_files, time, os, csv


if __name__ == '__main__':



    parser = argparse.ArgumentParser(description='Herramienta de automatización tipo surface attack manager.')
    parser.add_argument('--target', dest='victim', help='select the victim', type=str)
    parser.add_argument('--domains', dest='domains', help='select the number of domains on which you want to get the DNS', type=int)
    parser.add_argument('--files', action='store_true', dest='files', help='select this option if you want to store the data')
    parser.add_argument('--no-files', action='store_false', dest='files', help='select this option if you dont want to store the data (default option)')
    parser.add_argument('--lists', action='store_true', dest='lists', help='select this option if you want to see the IPs on which to perform the zmap')
    parser.add_argument('--no-lists', action='store_false', dest='lists', help='select this option if you dont want to see the IPs on which to perform the zmap (default option)')
    parser.add_argument('--whois', action='store_true', dest='whois', help='select this option if you want to get more information about a certain IP and store it')
    parser.add_argument('--no-whois', action='store_false', dest='whois', help='select this option if you dont want to get more information about a certain IP or store it')
    parser.add_argument('--print-whois', action='store_true', dest='print_whois',
                        help='select this option to print more information about a certain IP and store it')
    parser.add_argument('--no-print-whois', action='store_false', dest='print_whois',
                        help='select this option if you dont want to print more information about a certain IP or store it')

    args = parser.parse_args()

    # create files
    general.create_project_dir(args.victim)

    # general.check_installations()
    nerea = VulkaN.VulkaN(args.victim, args.domains, args.files, args.lists, args.whois)


    nerea.extract_info()
    general.create_data_files(args.victim, nerea.domains_list[:args.domains], nerea.credentials_list[:args.domains], nerea.white_lists_list[:args.domains])
    print("Top", args.domains,  "domains of the victim", args.victim, ":", nerea.domains_list[:args.domains])
    print()
    print("Top", args.domains, "ips to zmap of the victim", args.victim, ":", nerea.white_lists_list[:args.domains])
    print()
    nerea.send_phising_mail()
    print("Enviado correo masivo a las credenciales extraidas")
    nerea.wake_up_server()

    '''for i in range(args.domains):
        whois = whois_files.get_whois(args.victim, i)
        whois_file = args.victim + '/whois_file_' + str(i) + '.txt'

        if not os.path.isfile(whois_file):
            try:
                with open(whois_file, 'w') as f:
                    f.write(str(whois))

            except:
                print("Couldnt open file: ", whois_file)'''

    for i in range(args.domains):
        whois = whois_files.get_whois(args.victim, i)
        whois_file = args.victim + '/whois_file' + str(i) + '.txt'

        if not os.path.isfile(whois_file):
            try:
                with open(whois_file, 'w') as f:
                    f.write(str(whois))

            except:
                print('Couldnt open file: ', whois_file)

        if args.print_whois:
            try:
                with open(whois_file, 'r') as r:
                    print(r.read())
            except FileNotFoundError as error:
                print('Error file not found: ', error)




    #nerea.white_lists_scanning()
    '''if args.lists:
        nerea.white_lists_scanning()'''
    #print(nerea)