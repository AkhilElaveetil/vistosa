from _sha256 import sha256


def get_sha_hash(word):
    hashed_word = sha256(word.encode()).hexdigest()
    return hashed_word
