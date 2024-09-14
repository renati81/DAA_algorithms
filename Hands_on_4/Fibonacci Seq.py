# python code for fibonacci sequence
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#python code for fibonacci sequence when n = 5
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Main function
if __name__ == "__main__":
    n = 5
    result = fib(n)
    print("Fibonacci of", n, "is:", result)



# Debug and listing the stack overflow through fib(5) 
print("\nStepping through fib(5):")
print("fib(5)")
print("  -> fib(4)")
print("    -> fib(3)")
print("      -> fib(2)")
print("        -> fib(1)")
print("        <- return 1")
print("        -> fib(0)")
print("        <- return 0")
print("      <- return 1")
print("      -> fib(1)")
print("      <- return 1")
print("    <- return 2")
print("    -> fib(2)")
print("      -> fib(1)")
print("      <- return 1")
print("      -> fib(0)")
print("      <- return 0")
print("    <- return 1")
print("  <- return 3")
print("  -> fib(3)")
print("    -> fib(2)")
print("      -> fib(1)")
print("      <- return 1")
print("      -> fib(0)")
print("      <- return 0")
print("    <- return 1")
print("    -> fib(1)")
print("    <- return 1")
print("  <- return 2")
print("<- return 5")
print("\nFinal result: fib(5) = ",result)
