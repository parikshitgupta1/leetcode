class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r={}
        for c in ransomNote:
            if c not in count_r:
                count_r[c]=1
            else:
                count_r[c]+=1
        print(count_r)
       
        for cr in magazine:
            if cr not in count_r or count_r[cr]==0:
                # print("entered")
                continue
            else:
                count_r[cr]-=1
        
        print(count_r)                
        x=sum(count_r.values()) 
        print(x)
        if x==0:
            return 1
        else:
            return 0
        
