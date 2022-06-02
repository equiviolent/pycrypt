# Caesar Cipher

The birth of cryptography.

The caesar cipher algorithm is a simple substitution method of encryption, each letter of plain text is replaced by a letter with some fixed number of position down with alphabet.

Example:
```
    X Y Z A B C
... │ │ │ │ │ │ ...
    ▼ ▼ ▼ ▼ ▼ ▼
    A B C D E F

----------------------

Text : ATTACKATONCE
Shift: 4
Cipher: EXXEGOEXSRGI
```

(Encryption phase with shift n)
```
En(x) = (x + n)mod26
```

(Decryption phase with shift n)
```
En(x) = (x - n)mod26
```

* Traverse the given text one character at a time .
* For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.
* Return the new string generated.
