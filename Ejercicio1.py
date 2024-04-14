def count_combinations(n):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    memo = {}  # Estructura de memoización
    
    def helper(curr_digit, remaining):
        if remaining == 0:
            return 1
        
        if (curr_digit, remaining) in memo:
            return memo[(curr_digit, remaining)]
        
        total = 0
        adj_digits = get_adjacent_digits(curr_digit, keypad)
        
        for digit in adj_digits:
            total += helper(digit, remaining - 1)
        
        memo[(curr_digit, remaining)] = total
        return total
    
    total_combinations = 0
    
    for i in range(10):
        total_combinations += helper(str(i), n - 1)
    
    return total_combinations

def get_adjacent_digits(digit, keypad):
    adj_digits = []
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == digit:
                if i > 0 and keypad[i-1][j] != '*' and keypad[i-1][j] != '#':
                    adj_digits.append(keypad[i-1][j])
                if i < len(keypad) - 1 and keypad[i+1][j] != '*' and keypad[i+1][j] != '#':
                    adj_digits.append(keypad[i+1][j])
                if j > 0 and keypad[i][j-1] != '*' and keypad[i][j-1] != '#':
                    adj_digits.append(keypad[i][j-1])
                if j < len(keypad[0]) - 1 and keypad[i][j+1] != '*' and keypad[i][j+1] != '#':
                    adj_digits.append(keypad[i][j+1])
                adj_digits.append(digit)  # Agregar el dígito actual como adyacente válido
    return adj_digits

# Ejemplo de uso
n = 10
combinations = count_combinations(n)
print(f"El número total de combinaciones posibles para n = {n} es: {combinations}")