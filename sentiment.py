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


from collections import defaultdict,Counter
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

def tweedid_sonastikku(fail):
    f = open(fail,encoding='UTF-8')
    treenimissonastik = defaultdict(list)
    i = 0
    for rida in f:
        i +=1
        if i == 4501:
            break
        rida = rida.strip()
        lahku = rida.split('","')  # praegu on esimesel sõnal ees jutumärk ja tweedi lõpus on üks jutumärk"
        treenimissonastik[lahku[1]].append(lahku[-1])
    f.close()
    return treenimissonastik

def sagedus (sonastik, meeleolu): #meeleolud: positive, negative, irrelevant, neutral
    meeleolu = len(sonastik[meeleolu])
    return meeleolu

def sonesta(tweedid):
    sonestatud = []
    for i in tweedid:
        sonestatud.append(i.split(' ')[:-1])
    return sonestatud

def ngrammid(tweet):
    yksgrammid = []
    bigrammid = []
    kolmgrammid = []
    neligrammid = []
    for a in range(len(tweet)):
        for i in range(len(tweet[a])):
            yksgrammid.append((tweet[a][i]))
        for i in range(len(tweet[a])-1):
            bigrammid.append((tweet[a][i], tweet[a][i+1]))
        for i in range(len(tweet[a]) - 2):
            kolmgrammid.append((tweet[a][i], tweet[a][i + 1], tweet[a][i + 2]))
        for i in range(len(tweet[a]) - 3):
            neligrammid.append((tweet[a][i], tweet[a][i + 1], tweet[a][i + 2], tweet[a][i+3]))
    return yksgrammid, bigrammid, kolmgrammid, neligrammid

treenimissonastik = tweedid_sonastikku('tweedid_segamini.txt')
positiivsed_sonestatud = (sonesta(treenimissonastik['positive']))
negatiivsed_sonestatud = (sonesta(treenimissonastik['negative']))
neutraalsed_sonestatud = (sonesta(treenimissonastik['neutral']))
irrelevant_sonestatud = (sonesta(treenimissonastik['irrelevant']))

def sonastikku(meeleolu):
    sonastik = defaultdict(list)
    sonastik['yksgrammid'] = Counter(ngrammid(meeleolu)[0]).most_common(50)
    sonastik['kaksgrammid'] = Counter(ngrammid(meeleolu)[1]).most_common(50)
    sonastik['kolmgrammid'] = Counter(ngrammid(meeleolu)[2]).most_common(20)
    sonastik['neligrammid'] = Counter(ngrammid(meeleolu)[3]).most_common(10)
    return  sonastik
positiivsed_sagedused = sonastikku(positiivsed_sonestatud)
negatiivsed_sagedused = sonastikku(negatiivsed_sonestatud)
neutraalsed_sagedused = sonastikku(neutraalsed_sonestatud)
irrelevant_sagedused = sonastikku(irrelevant_sonestatud)

#teha unikaalsed
