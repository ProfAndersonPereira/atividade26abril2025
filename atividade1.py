def mySqrt(x):
    if x == 0 or x == 1:
        return x
    
    left, right = 1, x
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
            result = mid  # Atualiza o resultado para o maior k encontrado até agora onde k^2 <= x
        else:
            right = mid - 1
    
    return result

# Exemplos de uso
print(mySqrt(4))   # Saída: 2
print(mySqrt(8))   # Saída: 2
print(mySqrt(25))  # Saída: 5
print(mySqrt(26))  # Saída: 5 
print(mySqrt(16))  # Saída: 4 
print(mySqrt(36))  # Saída: 6 