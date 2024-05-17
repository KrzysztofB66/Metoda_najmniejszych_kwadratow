import math


# Dane wejściowe
def funkcja(x):
    return math.sqrt(3 + 2*math.pow(x, 2))


m = 6  # stopień wielomianu
x = -0.25
n = 4
X = [-1, -0.5, 0, 0.5, 1]
Y = [funkcja(x) for x in X]


def eliminacja_gausa(A, b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = round(float(M[n-1][n])/M[n-1][n-1], 3)
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = round(float(M[i][n] - z)/M[i][i], 3)
    return x


def metoda_najmniejszych_kwadratow(x, y, m):
    n = len(x)
    A = [[sum(x[i]**(k+j) for i in range(n)) for j in range(m+1)] for k in range(m+1)]
    B = [sum(y[i]*x[i]**k for i in range(n)) for k in range(m+1)]
    wspolczynniki = eliminacja_gausa(A, B)
    return wspolczynniki


def oblicz_wielomian(x, wspolczynniki):
    m = len(wspolczynniki)
    return sum([wspolczynniki[i]*x**i for i in range(m)])

wspolczynniki = metoda_najmniejszych_kwadratow(X, Y, m)
print("Współczynniki wielomianu aproksymującego: ", wspolczynniki)


y_wartosc = oblicz_wielomian(x, wspolczynniki)
print(f"Wartość wielomianu aproksymującego dla x = {x} i stopnia wielomianu = {m} wynosi {y_wartosc}")

