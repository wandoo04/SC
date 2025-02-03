def hebbian_learning():
    # Initialize weight
    w = float(input("Enter the initial weight: "))
    d = float(input("Enter the learning rate: "))  # Learning rate
    x = float(input("Enter the input value: "))  # Input value
    y = float(input("Enter the output value: "))  # Output value

    for i in range(10):  # Train for 10 iterations
        w = w + d * x * y  # Hebbian weight update
        print(f"Iteration {i+1}: Updated weight = {w}")

if __name__ == "__main__":
    hebbian_learning()


Enter the initial weight: 0.5
Enter the learning rate: 0.1
Enter the input value: 1.0
Enter the output value: 1.0

