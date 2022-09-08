def foo(name):
    print(f'foo~~~~~ hello {name}')

if __name__ == "__main__":
    from src.config import NAME
    foo(NAME)
