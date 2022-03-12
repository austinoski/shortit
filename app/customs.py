import hashlib, time


def generate_unique_key(url, user: object="Guest"):
    '''Takes a url and optional user object
        Return 8 characters slice of an md5 encoded string
    '''
    hashed_str = str(hash(str(url)+str(user)+str(time.time())))
    md5_encoded_str = hashlib.md5(hashed_str.encode()).hexdigest()
    key = md5_encoded_str[:8]
    return key
