import Crypto.PublicKey.RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA


class RSA:
    def __init__(self):
        super().__init__()

    @staticmethod
    def GenerateSKPK():
        rsa = Crypto.PublicKey.RSA.generate(1024)
        sk = rsa.export_key()
        pk = rsa.publickey().export_key()
        return sk, pk

    @staticmethod
    def Cipher(sk, content):
        sk = Crypto.PublicKey.RSA.importKey(sk)
        cipher = PKCS1_v1_5.new(sk)
        sha = SHA.new()
        sha.update(content.encode())
        ciphered = cipher.sign(sha)
        return ciphered

    @staticmethod
    def Decipher(pk, content, ciphered):
        pk = Crypto.PublicKey.RSA.importKey(pk)
        decipher = PKCS1_v1_5.new(pk)
        sha = SHA.new()
        sha.update(content.encode())
        isverify = decipher.verify(sha, ciphered)
        return isverify


if __name__ == '__main__':
    sk, pk = RSA.GenerateSKPK()
    # print(sk, pk)
    content = "hello world"
    ciphered = RSA.Cipher(sk, content)
    deciphered = RSA.Decipher(pk,  content, ciphered)
    print(deciphered)
