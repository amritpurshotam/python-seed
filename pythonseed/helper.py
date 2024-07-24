def increment(x: int) -> int:
    return x + 1


def bugbear_error():
    try:
        list1 = [1, 2]
        list2 = [1, 2, 3]
        for i, j in zip(list1, list2, strict=False):  # show squiggly under zip for bugbear error
            print(i, j)
    except ValueError:  # show squiggly under except
        print("bugbear")


def test_mypy(x: int):
    increment(x)  # show squiggly under x
