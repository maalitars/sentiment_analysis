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
"""def sagedus (sonastik, meeleolu): #meeleolud: positive, negative, irrelevant, neutral
    meeleolu = len(sonastik[meeleolu])
    return meeleolu"""
def sonesta(sonastik_võtmega):
    sonestatud = []
    for i in sonastik_võtmega:
        sonestatud.append(i.split(' ')[:-1])
    return sonestatud
def ngrammid(meeleolu_sonestatud):
    yksgrammid = []
    bigrammid = []
    kolmgrammid = []
    neligrammid = []
    for a in range(len(meeleolu_sonestatud)):
        for i in range(len(meeleolu_sonestatud[a])):
            yksgrammid.append((meeleolu_sonestatud[a][i]))
        for i in range(len(meeleolu_sonestatud[a])-1):
            bigrammid.append((meeleolu_sonestatud[a][i], meeleolu_sonestatud[a][i+1]))
        for i in range(len(meeleolu_sonestatud[a]) - 2):
            kolmgrammid.append((meeleolu_sonestatud[a][i], meeleolu_sonestatud[a][i + 1], meeleolu_sonestatud[a][i + 2]))
        for i in range(len(meeleolu_sonestatud[a]) - 3):
            neligrammid.append((meeleolu_sonestatud[a][i], meeleolu_sonestatud[a][i + 1], meeleolu_sonestatud[a][i + 2], meeleolu_sonestatud[a][i+3]))
    return yksgrammid, bigrammid, kolmgrammid, neligrammid
def sonastikku(meeleolu_sonestatud):
    sonastik = defaultdict(list)
    sonastik['yksgrammid'] = list(Counter(ngrammid(meeleolu_sonestatud)[0]).most_common(50))
    sonastik['kaksgrammid'] = list(Counter(ngrammid(meeleolu_sonestatud)[1]).most_common(50))
    sonastik['kolmgrammid'] = list(Counter(ngrammid(meeleolu_sonestatud)[2]).most_common(20))
    sonastik['neligrammid'] = list(Counter(ngrammid(meeleolu_sonestatud)[3]).most_common(10))
    return  sonastik
def listiks (sagedustega_ennikud_meeleolu):
    sonastik = defaultdict(list)
    for i in sagedustega_ennikud_meeleolu:
        for a in sagedustega_ennikud_meeleolu[i]:
            sonastik[i].append(list(a))
    return sonastik
def sonastik_hulgaks(meeleolu_sagedused):
    hulk = set()
    for i in meeleolu_sagedused:
        for a in meeleolu_sagedused[i]:
            hulk.add(a[0])
    return hulk
def otsime_sagedused(meeleolu_sagedused, meeleolu_unikaalne_hulk):
    sagedustega = defaultdict(list)
    for i in meeleolu_unikaalne_hulk:
        for a in meeleolu_sagedused:
            for b in meeleolu_sagedused[a]:
                if b[0] == i:
                    sagedustega[a].append(b)
    return sagedustega
'''def kaalude_summa(unikaalsed_sonastik):
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
        #sõna = i[0]
        kaal = round(i[1]/summa,2)
        i[1] = kaal
    return unikaalsed_sonastik'''
def kaalud (unikaalsed_sonastik): #summa, gramm):
    for i in unikaalsed_sonastik['yksgrammid']:
        i[1] = 1
    for i in unikaalsed_sonastik['kaksgrammid']:
        i[1] = 2
    for i in unikaalsed_sonastik['kolmgrammid']:
        i[1] = 3
    for i in unikaalsed_sonastik['neligrammid']:
        i[1] = 4
    return unikaalsed_sonastik
'''def sonastiku_muutmine(sonastik):
    kaalud(sonastik, kaalude_summa(sonastik)[0], 'yksgrammid')
    kaalud(sonastik, kaalude_summa(sonastik)[1], 'kaksgrammid')
    kaalud(sonastik, kaalude_summa(sonastik)[2], 'kolmgrammid')
    kaalud(sonastik, kaalude_summa(sonastik)[3], 'neligrammid')
    return sonastik'''
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
                        summa += c[1]
                    if d in c and b == 'kaksgrammid':
                        summa += c[1]
                    if d in c and b == 'kolmgrammid':
                        summa += c[1]
                    if d in c and b == 'neligramid':
                        summa += c[1]

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
    if väärtused == [0,0,0,0]: return 'Meie parameetritega seda lauset kahjuks määrata ei saa.' #kui oleks väärtuste list[0,5,5,3]?
    #väärtused.remove(maksimum)
    #if maksimum-väärtused[0] >= 1 and maksimum-väärtused[1] >= 1 and maksimum-väärtused[2] >= 1:
    else: return meeleolu
    #else:
    #    return '-'
