import numpy as np

m = [[0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print("--------------------------------------------------------------")
print("Task 1")


def Reflective(m):
    reflective = True
    for i in range(len(m)):
        for j in range(len(m)):
            if (i == j):
                if (m[i][j] != 1):
                    reflective = False
                    return reflective

    return reflective


def Semmetric(m):
    symmetric = True
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i][j] != m[j][i]) & (i != j)):
                symmetric = False
                return symmetric

    return symmetric

Semmetric(m)

def Transitivity(m):
    transitivity = True
    for a in range(len(m)):
        for b in range(len(m)):
            for c in range(len(m)):
                if ((m[a][b] == 1) & (m[b][c] == 1)):
                    if (not (m[a][c] == 1)):
                        transitivity = False
                        return transitivity

    return transitivity
Transitivity(m)


def Antisymmetric(m):
    antisymmetric = True
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i][j] == 1) & (m[j][i] != 0) & (i != j)):
                antisymmetric = False
                return antisymmetric

    return antisymmetric


Antisymmetric(m)


def Asymmetric(m):
    asymmetric = True
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i][j] == 1) & (m[j][i] != 0)):
                asymmetric = False
                return asymmetric

    return asymmetric


def Equivalence():
    if Reflective(m) == True and Transitivity(m) == True and Semmetric(m) == True:
        print("Відношення еквівалентне")
    else:
        print("Відношення не еквівалетне")

Equivalence()


def PartialOrder():
    if Reflective(m) == True and Transitivity(m) == True and Semmetric(m):
        print("Відношення є відношенням часткового порядку")
    else:
        print("Відношення не є відношенням часткового порядку")

PartialOrder()

def StrictOrder():
    if Transitivity(m) == True and Asymmetric(m) == True:
        print("Відношення є відношенням строгого порядку")
    else:
        print("Відношення не є відношенням строгого порядку")

StrictOrder()
print("----------------------------------------------------------------")
print("Task 2")


def reflectiveClosure(m):
    m1 = m
    for i in range(len(m1)):
        m1[i][i] = 1

    return m1


print("Рефлексивне замикання: " + str(reflectiveClosure(m)))


def symmetricalClosure(m):
    m1 = m
    for i in range(len(m1)):
        for j in range(len(m1)):
            if not i == j:
                if m1[i][j] == 1:
                    m1[j][i] = 1

    return m1


print("Симетричне замикання: " + str(symmetricalClosure(m)))


def transitiveClosure(m):
    m1 = m
    for i in range(len(m1)):
        for j in range(len(m1)):
            if not i == j:
                if m1[i][j] == 1:
                    for k in range(len(m1)):
                        m1[i][k] = m1[i][k] | m1[j][k]

    return m1


print("Транзитивне замикання: " + str(transitiveClosure(m)))

print("--------------------------------------------------------------")

print("Task 3")


def getComposition(r1, r2):
    length = len(r1)
    r = np.zeros((length, length))
    for a in range(length):
        for b in range(length):
            for c in range(length):
                if (r1[a][c] == 1) & (r2[c][b] == 1):
                    r[a][b] = 1
                    break

    return r


r1 = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1]
]

r2 = getComposition(r1, r1)

r3 = getComposition(r2, r1)

print("Відношення другого степеня: ")
print(r2)
print("Відношення третього степеня: ")
print(r3)
print("---------------------------------------------------------------")
