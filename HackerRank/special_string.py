'''
Sample Input 1

7
abcbaba
Sample Output 1

10 
Explanation 1

The special palindromic substrings of s=abcbaba are a,b,c,b,a,b,a,bcb,bab,aba
'''
# Complete the substrCount function below.
def CountSpecialPalindrome(str): 
    n = len(str); 
    result = 0; 
    sameChar=[0] * n; 
    i = 0; 
    while (i < n): 
        sameCharCount = 1; 
  
        j = i + 1; 
        while (j < n): 
            if(str[i] != str[j]): 
                break; 
            sameCharCount += 1; 
            j += 1; 
        result += int(sameCharCount * 
                     (sameCharCount + 1) / 2); 
        sameChar[i] = sameCharCount; 
        i = j; 
    for j in range(1, n): 
        if (str[j] == str[j - 1]): 
            sameChar[j] = sameChar[j - 1]; 
        if (j > 0 and j < (n - 1) and 
           (str[j - 1] == str[j + 1] and 
            str[j] != str[j - 1])): 
            result += (sameChar[j - 1] 
                    if(sameChar[j - 1] < sameChar[j + 1])  
                    else sameChar[j + 1]); 
    return result; 
i=input()
str =input()
print(CountSpecialPalindrome(str)); 
