import hashlib


def hashit(s):
    if type(s) == list:
        s = '_'.join(s)
    return hashlib.sha1(s.encode('utf-8')).hexdigest()
