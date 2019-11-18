from authlib.jose import jwk

private_key_file = open('id_rsa')
private_key = private_key_file.read()
private_key_file.close()

public_key_file = open('id_rsa.pub')
public_key = public_key_file.read()
public_key_file.close()

obj = jwk.dumps(public_key, kty='RSA')
print(obj)

