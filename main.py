def GCD(a: int, b: int):
    # Ensure that a is greater than b
    if (b > a):
        temp: int = a;
        a = b;
        b = temp;
 
    # Compute GCD using the Euclidean algorithm
    while (b > 0):
        r: int = a % b;
        a = b;
        b = r;
 
    return a;

gcd = GCD(100,10)
print(gcd) # 10