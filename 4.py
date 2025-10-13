import numpy as np

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def print_identity_matrix(size):
    identity = np.eye(size)
    print(f"\nIdentity matrix of size {size} x {size}:\n")
    for row in identity:
        print(" ".join(f"{int(elem)}" for elem in row))

def main():
    n = get_positive_integer("Enter the size of the identity matrix: ")
    print_identity_matrix(n)

if __name__ == "__main__":
    main()
