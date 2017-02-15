import math


def tf(word, blob):
    '''
        Term frequency: number of times a word appears in document
    '''
    return blob.count(word) / len(blob)


def n_containing(word, bloblist):
    '''
        Return a number of documents containing word
    '''
    print ('n containing')
    return sum(1 for blob in bloblist if word in blob)


def idf(word, bloblist):
    '''
        Inverse document frequency
    '''
    print ('bloblist', len(bloblist))
    print (1 + n_containing(word, bloblist))
    print ('pass', float(len(bloblist) / (1 + n_containing(word, bloblist))))
    return math.log(float(len(bloblist) / (1 + n_containing(word, bloblist))))


def tfidf(word, blob, bloblist):
    '''
        Compute the TF-IDF score
    '''
    print ('tf', tf(word, blob))
    print ('idf', idf(word, bloblist))
    print ('producto', tf(word, blob) * idf(word, bloblist))

    return tf(word, blob) * idf(word, bloblist)
