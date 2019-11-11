from Crypto.Cipher import AES
import hashlib
import codecs

bytesToDecrypt = bytes.fromhex('71127f3c3a34f552aef16949a0e57c6f44d6b899ecaad141d36a7c8b2501bc6e')
key = bytes.fromhex('bcf6e16f4ddd3fad8a0b263aed73b7d6')
skey = hashlib.pbkdf2_hmac(
        hash_name = 'sha256',
        password = key,
        salt = bytesToDecrypt,
        iterations = 10000,
        dklen = 32)
cipher = AES.new(skey, AES.MODE_ECB)
out_bytes = cipher.decrypt(key)
print(out_bytes.hex())
