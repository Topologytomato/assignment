m = 10
n1 = int(input())
n2 = int(input())
# calculate the result sequence
m_seq = list()
m_seq.extend([0, 1, 1])
for i in range(3, m ** 2 - 1):
    m_seq.append((m_seq[i - 1] + m_seq[i - 2]) % m)
    if m_seq[i] == 1 and (m_seq[i] + m_seq[i - 1]) % m == 0:
        break

remain = sum(m_seq[(n1 % 60):((n2 % 60) + 1)]) % 10
print(remain)

