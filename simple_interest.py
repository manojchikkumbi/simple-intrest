import sys

# Check if correct number of arguments are passed (script + 3 values = 4)
if len(sys.argv) != 4:
    print("Usage : python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

# Convert arguments to float
principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

# Validate input values
if principal <= 0:
    print("Principal amount must be greater than 0.")
elif rate <= 0:
    print("Rate of interest must be greater than 0.")
elif time <= 0:
    print("Time must be greater than 0.")
else:
    # Calculate Simple Interest
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest =", simple_interest)
