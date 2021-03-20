from time import time, sleep
def meter(f):
    def wr(*a, **kw):
        t1 = time()
        res = f(*a, **kw)
        t2 = time()
        print(t2 - t1)
        return res
    return wr


encryptedMessage = 'wwaldaadicffenn'
@meter
def decryption(s):
    sleep(1)
    symbolArr = list(s)
    for i in range(len(symbolArr) - 1):
        while i < len(symbolArr):
            if i + 1 == len(symbolArr):
                return ''.join(symbolArr)
            if symbolArr[i] == symbolArr[i + 1]:
                del symbolArr[i]
                del symbolArr[i]
                i -= 1
                
            else:
                break
    return ''.join(symbolArr)


resultNew = decryption(encryptedMessage)
print(resultNew)
