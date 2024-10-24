
def place(k, i):
    for j in range(k):
        if x[j] == i or abs(k - j) == abs(i - x[j]):
            return False
    return True
def nQueen(k, n):
    if k == n:
        solutions.append(x.copy())  # Store the current solution
        return
    for i in range(n):
        if place(k, i):
            x[k] = i
            nQueen(k + 1, n)
def printSolution(solution, n): 
    for row in solution: 
        print('. ' * row + 'Q ' + '. ' * (n - row - 1)) 
        print()
if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    if n <= 0:
        print("Enter a valid input.")
    else:
        x = [0] * n  # Initialize the list with zeros
        solutions = []  # List to store all valid solutions
        nQueen(0, n)
        if solutions:
            printSolution(solutions[0], n)  # Print the first valid arrangement in matrix format
        else:
            print("No solutions exist.")