from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from twilio.rest import Client

# load data
with open('ciphertext.bin', 'rb') as f:
    iv = f.read(16)  # AES block size is 16 bytes
    ciphertext = f.read()

# load key
with open('key.bin', 'rb') as f:
    key = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # creating a new AES cipher with the saved key and IV
data = unpad(cipher.decrypt(ciphertext), AES.block_size)  # decrypting the data

# save decrypted data
with open('decrypted.txt', 'wb') as f:
    f.write(data)

# Twilio credentials
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Alert! Decryption of a file is done!',
    from_='XXXXXXXXXXXXXXXXXXXXX',
    to='XXXXXXXXXXXXXXXXXXXXXXXX'
)
