''' 
MD5 Algorithm --> convert any length of input data into fixed length (128 bit = 32 character hexadecimal) of hash value
'''
# import hashlib
# inputStr = "This is a message sent by computer user."
# output = hashlib.md5(inputStr.encode())
# print(f"Hash of the input string: {output.hexdigest()}")

'''
A SHA(Secure Hash Algorithm) a cryptographic hashing algorithm - function takes input of any size and produces a fixed-length output
SHA-1 --> converts input data into a fixed 160-bit (20-byte / 40 digit hexadecimal string) hash value
SHA-2 --> SHA-256(256-bit output) -- SHA-512(512-bit output)
'''
# import hashlib
# data = "Hello, World!"
# hash_object = hashlib.sha256(data.encode())
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

'''
scrypt
scrypt is a password-based key derivation function (KDF) designed to be very hard to crack using brute force or specialized hardware.
key para --> N(Cost factor), r(Block size), p(Parallelization)
'''
# # Hashing a password with scrypt
# import hashlib
# import os
# password = "my_secure_password".encode()  # must be bytes
# salt = os.urandom(16)  # random salt (VERY important)
# # scrypt parameters
# key = hashlib.scrypt(
#     password=password,
#     salt=salt,
#     n=2**14,   # CPU/memory cost (higher = more secure, slower)
#     r=8,
#     p=1,
#     dklen=64   # length of derived key
# )
# print("Salt:", salt.hex())
# print("Hash:", key.hex())

# # Verifying a password
# import hashlib
# def verify_password(stored_salt, stored_hash, password):
#     new_hash = hashlib.scrypt(
#         password=password.encode(),
#         salt=stored_salt,
#         n=2**14,
#         r=8,
#         p=1,
#         dklen=64
#     )
#     return new_hash == stored_hash
# # Example usage
# password = "my_secure_password"
# stored_salt = salt
# stored_hash = key
# print(verify_password(stored_salt, stored_hash, password))  # True
# print(verify_password(stored_salt, stored_hash, "wrong"))   # False

'''
bcrypt
bcrypt is a password hashing function specifically designed to store passwords securely.
It's built to be slow and adaptive, which makes brute-force attacks much harder compared to fast hash functions like MD5 or SHA-256.
'''
# import bcrypt
# # Hash a password
# password = b"my_secure_password"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
# print(hashed)
# # Verify password
# if bcrypt.checkpw(password, hashed):
#     print("Password is correct")
# else:
#     print("Wrong password")
