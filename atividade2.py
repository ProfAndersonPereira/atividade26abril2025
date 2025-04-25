def plusOne(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):  # Percorre do último ao primeiro dígito
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # Se o dígito for 9, define como 0 e propaga o carry
    
    # Se todos os dígitos eram 9, adiciona um 1 no início
    return [1] + digits

# Exemplos de uso
print(plusOne([1, 2, 3]))     # Saída: [1, 2, 4]
print(plusOne([4, 3, 2, 1]))   # Saída: [4, 3, 2, 2]
print(plusOne([9]))            # Saída: [1, 0]
print(plusOne([9, 9]))         # Saída: [1, 0, 0]
