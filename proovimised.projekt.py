def sõna_tüübid(sõnad):
    return dict([(sõna, True)for sõna in sõnad])

def sõna_tüübid(sõnad):
    sõnastik = {}
    for sõna in sõnad:
         sõnastik[sõna] = True
    return sõnastik

#Feature extraction method
#Antud funktsioonid toodavad mõlemad sama vastuse.
#print(sõna_tüübid("mulle meeldivad maasikad"))
#see näide on tehtud selle lehe järgi: http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
