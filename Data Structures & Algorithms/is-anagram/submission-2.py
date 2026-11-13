class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mi_diccionario2 = {}
        mi_diccionario = {}
        for i in t:
            if i in mi_diccionario:
                mi_diccionario[i] += 1
            else:
                mi_diccionario[i] = 1
        for i in s:
            if i in mi_diccionario2:
                mi_diccionario2[i] += 1
            else:
                mi_diccionario2[i] = 1
        return mi_diccionario==mi_diccionario2

