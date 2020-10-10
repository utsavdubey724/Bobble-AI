import string 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

myStr="Steve was born in Tokyo, Japan in 1950. He moved to London with his parents when he was 5 years old. Steve started school there and his father began work at the hospital.His mother was a house wife and he had four brothers.\t He lived in England for 2 years then moved to Amman, Jordan where he lived there for 10 years. Steve then moved to Cyprus to study at the Mediterranean University.Unfortunately, he did not succeed and returned to Jordan. His parents were very unhappy so he decided to try in America.\tHe applied to many colleges and universities in the States and finally got some acceptance offers from them. He chose Wichita State University in Kansas. His major was Bio-medical Engineering. He stayed there for bout six months and then he moved again to a very small town called Greensboro to study in a small college."


#To convert the string into lowercase
result=myStr.lower()
print("To Lowercase:")
print(result)
print()

#To remove punctuation
result=''.join(c for c in s if c not in punctuation)
print("After removing punctuation:")
print(result)
print()

#To remove whitespaces
result=myStr.replace(" ", "") 
print("After removing whitesapces:")
print(result)
print()

#To remove stop words from string
stop_words=set(stopwords.words('english'))
tokens=word_tokenize(myStr)
result=[i for i in tokens if not i in stop_words]
print("After removing stop words:")
print(result)
print()

#To perfrom stemming on string
snowball_stemmer=SnowballStemmer(‘english’)
word_tokens=nltk.word_tokenize(myStr)
result=[snowball_stemmer.stem(word) for word in word_tokens]
print (result)
print()

#To perform Lemmaize on string
stopword=stopwords.words(‘english’)
wordnet_lemmatizer=WordNetLemmatizer()
word_tokens=nltk.word_tokenize(myStr)
result= [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
print(result)



