def find_largest_cross(grid):
    n = len(grid)
    m = len(grid[0])
    
    left = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]
    top = [[0] * m for _ in range(n)]
    bottom = [[0] * m for _ in range(n)]
        
    # Calcular valores para left y top
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                left[i][j] = left[i][j-1] + 1 if j > 0 else 1
                top[i][j] = top[i-1][j] + 1 if i > 0 else 1
    
    # Calcular valores para right y bottom
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = right[i][j+1] + 1 if j < m-1 else 1
                bottom[i][j] = bottom[i+1][j] + 1 if i < n-1 else 1
    
    max_size = 0
    
    # Encontrar el tamaño máximo de la cruz
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                size = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                max_size = max(max_size, (size - 1) * 4 + 1)

    if max_size == 1:
        max_size = 0
    
    return max_size

# Prueba de los inputs proporcionados

grid1 = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]

grid2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0]
]

# Calcular el tamaño de la cruz más grande para cada input
size1 = find_largest_cross(grid1)
size2 = find_largest_cross(grid2)

# Imprimir los resultados
print("El tamaño de la cruz más grande en el primer input es:", size1)
print("El tamaño de la cruz más grande en el segundo input es:", size2)