# Count by 2s, 3s, or Multiples of Any Number

# Get count by from user
count = int(input("Enter a number you want to count by?: "))

# Set n = 0
n = 0

# Get user choice - quit or not
choice = input("Enter return to continue or q to quit: ")

# While user choice is not quit do the following
while choice != 'q':
    # print n
    print(n)
    # Increase n by county by
    n += count
    # Get user choice quit or not
    choice = input("Enter return to continue or q to quit: ")
