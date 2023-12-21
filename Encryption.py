from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from twilio.rest import Client


with open('plaintext.txt', 'rb') as f:
    data = f.read()

key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
cipher = AES.new(key, AES.MODE_CBC)  # creating a new AES cipher
ciphertext = cipher.encrypt(pad(data, AES.block_size))  # encrypting the data

with open('ciphertext.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphertext)

with open('key.bin', 'wb') as f:
    f.write(key)

# Twilio credentials
account_sid = 'AC4223245fa22dd66e3eab7b71e9d034ee'
auth_token = '66dc0f5b261c4cb5ae102652249050fc'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Alert! A file has been encrypted!',
    from_='+1 361 264 4011',
    to='+1 504 338 1970'
)
