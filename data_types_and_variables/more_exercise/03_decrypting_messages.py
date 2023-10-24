key = int(input())
n = int(input())
decrypted_message = ""
for i in range(n):
    message = ord(input())
    decrypted = chr(message + key)
    decrypted_message += decrypted
print(decrypted_message)