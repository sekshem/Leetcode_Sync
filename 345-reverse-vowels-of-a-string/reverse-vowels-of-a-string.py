class Solution:
    def reverseVowels(self, s: str) -> str:
       a = list(s)
       l = 0 
       r = len(s) -1
       vowels = ('a','e','i','o','u','A','E','I','O','U')
       while(l < r):
        if(a[l] in vowels and a[r] in vowels): 
            a[l] , a[r] = a[r] , a[l]
            l+=1
            r-=1
        elif(a[l] in vowels):
            r-=1
        else: 
            l+=1
       return''.join(a)