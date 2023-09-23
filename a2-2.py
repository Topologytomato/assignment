m = 10
n = int(input())
# calculate the result sequence
m_seq = list()
m_seq.extend([0, 1, 1])
for i in range(3, m ** 2 - 1):
    m_seq.append((m_seq[i - 1] + m_seq[i - 2]) % m)
    if m_seq[i] == 1 and (m_seq[i] + m_seq[i - 1]) % m == 0:
        break

# return corresponding remains
remain = m_seq[n % len(m_seq)]
print(remain)
