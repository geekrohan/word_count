# import modules used here

import sys
import re

#Function to read file name from command line
def main():
	return sys.argv[1]


#Programs start here

if __name__ == '__main__':
	main()

file=open(sys.argv[1])		#opening a file

words=file.read()			#assigning it to string
regex= r'\b\w+\b'	#defining regular expression for getting word
individual_words=re.findall(regex,words)	# getting words

word_count={}					
for word in individual_words:
	
	lowercase_word=word.lower()		#converting the word to lowercase
	
	if lowercase_word not in word_count:
		word_count[lowercase_word]=1
	else:
		
		count=word_count[lowercase_word]
		count=count+1
		word_count[lowercase_word]=count

sorted_list_by_value=sorted(word_count.items(), key= lambda kv:(kv[1],kv[0]),reverse=True)


file = open("most_popular.txt", "w")

for i in sorted_list_by_value:
	print(i, file=file)
file.close

sorted_list_by_names=sorted(word_count.items(), key= lambda kv:(kv[0],kv[1]))

file = open('alphabetical.txt', 'w')
for i in sorted_list_by_names:
	print(i,file=file)
file.close



# sorted_list=sorted(word_count.values(),reverse=True)
# print(sorted_list)




