import sys
from functools import cache
from narwhals import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        sys.setrecursionlimit(10**6) #Pongo esta shit porque si no explota

        DERECHA, ABAJO = 0, 1

        @cache
        def contar(i, j, d):
            # 1. Fuera de la grilla
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            # 3. Celda espejo: el movimiento está forzado
            if grid[i][j] == 1:
                if d == DERECHA:          # entró moviéndose a la derecha
                    return contar(i + 1, j, ABAJO)    # sale hacia abajo
                else:                     # entró moviéndose hacia abajo
                    return contar(i, j + 1, DERECHA)  # sale a la derecha

            # 4. Celda vacía
            return (contar(i, j + 1, DERECHA) + contar(i + 1, j, ABAJO)) % MOD

        resultado = contar(0, 0, DERECHA)
        contar.cache_clear()
        return resultado