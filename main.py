from math import sqrt


def mean(liste=[]):
    sommeElement = customTotal(liste)
    nbElement = len(liste)
    moy = sommeElement / nbElement
    return moy


def variance(liste=[]):
    m = mean(liste)
    v = 0

    for i in liste:
        v = v + (i - m) ** 2
    result = (1 / len(liste)) * v
    return result


def standardDeviation(liste=[]):
    r = variance(liste)
    r = sqrt(r)
    return r


def customTotal(liste=[]):
    somme = 0
    for i in range(0, len(liste)):
        somme = somme + liste[i]
    return somme


if __name__ == '__main__':
    tab = [0, 10, 20, 15, 13, 7, 0, 20, 18, 16, 4, 2]
    print("La moyenne de " + str(tab) + " est " + str(mean(tab)))
    print("La variance de " + str(tab) + " est " + str(variance(tab)))
    print("L'ecart type de " + str(tab) + " est " + str(standardDeviation(tab)))
    print("La somme de " + str(tab) + " est " + str(customTotal(tab)))
