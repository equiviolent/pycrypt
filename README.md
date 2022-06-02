# PyCrypt

`A series of cryptography algorithms to learn more about python and cryptography.`

* Create a virtual environment:
```sh
  python3 -m venv (environment name)
```

* Activate the environment:
```sh
  source (environment name)/bin/activate
```

* Install dependencies:
```sh
  python -m pip install -r requirements.txt
```

## Some words about cryptography

In the programming or mathematical world, a function is merely a way to enter values and receive output.
When using algorithms in cryptography, we generally have two inputs for encryption and two inputs for decryption:
  - The encryption process will take the plaintext message(P) along with an encryption key(K) and then run the plaintext through encryption algorithm, which will return a ciphertext(C).
  - On the decryption side, the ciphertext(C) will be supplied along with the encryption key(K), which will reproduce the plaintext(P).
