def main(): 
    inputs = [] 
    weights = []
    desired_output = 0.0 
    # Initialize weights 
    for i in range(3):
        weight = float(input(f"Initialize weight vector {i}: ")) 
        weights.append(weight)
    # Get desired output
    desired_output = float(input("Enter the desired output: ")) 
    # Perceptron training loop
    while True:
        # Calculate net input (simplified for this example) 
        net_input = sum(w * x for w, x in zip(weights, inputs)) 
        # Calculate output (simplified for this example)
        output = 1 if net_input >= 0 else 0 
        # Calculate error
        delta = desired_output - output 
        if delta == 0:
            print("\nOutput is correct") 
            break
        # Adjust weights based on error 
        for i in range(3):
            weights[i] = weights[i] + delta * inputs[i] 
            print(f"\nValue of delta is: {delta}") 
            print("Weights have been adjusted")
if  __name__  == " main ": 
    main()


=================
0.5
-0.2
0.1
1
