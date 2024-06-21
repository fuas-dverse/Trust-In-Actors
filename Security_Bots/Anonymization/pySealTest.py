# import seal
# from seal import scheme_type, EncryptionParameters, SEALContext, KeyGenerator, Encryptor, Decryptor, Evaluator, Plaintext, Ciphertext

# # Create encryption parameters
# params = EncryptionParameters(scheme_type.BFV)
# params.set_poly_modulus_degree(4096)
# params.set_coeff_modulus(seal.coeff_modulus_128(4096))
# params.set_plain_modulus(1 << 8)

# # Create SEAL context
# context = SEALContext(params)

# # Generate keys
# keygen = KeyGenerator(context)
# public_key = keygen.public_key()
# secret_key = keygen.secret_key()

# # Create encryptor and decryptor
# encryptor = Encryptor(context, public_key)
# decryptor = Decryptor(context, secret_key)

# # Create evaluator
# evaluator = Evaluator(context)

# # Encrypt plaintexts
# plain1 = Plaintext("5")
# plain2 = Plaintext("3")
# cipher1 = Ciphertext()
# cipher2 = Ciphertext()
# encryptor.encrypt(plain1, cipher1)
# encryptor.encrypt(plain2, cipher2)

# # Perform addition homomorphically
# cipher_result = Ciphertext()
# evaluator.add(cipher1, cipher2, cipher_result)

# # Decrypt the result
# plain_result = Plaintext()
# decryptor.decrypt(cipher_result, plain_result)
# print(f"Encrypted addition result: {plain_result.to_string()}")

# # Perform multiplication homomorphically
# cipher_product = Ciphertext()
# evaluator.multiply(cipher1, cipher2, cipher_product)

# # Decrypt the product
# plain_product = Plaintext()
# decryptor.decrypt(cipher_product, plain_product)
# print(f"Encrypted multiplication result: {plain_product.to_string()}")
# from Pyfhel import Pyfhel, PyCtxt

# # Initialize Pyfhel context
# context = Pyfhel()
# context.contextGen(p=65537, m=4096, base=2, sec=128)
# context.keyGen()

# # Encrypt plaintexts
# plain1 = 5
# plain2 = 3
# cipher1 = context.encryptInt(plain1)
# cipher2 = context.encryptInt(plain2)

# # Perform addition homomorphically
# cipher_result = cipher1 + cipher2

# # Decrypt the result
# plain_result = context.decryptInt(cipher_result)
# print(f"Encrypted addition result: {plain_result}")

# # Perform multiplication homomorphically
# cipher_product = cipher1 * cipher2

# # Decrypt the product
# plain_product = context.decryptInt(cipher_product)
# print(f"Encrypted multiplication result: {plain_product}")

from phe import paillier

# Generate a public/private key pair
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt a number
plaintext = 42
ciphertext = public_key.encrypt(plaintext)
print("Cypher: ",ciphertext.ciphertext(be_secure=False))
# Perform operations on the encrypted data
ciphertext2 = ciphertext + 15

# Decrypt the result
result = private_key.decrypt(ciphertext2)

print(f"The result is: {result}")

