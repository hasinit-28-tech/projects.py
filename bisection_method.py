def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    
    # Negative check
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Handle 0 and 1
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    
    # Proper bounds (IMPORTANT for numbers < 1)
    low = 0
    high = square_target if square_target < 1 else square_target
    
    # (Better version below fixes this line 👇)
    low = 0
    high = max(1, square_target)
    
    for _ in range(max_iterations):
        mid = (low + high) / 2
        
        # ✅ Correct stopping condition (KEY FIX)
        if high - low <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        
        if mid * mid < square_target:
            low = mid
        else:
            high = mid
    
    print(f"Failed to converge within {max_iterations} iterations")
    return None