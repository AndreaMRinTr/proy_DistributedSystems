from passlib.hash import bcrypt_sha256

def hash_password(password):
    hashed_password = bcrypt_sha256.hash(password)
    return hashed_password

def verify_password(password, hashed_password):
    return bcrypt_sha256.verify(password, hashed_password)

# Ejemplo de uso
password = "pass"
hash = hash_password(password)
print("Hash :", hash)

# Verificar la contraseña ingresada
#password_in = input("Ingresa la contraseña: ")
#if verify_password(password_in, hash):
    #print("Contraseña correcta")
#else:
    #print("Contraseña incorrecta")
