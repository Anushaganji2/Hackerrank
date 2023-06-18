# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X = str(input())    
    b=X.split()
    if 4 in b:
        print(4 in b)