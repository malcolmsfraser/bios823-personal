
def greet(name='foo'):
    print(f"hello {name}")

if __name__ == "__main__":
    import sys
    greet(sys.argv[1])
