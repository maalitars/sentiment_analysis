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
    devsonastik = defaultdict(list)
    testsonastik = defaultdict(list)
    i = 0
    for rida in f:
        i +=1
        rida = rida.strip()
        lahku = rida.split('","')
        if i <=4500:
            treenimissonastik[lahku[1]].append(lahku[-1])
        if i > 4500 and i < 4901:
            devsonastik[lahku[1]].append(lahku[-1])
        if i > 4900:
            testsonastik[lahku[1]].append(lahku[-1])
    f.close()
    return treenimissonastik, devsonastik, testsonastik

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

def sonastik_hulgaks(sagedused):
    hulk = set()
    for i in sagedused:
        for a in sagedused[i]:
            hulk.add(a[0])
    return hulk

def otsime_sagedused(sonastik, grammid):
    sagedustega = defaultdict(list)
    for i in grammid:
        for a in sonastik:
            for b in sonastik[a]:
                if b[0] == i:
                    sagedustega[a].append(b)
    return sagedustega

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

def sonastiku_muutmine(sonastik):
    kaalud(sonastik, kaalude_summa(sonastik)[0], 'yksgrammid')
    kaalud(sonastik, kaalude_summa(sonastik)[1], 'kaksgrammid')
    kaalud(sonastik, kaalude_summa(sonastik)[2], 'kolmgrammid')
    kaalud(sonastik, kaalude_summa(sonastik)[3], 'neligrammid')
    return sonastik

def yks_ngrammiks(tweet):
    yksgrammid = []
    bigrammid = []
    kolmgrammid = []
    neligrammid = []
    for i in range(len(tweet)):
        yksgrammid.append((tweet[i]))
    for i in range(len(tweet)-1):
        bigrammid.append((tweet[i], tweet[i+1]))
    for i in range(len(tweet) - 2):
        kolmgrammid.append((tweet[i], tweet[i + 1], tweet[i + 2]))
    for i in range(len(tweet) - 3):
        neligrammid.append((tweet[i], tweet[i + 1], tweet[i + 2], tweet[i+3]))
    return yksgrammid, bigrammid, kolmgrammid, neligrammid

def määramine(yks_tweet,kaal):
    summa = 0
    tweet_grammidena = yks_ngrammiks(yks_tweet)
    for a in tweet_grammidena:
        for d in a:
            for b in kaal:
                for c in kaal[b]:
                    if d in c and b == 'yksgrammid':
                        summa += 1
                    if d in c and b == 'kaksgrammid':
                        summa += 2

                    if d in c and b == 'kolmgrammid':
                        summa += 3

                    if d in c and b == 'neligramid':
                        summa += 4

    return summa
'''
def määramine(yks_tweet,kaal):
    summa = 0
    tweet_grammidena = yks_ngrammiks(yks_tweet)
    for a in tweet_grammidena:
        for d in a:
            for b in kaal:
                for c in kaal[b]:
                    if d in c:
                        summa += c[1]
    return summa

'''
def määra(väärtused):
    meeleolud=['positiivne','negatiivne','neutraalne','irrelevant']
    maksimum = max(väärtused)
    meeleolu = meeleolud[väärtused.index(maksimum)]
    väärtused.remove(maksimum)
    #if maksimum-väärtused[0] >= 1 and maksimum-väärtused[1] >= 1 and maksimum-väärtused[2] >= 1:
    return meeleolu
    #else:
    #    return '-'



def tweetide_väärtused(sonastik, i):
        väärtused =[]
        väärtused.append(määramine(sonastik[i], positiivsed_kaaludega))
        väärtused.append(määramine(sonastik[i], negatiivsed_kaaludega))
        väärtused.append(määramine(sonastik[i], neutraalse_kaaludega))
        väärtused.append(määramine(sonastik[i], irrelevant_kaaludega))
        return määra(väärtused)

treenimissonastik = tweedid_sonastikku('tweedid_segamini.txt')[0]
devsonastik = tweedid_sonastikku('tweedid_segamini.txt')[1]
testsonastik = tweedid_sonastikku('tweedid_segamini.txt')[2]

positiivsed_sonestatud = (sonesta(treenimissonastik['positive']))
negatiivsed_sonestatud = (sonesta(treenimissonastik['negative']))
neutraalsed_sonestatud = (sonesta(treenimissonastik['neutral']))
irrelevant_sonestatud = (sonesta(treenimissonastik['irrelevant']))

positiivsed_sonestatud_dev = (sonesta(devsonastik['positive']))
negatiivsed_sonestatud_dev = (sonesta(devsonastik['negative']))
neutraalsed_sonestatud_dev = (sonesta(devsonastik['neutral']))
irrelevant_sonestatud_dev = (sonesta(devsonastik['negative']))

positiivsed_sagedused = listiks(sonastikku(positiivsed_sonestatud))
negatiivsed_sagedused = listiks(sonastikku(negatiivsed_sonestatud))
neutraalsed_sagedused = listiks(sonastikku(neutraalsed_sonestatud))
irrelevant_sagedused = listiks(sonastikku(irrelevant_sonestatud))

positiivsed_hulk = (sonastik_hulgaks(positiivsed_sagedused))
negatiivsed_hulk = (sonastik_hulgaks(negatiivsed_sagedused))
neutraalsed_hulk = (sonastik_hulgaks(neutraalsed_sagedused))
irrelevant_hulk = (sonastik_hulgaks(irrelevant_sagedused))

positiivsed = ((positiivsed_hulk -negatiivsed_hulk) - neutraalsed_hulk) - irrelevant_hulk
negatiivsed = ((negatiivsed_hulk -positiivsed_hulk) - neutraalsed_hulk) - irrelevant_hulk
neutraalsed = ((neutraalsed_hulk- negatiivsed_hulk)-positiivsed_hulk)- irrelevant_hulk
irrelevant = ((irrelevant_hulk- negatiivsed_hulk)- positiivsed_hulk)- neutraalsed_hulk

positiivsed = otsime_sagedused(positiivsed_sagedused,positiivsed)
negatiivsed = otsime_sagedused(negatiivsed_sagedused,negatiivsed)
neutraalsed = otsime_sagedused(neutraalsed_sagedused,neutraalsed)
irrelevant = otsime_sagedused(irrelevant_sagedused, irrelevant)

positiivsed_kaaludega = sonastiku_muutmine(positiivsed)
negatiivsed_kaaludega = sonastiku_muutmine(negatiivsed)
neutraalse_kaaludega = sonastiku_muutmine(neutraalsed)
irrelevant_kaaludega = sonastiku_muutmine(irrelevant)

#print('peaksid olema positiivsed')
#(tweetide_väärtused(positiivsed_sonestatud_dev))
#print('\n')
#print('peaksid olema negatiivsed')

#(tweetide_väärtused(negatiivsed_sonestatud_dev))
#print('\n')
#print('peaksid olema neutraalsed')
def silumine(yks_tweet,kaal):
    tweet_grammidena = yks_ngrammiks(yks_tweet)
    for a in tweet_grammidena:
        for d in a:
            for b in kaal:
                for c in kaal[b]:
                    if d in c:
                        print(kaal[b])
    return kaal
for i in range(len(neutraalsed_sonestatud_dev)):
     määratud = (tweetide_väärtused(neutraalsed_sonestatud_dev,i))
     if määratud != 'neutraalne' and määratud != '-':
         uus_sonastik = silumine(neutraalsed_sonestatud_dev[i], neutraalse_kaaludega)

         (neutraalsed_sonestatud_dev[i])
#print('\n')
#print('peaksid olema irrelevant')
#(tweetide_väärtused(irrelevant_sonestatud_dev))