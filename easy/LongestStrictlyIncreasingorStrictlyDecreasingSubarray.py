def longestMonotonicSubarray(nums):
    subarray = []
    direction = "Up"
    best = 0

    for n in nums:
        if subarray == []:
            subarray.append(n)

        elif subarray[-1] < n and direction == "Up":    # Sube y el elemento es mayor (sigue creciendo)
            subarray.append(n)

        elif subarray[-1] > n and direction == "Down":  # Baja y el elemento es menor (sigue decreciendo)
            subarray.append(n)

        elif subarray[-1] < n and direction == "Down":  # Baja y el elemento es mayor (cambia de dirección)
            subarray = [subarray[-1], n]
            direction = "Up"

        elif subarray[-1] > n and direction == "Up":    # Sube y el elemento es menor (cambia de dirección)
            subarray = [subarray[-1], n]
            direction = "Down"

        else:                                           # Elementos iguales: reiniciar
            subarray = [n]

        best = max(best, len(subarray))

    return best


print(longestMonotonicSubarray([1,4,3,3,2]))  # 2
print(longestMonotonicSubarray([3,2,1]))      # 3
print(longestMonotonicSubarray([3,3,3,3]))    # 1