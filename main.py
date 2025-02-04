from collections import Counter
wordlist = open('wordlist.txt','r')
words = [i.strip() for i in wordlist if len(i) == 6]
wordlist.close()
curWords = words
n = 0
def ans(word, guess):
	ret = 'bbbbb'
	guessC = {}
	wordC = Counter(word)
	for i in range(len(word)):
		if word[i] == guess[i]:
			ret = ret[:i]+'g'+ret[i+1:]
			wordC[word[i]] -= 1
	for i in range(len(word)):
		if guess[i] in wordC and wordC[guess[i]] > 0 and ret[i] == 'b':
			wordC[guess[i]] -= 1
			ret = ret[:i]+'y'+ret[i+1:]
	return ret
def getMax(i, curWords):
	c = Counter([ans(i, j) for j in curWords])
	return c[max(c, key=c.get)]
lastGuess = 'salet'
lastColors = 'ggggg'
while True:
	if lastColors == 'ggggg':
		curWords = words
		while True:
			badGuess = input('(Type QUIT to begin assistance) What was your guess?: ').lower()
			if badGuess == 'quit':
				break
			badColors = input('(Add B for black, Y for yellow, G for green) And what were you given back?: ').lower()
			curWords = [i for i in curWords if ans(i,badGuess) == badColors]
	else:
		curWords = [i for i in curWords if ans(i,lastGuess) == lastColors]
	lastGuess = 'salet' if words == curWords else max(curWords, key = lambda p: getMax(p, curWords))
	lastColors = input('I guess "'+lastGuess+'". What did your game tell you? ')
