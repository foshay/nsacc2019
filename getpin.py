import hashlib

checkpin = hex(0x71127f3c3a34f552aef16949a0e57c6f44d6b899ecaad141d36a7c8b2501bc6e)
print(checkpin)
for x in range(999999):
    m = hashlib.sha256(str(x).encode())
    if str("0x" + m.hexdigest()) == str(checkpin):
        print(x)
        break
