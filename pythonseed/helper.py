def increment(x: int) -> int:
    return x + 1


def bugbear_error():
    try:
        list1 = [1, 2]
        list2 = [1, 2, 3]
        for i, j in zip(list1, list2):  # show squiggly under zip for bugbear error
            print(i, j)
    except:  # show squiggly under except
        print("bugbear")


def test_mypy(x: str):
    increment(x)  # show squiggly under x
