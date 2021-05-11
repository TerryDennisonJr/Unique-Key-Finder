"""
HW2 starting file
"""
#Terry Dennison Jr
#9 March 2021
#CIS 410

import string
from numpy import dot
from numpy.linalg import norm

punc_map = str.maketrans(string.ascii_uppercase,string.ascii_lowercase,string.punctuation)
text1 = 'The first book was good so I got the sequel. It seemed to go on and on and on but never got anywhere.'
text2 = 'The book was for me a little slow places but I did persevere and I am so glad I did. The book drew me in and the characters got under my skin and came to life.'
text3 = 'Love it! I laughed and cried and fell in love and never wanted this book to end. So beautifully written I stayed up half the night to finish it.'
text4 = 'Love this book and looking forward to reading the sequel to it. A lovely story full of emotions and history, which is beautifully written.'

text1 = text1.translate(punc_map)
text1 = text1.strip()
text2 = text2.translate(punc_map)
text2 = text2.strip()
text3 = text3.translate(punc_map)
text3 = text3.strip()
text4 = text4.translate(punc_map)
text4 = text4.strip()

dic={}
num = 0

for word in text1.split():
       
      if word not  in dic:
              
              dic[word] =num
              num += 1            
              
for word in text2.split():
       
      if word not  in dic:
              dic[word] =num
              num += 1
              
for word in text3.split():
       
      if word not  in dic:
              dic[word] =num
              num += 1
             
for word in text4.split():
       
      if word not  in dic:
              dic[word] =num
              num += 1

liText1 = [0] * len(dic.items()) 
liText2 = [0] * len(dic.items()) 
liText3 = [0] * len(dic.items()) 
liText4 = [0] * len(dic.items())  

for word in text1.split():
    for k, v in dic.items():
        if word == k:
            liText1 [v] += 1

for word in text2.split():
    for k, v in dic.items():
        if word == k:
            liText2 [v] += 1

for word in text3.split():
    for k, v in dic.items():
        if word == k:
            liText3 [v] += 1

for word in text4.split():
    for k, v in dic.items():
        if word == k:
            liText4 [v] += 1

sim1 = dot(liText1,liText2)/(norm(liText1)*norm(liText2))
sim2 = dot(liText1,liText3)/(norm(liText1)*norm(liText3))
sim3 = dot(liText1,liText4)/(norm(liText1)*norm(liText4))
sim4 = dot(liText2,liText3)/(norm(liText2)*norm(liText3))
sim5 = dot(liText2,liText4)/(norm(liText2)*norm(liText4))
sim6 = dot(liText3,liText4)/(norm(liText3)*norm(liText4))

print('Similarity between text1 and text2:', sim1)
print('Similarity between text1 and text3:', sim2)
print('Similarity between text1 and text4:', sim3)
print('Similarity between text2 and text3:', sim4)
print('Similarity between text2 and text4:', sim5)
print('Similarity between text3 and text4:', sim6)



    
        


        

    
