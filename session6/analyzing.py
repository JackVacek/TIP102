'''
As a digital nomad who writes blogs, articles, and reports regularly, 
it's important to analyze the text you produce to ensure clarity and avoid overusing certain words. 
You want to create a tool that analyzes the frequency of each word in a given text and identifies the most frequent word(s).

Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. 
Additionally, return a list of the word(s) that appear most frequently.

Assumptions:

The text is case-insensitive, so "Word" and "word" should be treated as the same word.

Punctuation should be ignored.

In case of a tie, return all words that have the highest frequency.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
import re
def word_frequency_analysis(text):
    freq = {}
    most = 0
    wordMost = []
    split_text = re.split(r'\s+|\.', text)
    text = list(filter(None, split_text))
    for word in text:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
        if freq[word] > most:
            most = freq[word]
            wordMost = [word]
        elif freq[word] == most:
            wordMost.append(word)
    return (freq, wordMost)
        
    
text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))