import hashlib
import time

a=input()
hash_object=(hashlib.sha256(str(a).encode()))
print("Hash of input string is: ",hash_object.hexdigest())

target='0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

sol=False
hex_val_a=int(hash_object.hexdigest(),16)
nonce_val=0

initial=time.time()
while not sol:
    string_with_added_nonce=hex_val_a+nonce_val
    hash_1=hashlib.sha256(hex(string_with_added_nonce).encode()).hexdigest()
    hash_2=hashlib.sha256(hash_1.encode()).hexdigest()
    print("The Nonce is: " + str(nonce_val))
    print('Hash of block with appended nonce is: ',hash_2)

    print('Is the new block hash less than the target? ')
    sol=int(hash_2, 16) < int(target, 16)
    print(sol)

    if not sol:
        nonce_val += 1

initial2=time.time()
print("Time taken to find this nonce value is : ",initial2-initial)



