
def meth():
    x = 10

    print("a")
    try:
        raise Exception()
    except ZeroDivisionError:
        print("DexE")
        try:

            raise FileNotFoundError()
        except FileNotFoundError:
            print("FileNotFoundError")
    except Exception as e:
        print("exE")

    finally:
        print("no zero division allowed (m)")

    print("b")


if __name__ == "__main__":
    meth()