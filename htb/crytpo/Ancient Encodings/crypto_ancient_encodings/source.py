from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64encode, b64decode
from binascii import unhexlify

# FLAG = b"HTB{??????????}"


# def encode(message):
#     return hex(bytes_to_long(b64encode(message)))


# def main():
#     encoded_flag = encode(FLAG)
#     with open("output.txt", "w") as f:
#         f.write(encoded_flag)


# if __name__ == "__main__":
#     main()

encrytped = "53465243657a467558336b7764584a66616a4231636d347a655639354d48566664326b786246397a5a544e66644767784e56396c626d4d775a4446755a334e665a58597a636e6c33614756794d33303d"

print(unhexlify(encrytped))

t = 'SFRCezFuX3kwdXJfajB1cm4zeV95MHVfd2kxbF9zZTNfdGgxNV9lbmMwZDFuZ3NfZXYzcnl3aGVyM30='
print(b64decode(t))