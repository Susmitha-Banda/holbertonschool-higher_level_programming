def add(a,b=98):
    if not isinstance(a, (int,float)):
        raise TypeError("a must be an Int")
    return int(a)+int(b)