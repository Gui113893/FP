def remove_multiple(list, n):
    for value in list:
        if value == n:
            pass
        elif value % n == 0:
            list.remove(value)

    return list

def primesUpTo(n):
    lista = [i for i in range(2, n+1)]

    for elemento in lista:
        if elemento ** 2 < n:
            remove_multiple(lista, elemento)

    return set(lista)

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()
    