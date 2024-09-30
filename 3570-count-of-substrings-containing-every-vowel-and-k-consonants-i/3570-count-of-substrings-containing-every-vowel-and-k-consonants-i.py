class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # vowels={'a','e','i','o','u'}
        # count_substr=0
        # if k==1:
        #     return 0
        # #for i in range(len(word)):
        # i,j=0,0
        # count_c=0
        # vowel_inword=set()
        # while j<len(word):
        #     c=word[j]
        #     if c in vowels:
        #         vowel_inword.add(c)
        #     else:
        #         count_c+=1

        #     while len(vowel_inword)==5 and count_c>=k:
        #         count_substr+=(len(word)-j)
        #         if word[i] in vowels:
        #             vowel_inword.remove(word[i])
        #         else:
        #             count_c-=1
        #     j+=1
        #     i+=1
        # return count_substr

        # vowels={'a','e','i','o','u'}
        # count=0
        # i=0
        # while i<len(word):
        #     vinword=set()
        #     j=i
        #     while j<len(word) and word[j] in vowels:
        #         vinword.add(word[j])
        #         j+=1
        #     if len(vinword)==5 :
        #         consonant=0
        #         left=i-1
        #         while left>=0 and consonant<k:
        #             if word[left] not in vowels:
        #                 consonant+=1
        #             left-=1

        #         right=j
        #         while right<len(word) and consonant<k:
        #             if word[right] not in vowels:
        #                 consonant+=1
        #             right+=1
        #         if consonant>=k:
        #             count+=(right-j+1)
        #     i+=1

        # return count
        vowels = {'a', 'e', 'i', 'o', 'u'}  
        n = len(word)
        count = 0  

       
        for start in range(n):
            vowels_found = set()
            consonant_count = 0  

            for end in range(start, n):
                char = word[end]
                
                if char in vowels:
                    vowels_found.add(char)
                else:
                    consonant_count += 1

                    if consonant_count>k:
                        break
                if consonant_count==k and vowels_found==vowels:
                    count+=1
                

        return count