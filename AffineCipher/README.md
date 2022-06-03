The Affine Cipher is an ancient encryption system created in the Middle East.

The affine cipher is a type of [monoalphabetic substitution](https://www.101computing.net/mono-alphabetic-substitution-cipher/) cipher.

> Each character is mapped to its numeric equivalent, encrypted with a mathematical function and then converted to the letter relating to its new numeric value.

The encryption function is:
```
  E(x) = (ai + b) mod m
```
where:
  * `i` is the letter's index from 0 to the length of the alphabet - 1.
  * `m` is the length of the used alphabet. For the Roman alphabet `m` is `26`.
  * `a` and `b` are integers which make the encryption key.

The value of `a` and `b` must be [coprime](http://www.isg.rhul.ac.uk/static/msc/teaching/ic2/demo/24c.htm) for automatic decryption to succeed.

Th decryption function is:
```
  D(y) = (a^-1)(y - b) mod m
```
where:
  * `y` is the numeric value of an encrypted letter, i.e `y = E(x)`.
  * `a^-1`is the [modular multiplicative inverse](https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/) (MMI) of a `a mod m`.

The modular multiplicative inverse only exists if `a` and `m` are coprime.
