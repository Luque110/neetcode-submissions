class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupo = {}
        for palabra in strs:
            clave = tuple(sorted(palabra))
            if clave not in grupo:      
                grupo[clave] = []
            grupo[clave].append(palabra)
        return list(grupo.values())