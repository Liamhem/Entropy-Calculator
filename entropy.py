# The purpose of this program is to calculate the entropy of a password gathered from input
# The formula for password entropy is log2(R ** L)
import getpass
import math
import string
import sys

def calculate_entropy():
    pool_size = 0
    password = getpass.getpass("Enter your password to have it checked (output will be hidden):\n")
    password_length = len(password)
    # Check for upper and lower case letters, numbers, and special characters
    if any(index in string.punctuation for index in password):
        pool_size += 32
    if any(index.isdigit() for index in password):
        pool_size += 10
    if any(index.islower() for index in password):
        pool_size += 26
    if any(index.isupper() for index in password):
        pool_size += 26
    if password_length == 0:
        raise SyntaxError("No password supplied.")
    entropy_result = math.log2(pool_size ** password_length)
    print(f'Pool Size: {pool_size}')
    print(f'Password length: {password_length}')
    print(f'\nEntropy: {entropy_result:.2f} bits.')
    if entropy_result <= 60:
        print("*This value is low. Try opting for a stronger password.")
        
def main():
    try:
        calculate_entropy()
    except KeyboardInterrupt:
        print("Quitting...")
        exit(0)
    except SyntaxError as e:
        print(e, "Error.\n")
        calculate_entropy()
    finally:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
