import math 

def main():
    c = float(input("Enter the learning coefficient of network c: "))
    w10, b10 = map(float, input("Enter the input weights/base of first network: ").split()) 
    w20, b20 = map(float, input("Enter the input weights/base of second network: ").split())

    p = float(input("Enter the input value p: ")) 
    t = float(input("Enter the target value t: "))

    # Step 1: Propagation of signal through network 
    n1 = w10 * p + b10
    a1 = math.tanh(n1) 
    n2 = w20 * a1 + b20 
    a2 = math.tanh(n2) 
    e = t - a2

    # Back Propagation of Sensitivities 
    s2 = -2 * (1 - a2 ** 2) * e
    s1 = (1 - a1 ** 2) * w20 * s2

    # Updation of weights and bases 
    w21 = w20 - (c * s2 * a1)
    w11 = w10 - (c * s1 * -1) 
    b21 = b20 - (c * s2)
    b11 = b10 - (c * s1)

    print("The updated weight of first network w11 =", w11) 
    print("The updated weight of second network w21 =", w21) 
    print("The updated base of first network b11 =", b11) 
    print("The updated base of second network b21 =", b21)


if  __name__  == " main ": 
    main()


=============
1,2,3,1,1,1,1