def tweetide_väärtused(sonestatud_tweedid, i):
    väärtused =[]
    väärtused.append(määramine(sonestatud_tweedid[i], positiivsed))
    väärtused.append(määramine(sonestatud_tweedid[i], negatiivsed))
    väärtused.append(määramine(sonestatud_tweedid[i], neutraalsed))
    väärtused.append(määramine(sonestatud_tweedid[i], irrelevant))
    return määra(väärtused)
def sagedaseim_vale_gramm(valesti_tweedid):
    k = 0
    vale_tweedi_gramm = ''
    for i in valesti_tweedid:
        ngramm = valesti_tweedid.count(i)
        if ngramm > k:
            k = ngramm
            vale_tweedi_gramm = i
    return vale_tweedi_gramm
def moju_suurendamine(õigesti_määratud_tweet,sonastik_grammidega):
    tweet_grammidena = yks_ngrammiks(õigesti_määratud_tweet)
    for a in tweet_grammidena:
        for d in a:
            for b in sonastik_grammidega:
                for c in sonastik_grammidega[b]:
                    if d in c:
                        c[1] +=0.5
    return sonastik_grammidega
def valed_tweedid(meeleolu_sonastatud_dev, meeleolu):
    valesti_tweedid = []
    for i in range(len(meeleolu_sonastatud_dev)):
        määratud = tweetide_väärtused(meeleolu_sonastatud_dev,i)
        if määratud != meeleolu:
            valesti = yks_ngrammiks(meeleolu_sonastatud_dev[i])
            for a in valesti:
                for i in range(len(a)):
                    valesti_tweedid.append(a[i])
    return valesti_tweedid

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

#positiivsed_kaaludega = sonastiku_muutmine(positiivsed)
#negatiivsed_kaaludega = sonastiku_muutmine(negatiivsed)
#neutraalse_kaaludega = sonastiku_muutmine(neutraalsed)
#irrelevant_kaaludega = sonastiku_muutmine(irrelevant)

positiivsed = kaalud(positiivsed)
negatiivsed = kaalud(negatiivsed)
neutraalsed = kaalud(neutraalsed)
irrelevant = kaalud(irrelevant)

def valede_tweetide_eemaldamine(meeleolu_sonestatud_dev, meeleolu, meeleolu_sonastik):
    all_tweets = valed_tweedid(meeleolu_sonestatud_dev,meeleolu)
    valede_tweetide_grammid = []
    for gramm in all_tweets:
        for voti in meeleolu_sonastik:
            for element in meeleolu_sonastik[voti]:
                if gramm in element:
                    valede_tweetide_grammid.append(gramm)
    return valede_tweetide_grammid


def most_common(list_ngrammidega):
    a = 0

    for element in list_ngrammidega:
        mitu = list_ngrammidega.count(element)
        if mitu > a:
            a = mitu
            enim = element
    try:
        list_ngrammidega.remove(enim)
    except:
        return
    return enim

def eemaldamine(meeleolu_element,sonastik_grammidega):
        for voti in sonastik_grammidega:
            for a in sonastik_grammidega[voti]:
                if meeleolu_element in a :
                    sonastik_grammidega[voti].remove(a)

        return sonastik_grammidega


def silumine(meeleolu_sonastatud_dev, meeleolu):
    if meeleolu != 'positiivne':
        s = most_common(valede_tweetide_eemaldamine(meeleolu_sonastatud_dev, meeleolu, positiivsed))
        eemaldamine(s,positiivsed)
    if meeleolu != 'negatiivne':
        s = most_common(valede_tweetide_eemaldamine(meeleolu_sonastatud_dev, meeleolu, negatiivsed))
        eemaldamine(s,negatiivsed)
    if meeleolu != 'neutraalne':
        s = most_common(valede_tweetide_eemaldamine(meeleolu_sonastatud_dev, meeleolu, neutraalsed))
        eemaldamine(s,neutraalsed)
    if meeleolu != 'irrelevant':
        s = most_common(valede_tweetide_eemaldamine(meeleolu_sonastatud_dev, meeleolu, irrelevant))

        eemaldamine(s,irrelevant)
    return meeleolu_sonastatud_dev

def maaramine(meeleolu_sonastatud_dev, meeleolu):
    for i in range(5):
        a= 0
        for i in range(len(meeleolu_sonastatud_dev)):
            määratud = tweetide_väärtused(meeleolu_sonastatud_dev, i)
            if määratud != meeleolu and määratud != 'Meie parameetritega seda lauset kahjuks määrata ei saa.':
                a +=1
        print('Valesti, ',a, 'väljaarvatud need, mida ei oska ta määrata')
        silumine(meeleolu_sonastatud_dev, meeleolu)
print('positiivsed 5 korda silutud')
maaramine(positiivsed_sonestatud_dev, 'positiivne')
print('negatiivsed 5 korda silutud')

maaramine(negatiivsed_sonestatud_dev, ' negatiivsed')
print('neutraalsed 5 korda silutud')

maaramine(neutraalsed_sonestatud_dev, ' neutraalsed')
print('irrelevandid 5 korda silutud')

maaramine(irrelevant_sonestatud_dev, ' irrelevant')
