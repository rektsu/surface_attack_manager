# Deprecated project
# IPV4INFO AND PWNDB SHUTTED DOWN

# surface attack manager
PoC of a web scrapping based tool that provides bunch of information from an organization by scraping http://ipv4info.com, retrieving most used domains, white lists from an organization and runing a whois scan type in those domains retrieved.

# Purpose on a red team exercise

The idea of this tool is to scrap the N (user input) most used domains from an organization, run pwndb on those domains to get filtered credentials. Then perform a credential stuffing or a password spraying attack to the organization

# Installation
git clone https://github.com/rektsu/surface_attack_manager.git

# Example of use
Being in the same directory you've cloned the repository, access surface_attack_manager: ../../../surface_attack_manager

python3 main.py -h
![image](https://user-images.githubusercontent.com/15212130/119590174-8bbbf700-bdd4-11eb-8f70-07fcd4817748.png)


python3 main.py --target bbva --domains 5 --no-files --no-lists --whois --print-whois
![image](https://user-images.githubusercontent.com/15212130/119590216-9bd3d680-bdd4-11eb-8fba-1cfba1eb5b59.png)

![image](https://user-images.githubusercontent.com/15212130/119590238-a5f5d500-bdd4-11eb-98d1-b654d84aff38.png)
