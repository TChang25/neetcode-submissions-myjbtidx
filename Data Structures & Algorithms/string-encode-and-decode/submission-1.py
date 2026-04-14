class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(0, len(strs)):
            for j in range(0, len(strs[i])):
                encoded += (str(ord(strs[i][j])))
                if j == len(strs[i])-1:
                    continue
                else:
                    encoded += ','
            encoded += " "
        return encoded

    def decode(self, s: str) -> List[str]:
        decodedList = s.split(" ")[:-1]
 
        for i in range(0, len(decodedList)):
            decodedStr = ""
            if not decodedList[i]:
                continue 
            asc = decodedList[i].split(',')
            for s in asc:
                decodedStr += (chr(int(s)))
            decodedList[i] = decodedStr
            
        return decodedList