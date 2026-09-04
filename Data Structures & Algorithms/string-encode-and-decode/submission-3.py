class Solution:
    def encode(self,strs:list[str])->str:
        result=""
        for word in strs:
            result+=str(len(word))+"#"+word
        return result
    def decode(self,s:str)->list[int]:
        result=[]
        i=0
        while i<len(s):
            j=s.index("#",i)
            n=int(s[i:j])
            i=j+1
            result.append(s[i:i+n])
            i+=n
        return result










       
