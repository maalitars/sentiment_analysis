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

def tweedid_sõnastikku(fail):
    f = open(fail, encoding='UTF-8')
    sõnastik = defaultdict(list)

    for rida in f:
        rida = rida.strip()
        lahku = rida.split('","')  # praegu on esimesel sõnal ees jutumärk ja tweedi lõpus on üks jutumärk"
        sõnastik[lahku[1]].append(lahku[-1])
    sõnastik = sõnastik.items()
    return sõnastik

