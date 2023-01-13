from decouple import config

print("Hello World")
USER = config('user1')
PASSWORD = config('password')

print(USER)
print(PASSWORD)