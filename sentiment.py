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
    sonastik['yksgrammid'] = list(Counter(ngrammid(meeleolu)[0]).most_common(50))
    sonastik['kaksgrammid'] = list(Counter(ngrammid(meeleolu)[1]).most_common(50))
    sonastik['kolmgrammid'] = list(Counter(ngrammid(meeleolu)[2]).most_common(20))
    sonastik['neligrammid'] = list(Counter(ngrammid(meeleolu)[3]).most_common(10))
    return  sonastik
def listiks (sagedustega_ennikud):
    sonastik = defaultdict(list)

    for i in sagedustega_ennikud:
        for a in sagedustega_ennikud[i]:
            sonastik[i].append(list(a))
    return sonastik
positiivsed_sagedused = listiks(sonastikku(positiivsed_sonestatud))
negatiivsed_sagedused = listiks(sonastikku(negatiivsed_sonestatud))
neutraalsed_sagedused = listiks(sonastikku(neutraalsed_sonestatud))
irrelevant_sagedused = listiks(sonastikku(irrelevant_sonestatud))

def sonastik_hulgaks(sagedused):
    hulk = set()
    for i in sagedused:
        for a in sagedused[i]:
            hulk.add(a[0])
    return hulk

positiivsed_hulk = (sonastik_hulgaks(positiivsed_sagedused))
negatiivsed_hulk = (sonastik_hulgaks(negatiivsed_sagedused))
neutraalsed_hulk = (sonastik_hulgaks(neutraalsed_sagedused))
irrelevant_hulk = (sonastik_hulgaks(irrelevant_sagedused))

positiivsed = ((positiivsed_hulk -negatiivsed_hulk) - neutraalsed_hulk) - irrelevant_hulk
negatiivsed = ((negatiivsed_hulk -positiivsed_hulk) - neutraalsed_hulk) - irrelevant_hulk
neutraalsed = ((neutraalsed_hulk- negatiivsed_hulk)-positiivsed_hulk)- irrelevant_hulk
irrelevant = ((irrelevant_hulk- negatiivsed_hulk)- positiivsed_hulk)-neutraalsed_hulk
def otsime_sagedused(sonastik, grammid):
    sagedustega = defaultdict(list)
    for i in grammid:
        for a in sonastik:
            for b in sonastik[a]:
                if b[0] == i:
                    sagedustega[a].append(b)
    return sagedustega

positiivsed = otsime_sagedused(positiivsed_sagedused,positiivsed)
negatiivsed = otsime_sagedused(negatiivsed_sagedused,negatiivsed)
neutraalsed = otsime_sagedused(neutraalsed_sagedused,neutraalsed)
irrelevant = otsime_sagedused(irrelevant_sagedused, irrelevant)

#liidame kokku ja siis võtame for i ja jagame sellega selle summaga kõik...
def kaalude_summa(unikaalsed_sonastik):
    summa_1 = 0
    summa_2 = 0
    summa_3 = 0
    summa_4 = 0
    for i in unikaalsed_sonastik['yksgrammid']:
        summa_1 += i[1]
    for i in unikaalsed_sonastik['kaksgrammid']:
        summa_2 += i[1]
    for i in unikaalsed_sonastik['kolmgrammid']:
        summa_3 += i[1]
    for i in unikaalsed_sonastik['neligrammid']:
        summa_4 += i[1]
    return summa_1,summa_2,summa_3,summa_4
def kaalud (unikaalsed_sonastik, summa, gramm):
    for i in unikaalsed_sonastik[gramm]:
        sõna = i[0]
        kaal = round(i[1]/summa,2)
        i[1] = kaal

    return unikaalsed_sonastik

kaalud(positiivsed, kaalude_summa(positiivsed)[0],'yksgrammid')
kaalud(positiivsed, kaalude_summa(positiivsed)[1],'kaksgrammid')
kaalud(positiivsed, kaalude_summa(positiivsed)[2],'kolmgrammid')
kaalud(positiivsed, kaalude_summa(positiivsed)[3],'neligrammid')
print(positiivsed)
