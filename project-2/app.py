def add(a, b):
    return a + b

def test():
    assert add(2, 3) == 5
    assert add(10, 5) == 15

if __name__ == "__main__":
    test()
    print("All tests passed successfully!")
