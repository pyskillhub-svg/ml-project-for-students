def add(a:int,b:int):
    if not isinstance(a , int) or not isinstance(b, int):
        raise TypeError("both are must be integers")
    print(a+b)
add(4,6)
