from collections import defaultdict

def loe_korpus(algkaust):
    tweedid = []
    ###for i in algkaust:
    ###     if i.isfile:
    ###         puhastatud = puhasta(i.read())
    ###         tweedid.append(puhastatud)
    return tweedid

def sonesta(tweedid):
    sonestatud = []
    ##for i in tweedid:
    ##      sonestatud.append(sõnesta i)
    ##
    return sonestatud

def leia_sagedused(treening_korpus):
    sagedused = defaultdict(int)
    #treeningkorpus on list, mis sisaldab endas sõnestatud
    #tweete, mis on samuti listi kujul, ehk kokkuvõttes on meil
    #listide list.
    return sagedused

def leia_enim_unikaalsed(sagedused):
    unikaalsed = []
    return unikaalsed

def silumine():

    return None


def testimine():

    return None

def main():

    print("jou")


from collections import defaultdict
from random import shuffle

def fail_segamini(fail):
    f = open(fail,encoding='UTF-8')
    read = []
    for rida in f:
        read.append(rida)
    shuffle(read)
    g = open('tweedid_segamini.txt', 'w', encoding='UTF8')
    for i in read:
        g.write(i)
    return

def tweedid_sõnastikku(fail):
    f = open(fail,encoding='UTF-8')
    treenimissõnastik = defaultdict(list)
    i = 0
    for rida in f:
        i +=1
        if i == 4501:
            break
        rida = rida.strip()
        lahku = rida.split('","')  # praegu on esimesel sõnal ees jutumärk ja tweedi lõpus on üks jutumärk"
        treenimissõnastik[lahku[1]].append(lahku[-1])
    f.close()
    #treenimissõnastik = treenimissõnastik.items()
    return treenimissõnastik

treenimissõnastik = tweedid_sõnastikku('tweedid_segamini.txt')

def sagedus (sõnastik, meeleolu):
    meeleolu = len(sõnastik[meeleolu])
    return meeleolu
print(sagedus(treenimissõnastik, 'positive'))
print(sagedus(treenimissõnastik, 'negative'))
print(sagedus(treenimissõnastik, 'irrelevant'))
print(sagedus(treenimissõnastik, 'neutral'))


#võtmed eraldi(4)
#def tweet_sõneks(võti):
   # return

