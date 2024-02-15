from pyspark import SparkConf, SparkContext
import sys

# Initialize Spark configuration
conf = SparkConf()
sc = SparkContext(conf=conf)

# Read input text file and split it into words
words = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
words_w_idx = words.zipWithIndex() # (the, 0), (anarchy, 1), (of, 2)
shifted_right = words_w_idx.map(lambda x: (x[1]-1, x[0])) 
original_words = words_w_idx.map(lambda x: (x[1], x[0]))
joined_words = original_words.join(shifted_right)
bigrams = joined_words.map(lambda x: ((x[1][0], x[1][1]), 1)).reduceByKey(lambda a, b: a+b)
bigram_counts = bigrams.map(lambda x: (x[0][0], (x[0][1], x[1])))


joined_bigram_word_counts = bigram_counts.join(word_counts)
bigram_dist = joined_bigram_word_counts.map(lambda x: ((x[0], x[1][0][0]), x[1][0][1]/x[1][1]))
bigram_counts = joined_bigram_word_counts.map(lambda x: ((x[0], x[1][0][0]), x[1][0][1]))

bigram_dist.coalesce(1).saveAsTextFile('output/bigrams_dist')
bigram_counts.coalesce(1).saveAsTextFile('output/bigrams_counts')
sc.stop()
