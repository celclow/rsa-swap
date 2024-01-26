import os
import sys

from Crypto.PublicKey import RSA

input_path = os.path.abspath(sys.argv[1])
input_key = RSA.import_key(open(input_path, "rb").read())
swap_key = RSA.construct((input_key.n, input_key.d, input_key.e))  # swap e for d

print(swap_key.export_key("PEM").decode())
