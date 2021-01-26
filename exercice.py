#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction
    motMajuscule=""
    for var in mot:
        motMajuscule += chr(ord(var)-32)
    return motMajuscule


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)): #range(start, stop, step)->nb tours boucle for #len()->nb élements dans une liste donnée
        mots[i] = majuscule(mots[i])

    print(mots)

