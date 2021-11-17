#Explaination
# Let's dive deep into the condition (time[i] + time[j]) % 60 == 0 to examine the relation between time[i] and time[j]. Assuming that a and b are two elements in the input array time, we have:

# (a+b)\space \% \space60=0 \\ \Downarrow \\ ((a \space \% \space 60)+(b \space \% \space 60))\space \% \space 60=0 \\ \Downarrow \\ \text{Therefore, either }\begin{cases} a \space \% \space60 &= 0\\ b \space \% \space60 &= 0 \end{cases} \text{, or } (a\space\%\space60)+(b\space\%\space60)=60 \\(a+b) % 60=0
# ⇓
# ((a % 60)+(b % 60)) % 60=0
# ⇓
# Therefore, either { 
# a % 60 = 0 ,b % 60​  = 0
# or (a % 60)+(b % 60)=60
# We would iterate through the input array time and for each element a, we want to know the number of elements b such that:

# b % 60=0, if  a % 60=0 if a % 60=0
# b % 60=60-a % 60, if a% 60 != 0 if a % 60 

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #count remainder with 60 in dic
        remainderDic = defaultdict(int)
        counts = 0
        
        for i, t in enumerate(time):
            remainder = t % 60
            if remainder == 0:
                counts += remainderDic[remainder]
            else:
                counts += remainderDic[60- remainder]
            remainderDic[remainder] += 1
            
        return counts
        