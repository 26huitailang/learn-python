import hashlib
import sys

def hash_file(filename):

    sha_obj = hashlib.sha1()
    with open(filename, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(512)
            sha_obj.update(chunk)

    return sha_obj.hexdigest()

if __name__ == '__main__':
    hash_msg = hash_file(sys.argv[1])
    print(hash_msg)

