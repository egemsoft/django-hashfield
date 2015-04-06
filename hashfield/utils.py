import hashlib


hashit = lambda s: hashlib.sha1(s.encode('utf-8')).hexdigest()
