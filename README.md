# Python Entropy Calculator

This simple Python program takes a password as input and calculates its entropy. Entropy originates from physics, more specifically, the second law of thermodynamics, which describes the "randomness" of a thermal system. In a cybersecurity context, entropy measures how "random" something is—in this case, a password. Passwords with high entropy contain a mixture of lower and upper case letters, numbers, and special characters.

As you might have guessed, a high entropy password is a good password.

The formula for calculating password entropy is as follows:

### $E = \log_2(R^L)$

E = Entropy, measured in bits.

R = Pool of characters.

L = Password length.

## Download:
```git clone https://github.com/Liamhem/Entropy-Calculator/```
## Usage:

You can run this through CLI or your IDE of choice.

```python entropy.py```
### OR
```python3 entropy.py```
