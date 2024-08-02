#!/usr/bin/env python
# coding: utf-8

# In[2]:


def tringle(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end=" ") 
        print("\n")
tringle(3)        


# In[3]:


def tri(n):
    k= n
    for i in range(0,n):
       
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j  in range(0,i+1) :
            print("* ",end="")
        print("\n")
print("**********")            
tri(7) 


# In[4]:


def triangle(n):
    """ this is tri called function """
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*", end=" ")
        print("\n")   
triangle(5)  


# In[5]:


def tri(n):
    for i in range(n):
        for j in range(i+1):
            print(j,end=" ")
        print()  
tri(5)        


# In[6]:


# 1. Write a program to find the square of the largest element in an array.
# 2. Write a program to find the number of times a number exists in a list. 
# return in descending order of number of occurrences a number exists.
# 3. write a program to find a number that is prime or not prime.
# 4. write a program to delete duplicates and return the list without duplicates.
# 5. Write a program to find the second large number in a list.
# 6. Write a program to find the second-largest negative number in a list. numbers = [3, -5, -28, 7, -81, 4, -16]
# 7. Write a program to reverse the order of words in a sentence.
# 8. Write a program to count the lower and upper case characters in any text or sentence.
# 9. Check if a String Is a Palindrome


# In[7]:


# 1. Write a program to find the square of the largest element in an array.

user_int = input()
l = user_int.split(",")
print(l)
type(l[1])


# In[8]:


user_int = input()
l = user_int.split(",")

for i in l:
    a=int(i)
    if int(i)>a:
        a=int(i)
    else:
        pass
sqr = a*a
print(sqr) 


# In[10]:


# 2. Write a program to find the number of times a number exists in a list. 
# return in descending order of number of occurrences a number exists.

from collections import Counter

def count_occurrences(nums):
    # Count the occurrences of each number using Counter
    counts = Counter(nums)
    
    # Sort the counts in descending order of occurrences
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_counts

# Example usage
nums = [1, 3, 2, 2, 3, 1, 4, 2, 3, 1, 4, 4, 4]
result = count_occurrences(nums)
print(result)


# In[11]:


nums = [1, 3, 2, 2, 3, 1, 4, 2, 3, 1, 4, 4, 4]

dic ={}

for i in nums:
    if i in dic:
        dic[i] = dic[i]+ 1
    else :
        dic[i] = 1
print(dic)   


# In[12]:


# 3. write a program to find a number that is prime or not prime.

number= int(input())

for i in range (2, number):
    if number%i==0:
        flag = 1
        break
    else :
        flag =0
if (flag == 1):
    print("not prime")
    
else:
    print("prime")


# In[13]:


# 4. write a program to delete duplicates and return the list without duplicates.

mylist = input()

l1 = mylist.split(",")

l2=[]

for i in l1:
    l2.append(int(i))
set(l2)  


# In[14]:


# 5. Write a program to find the second large number in a list.

mylist = input()

l1 = mylist.split(",")

l2=[]

for i in l1:
    l2.append(int(i))
    
def find_second_largest(l2):
    if len(l2) < 2:
        return None  # Not enough elements to have a second largest

    unique_nums = list(set(l2))  # Remove duplicates
    
    if len(unique_nums) < 2:
        return None  # Not enough unique elements to have a second largest

    unique_nums.sort()  # Sort the list
    return unique_nums[-2]  # Return the second last element
result = find_second_largest(l2)
print(result)


# In[15]:


# 6. Write a program to find the second-largest negative number in a list. 

numbers = [3, -5, -28, 7, -81, 4, -16]

l1=[]

for i in numbers:
    if i <0:
        l1.append(i)

l1.sort()

l1[-2]


# In[16]:


def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage
sentence = "Hello world this is a test"
result = reverse_words(sentence)
print(result)


# In[17]:


# 8. Write a program to count the lower and upper case characters in any text or sentence.
inp = input()

d ={"uppercase":0 , "lowecase":0}
for i in inp:
    if i.isupper():
        d["uppercase"]=d["uppercase"]+1
    elif i.islower():
        d["lowecase"]=d["lowecase"]+1
print("UPPER CASE ", d["uppercase"])
print("LOWER CASE ", d["lowecase"])


# In[20]:


# 9. Check if a String Is a Palindrome

inp = input()

reverse = inp[::-1]

if reverse == inp:
    print("Paindrome")
else:
    print("not palindrome")
    


# In[ ]:




