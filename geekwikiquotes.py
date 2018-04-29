#!/usr/bin/env python3
import wikiquote, random

MAX_QUOTES_LENGTH = 100

GENIUS = [ "Leonardo da Vinci", 
			"Isaac Newton", 
			"Albert Einstein", 
			"Martha Stewart",
			"J. K. Rowling",
			"Marie Curie",
			"Hedy Lamarr",
			"Charles Darwin",
			"Archimedes",
			"Wolfgang Amadeus Mozart",
			"Galileo Galilei",
			"Aristotle", 
			"Plato", 
			"Nikola Tesla", 
			"William Shakespeare", 
			"Socrates", 
			"Stephen Hawking", 
			"Friedrich Nietzsche", 
			"Confucius", 
			"Voltaire", 
			"René Descartes", 
			"Johannes Kepler", 
			"Steve Jobs", 
			"Louis Pasteur", 
			"Sun Tzu", 
			"Sophocles", 
			"Abraham Lincoln", 
			"Edgar Allan Poe", 
			"Charles Dickens", 
			"George Orwell", 
			"Martin Luther King, Jr.", 
			"Sigmund Freud", 
			"Gautama Buddha",  
			"Jules Verne", 
			"Mahatma Gandhi", 
			"Oscar Wilde"
]

#print(wikiquote.quote_of_the_day(lang='en')) 
#print(wikiquotes.random_quote("Aristotle", "english"))

def test():
	j = 0
	for i in range(len(GENIUS)):
		quotes = wikiquote.quotes(GENIUS[i], "en")
		for quote in quotes:
			if len(quote)<= MAX_QUOTES_LENGTH:
				j+=1
		print("%s passed", i)
	print("Total available citations = %s", j)
	#1177

def getCitations():
	search = True
	while(search):
		index = random.randint(0, len(GENIUS)-1)
		quotes = wikiquote.quotes(GENIUS[index], "en")
		random.shuffle(quotes)	
		i=0;
		for quote in quotes:
			if len(quote)<= MAX_QUOTES_LENGTH:
				print( "\"" + quote + "\"")
				print(" -- [" + GENIUS[index] + "]")
				search = False
				break
			#else:
			#	print("Bypass [%s]  #%s" % (GENIUS[index], i))
			
			i+=1

def saveCitations():
	# For an online use : save in a json file and use it
	print("TODO")





