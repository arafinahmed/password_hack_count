import sys
import pwnedpasswords
import hashlib
import requests


def api_check(head):
    res = requests.get('https://api.pwnedpasswords.com/range/'+head)

    if res.status_code != 200:
        raise RuntimeError('There is a error')
    return res


def hack_count(hash, tail):
    hash = (line.split(':') for line in hash.text.splitlines())
    for h, count in hash:
        if h == tail:
            return count
    return  0




def password_check(main_password):
    hashed_password = hashlib.sha1(main_password.encode('utf-8')).hexdigest().upper()
    head, tail = hashed_password[:5], hashed_password[5:]
    res = api_check(head)
    return  hack_count(res, tail)


def main():
    for i in range(1, len(sys.argv)):
        var = password_check(sys.argv[i])
        if(var!=0):
            print(f'Your password hacked {var} time/s')
        else:
            print('Perfect password')


if __name__ == '__main__':
    main()
