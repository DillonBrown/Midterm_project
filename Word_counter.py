__author__ = 'SFU'
import string

# reads the txt file, converts it to lower case, deletes punctuation and double hyphens, then splits it into an array
words = open('data/speech.txt').read().lower().replace(string.punctuation, "").replace("--", "").split()

# Get the set of unique words.
uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

# Make a list of (count, unique) tuples.
counts = []
for unique in uniques:
  count = 0              # Initialize the count to zero.

  for word in words:     # Iterate over the words.
    if word == unique:   # Is this word equal to the current unique?
      count += 1         # If so, increment the count
  counts.append((count, unique))

counts.sort()            # Sorting the list puts the lowest counts first.
counts.reverse()         # Reverse it, putting the highest counts first.
# Print the fifteen words with the highest counts.
for i in range(min(15, len(counts))):
  count, word = counts[i]
  print('%s appeared %d times' % (word, count))