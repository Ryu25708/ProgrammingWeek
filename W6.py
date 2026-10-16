def sum_m_to_n(m, n):
    total = 0
    count = m

    while count <= n:
        total = total + count
        count = count + 1

    return total


print(sum_m_to_n(1, 5))
