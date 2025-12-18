# Coding:
# Demonstrating flow controls in python
#CONDITIONAL STATEMENTS

print("Conditional Statements")
x = 10
if x > 0:
    print(f"{x} is a positive number")
elif x == 0:
    print(f"{x} is zero.")
else:
    print(f"{x} is a negative number.")

#LOOPS
print("\nFor Loop:")
for i in range(1,6):
    print(f"Number:{i}")

print("\nWhile Loop:")
n = 5
while n > 0:
    print(f"Countdown: {n}")
    n -= 1

#NESTED LOOPS
print("\nNested Loops:")
for i in range(1,4):
    for j in range(1,4):
        print(f"i={i}, j={j}")

#LOOP CONTROL STATEMENTS
print("\nLoop Control Statements:")
print("Using break:")
for i in range(1,10):
    if i == 5:
        print("Breaking the loop.")
        break
    print(i)
print("\nUsing continue:")
for i in range(1,10):
    if i == 5:
        print("Skipping 5.")
        continue
    print(i)

print("\nUsing pass:")
for i in range(1,10):
    if i == 5:
        pass # Does nothing
    print(i)

#FUNCTION TO INCLUDE ALL FLOW CONTROLS
def demo_function(x):
    print("\nFunction with Flow Controls:")
    if x < 0:
        print(f"{x} is negative.")
    else:
        for i in range(x, x + 5):
            if i % 2 == 0:
                print(f"{i} is even.")
            else:
                print(f"{i} is odd.")

# Calling the function
demo_function(3)

