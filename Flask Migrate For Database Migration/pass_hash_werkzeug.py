from werkzeug.security import generate_password_hash, check_password_hash

password= 'mysecretpassword'

hashed_password = generate_password_hash(password)
print(hashed_password)

check_password= check_password_hash(hashed_password,'mysecretpassword')
print(check_password)