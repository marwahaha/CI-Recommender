import collections
import math


def TFIDF(documents):
    """Calculates the TFIDF score for every document's terms.

    Keyword arguments:
    documents -- the documentent dictionary {id: document}

    Returns -- dict: {id: {term: score}}

    """
    tfdict = {}
    dfdict = collections.defaultdict(int)
    for pmid, document in documents.iteritems():
        if(len(document) == 0):
            continue

        words = document.split()

        tfdict[pmid] = TF(words)
        #combining this loop for some df as well
        for word in set(words):
            dfdict[word] += 1

    tfidfdict = {}
    idfdict = IDF(dfdict, len(documents))
    for pmid, tf in tfdict.iteritems():
        tfidfdict[pmid] = {term: (count * idfdict[term]) for term, count in tf}

    return tfidfdict

def TF(termList):
    """Calculates the TF score for every word in the given list.
    Uses adaptive TF, every word with its normalized value for max term, TFid = (fid / maxk fkd).
    TF of word i in document d is that divided by the frequency of word k where k is the most common term in d

    Keyword arguments:
    termList -- the list of terms

    Returns -- list: [(term, score)]

    """
    #use counter collection to get term frequency for all terms, sort on most_common, get tmax and calculate scores
    tfrequency = collections.Counter(termList).most_common()
    tmax = tfrequency[0][1]

    return [(f[0], float(f[1])/tmax) for f in tfrequency]

def IDF(dfTermsDict, documentN):
    """Calculates the IDF score for every term in the document frequency dictionary.

    Keyword arguments:
    dfTermsDict -- the dictionary {term: inNdocuments} (e.g. "Space" occurred in 10 documents)
    documentN -- the amount of documents to divide the document frequency by

    Returns -- dict: {term: score}

    """
    idfdict = {}
    for term, df in dfTermsDict.iteritems():
        idfdict[term] = math.log(documentN/df, 2)

    return idfdict
