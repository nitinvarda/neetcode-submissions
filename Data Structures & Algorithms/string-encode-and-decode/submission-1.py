class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return chr(258)
        newstring = ""
        separator = chr(257)
        for s in strs:
            newstring += s
            newstring += separator
        
        newstring = newstring[:-1]
        return newstring

    def decode(self, s: str) -> List[str]:
        if s == chr(258):
            return []
        seperator = chr(257)
        return s.split(seperator)
