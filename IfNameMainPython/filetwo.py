# file two.py
import fileone

print("top-level in two.py")
fileone.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")