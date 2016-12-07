f = open('tweedid.txt',encoding='UTF-8')
for rida in f:
    rida.strip()
    lahku = rida.split('","') #praegu on esimesel sõnal ees jutumärk ja tweedi lõpus on üks jutumärk"
    print(lahku)
