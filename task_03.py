import decimal

def lexicographics(to_analyze):
	count_words = []
	for char in to_analyze.split('\n'):
		length = len(char.split(' '))
		count_words.append(length)
	avg = decimal.Decimal(sum(count_words))/len(count_words)
	max_words = max(count_words)
	min_words = min(count_words)
	tup = max_words, min_words, avg
	return tup
