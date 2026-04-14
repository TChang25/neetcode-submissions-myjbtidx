class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = ""
        for s in strs:
            sizes += (str(len(s)))
            sizes += (',')
        sizes += ('#')
        for s in strs:
            sizes +=(s)
        return sizes

        

    def decode(self, s: str) -> List[str]:
        i = 0
        sizes = []
        size = ""
        if not s:
            return sizes
        while s[i] != '#':
            if s[i] != ',':
                size += (s[i])
            else:
                sizes.append(int(size))
                size = ""
            i += 1
            
        i += 1
        words = []
        for length in sizes:
            itr = 0
            word = ""
            while itr < length:
                word += (s[i])
                itr += 1
                i += 1
            words.append(word)
        return words
                
                