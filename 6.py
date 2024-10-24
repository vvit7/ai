def move_disk(src, dest):
    print(f"Move disk from {src} to {dest}")

# Recursive function to solve Towers of Hanoi problem
def solve_hanoi(n, src, aux, dest):
    if n == 1:
        move_disk(src, dest)  # Move one disk directly
        return
    solve_hanoi(n - 1, src, dest, aux)  # Move top n-1 disks to auxiliary peg
    move_disk(src, dest)  # Move the nth disk to destination peg
    solve_hanoi(n - 1, aux, src, dest)  # Move the n-1 disks from auxiliary to destination

# Main function to ask for user input and solve the problem
def main():
    n = int(input("Enter the number of disks: "))  # User input for number of disks
    solve_hanoi(n, 'A', 'B', 'C')  # A is the source, B is auxiliary, C is the destination

# Call the main function
main()