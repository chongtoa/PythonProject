lyrics_list = ['hers', 'name', 'is', 'rio']

words = make_wordlist()  #返回测试单词
for word in words:
	if word in lyrics_list:
		print(word, "is in the lyrics_list")

# better
lyrics_set = set(lyrics_list)
words = make_wordlist()
for word in words:
	if word in lyrics_set:
		print(word, "is in the lyrics_list")




