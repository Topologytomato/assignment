import numpy as np

# Generate some example to check the answers
# F_seq = list(range(1, 101))
# F_seq[0] = 0
# F_seq[1] = 1
# for i in range(2, 100):
#     F_seq[i] = F_seq[i - 1] + F_seq[i - 2]

# result = np.zeros((100, 100))
# for p in range(1, 100):
#     for q in range(0, 100):
#        result[p, q] = F_seq[q] % p


n = int(input())
m = int(input())
# calculate the result sequence
m_seq = list()
m_seq.extend([0, 1, 1])
for i in range(3, m**2 - 1):
    m_seq.append((m_seq[i-1] + m_seq[i-2]) % m)
    if m_seq[i] == 1 and (m_seq[i] + m_seq[i - 1]) % m == 0:
        break

# return corresponding remains
remain = m_seq[n % len(m_seq)]
print(remain)

