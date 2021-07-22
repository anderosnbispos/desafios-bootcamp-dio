d = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

natendidos = 0

#continue desenvolvendo a solucao
for i in range(3):
    if r[i] > d[i]:
        natendidos += r[i] - d[i]

print(natendidos)