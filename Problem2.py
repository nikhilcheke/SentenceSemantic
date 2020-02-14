"""
Two values in this code are manually set
1. Value of alpha(0.001) in SIF
2. Threshold value(0.81) for grouping similar sentences together

Also,
Changing the glove(word embedding) file i.e. size of word embeddings will affect the result
"""


from nltk.tokenize import word_tokenize
import numpy as np
from scipy import spatial
   
# this function returns sentence embeddings using Smooth Inverse Frequency(SIF) approach
def returnEmbd(sent,word2vec,a,wordCount,totalCount):
    embedding = []
    for word in sent:
        pw = wordCount[word]/totalCount
        wemd = np.array(word2vec[word])*(a/(a+pw))
        embedding.append(wemd)
     
    return embedding


word2vec = {}
# reading word embedings using glove
# location for file is https://nlp.stanford.edu/projects/glove/
# result can vary with selected glove file because of the word embedding size, here it is 50. 100,200,300 are the options for the same
with open('/Users/nikhildattatraya.c/Downloads/glove.6B/glove.6B.50d.txt', encoding='utf-8') as f:
  for line in f:
    values = line.split()
    word = values[0]
    vec = np.asarray(values[1:], dtype='float32')
    word2vec[word] = vec


sentences = []
wordCount = {}
totalCount = 0
# reading sentence data from file, calculating word count for every word in the corpus
with open('/Users/nikhildattatraya.c/Downloads/list_of_sentences', encoding='utf-8') as f:
  for line in f:
      line = line.lower()
      sentences.append(line)
      for word in word_tokenize(line):
          if word in wordCount:
              wordCount[word] += 1
          else:
              wordCount[word] = 1
          totalCount += 1

# value of alpha in SIF
alpha = 0.001
SentEmbd = {}
for line in sentences:
    sent = word_tokenize(line.strip())
    embedding = np.array(returnEmbd(sent,word2vec,alpha,wordCount,totalCount))
    finalEmbd = np.array(np.mean(embedding, axis=0))
    SentEmbd[line] = finalEmbd
    

similarSent = {}
for line1 in sentences:
    similarSent[line1] = []
    for line2 in sentences:
        
        #calculating cosine similarity between two sentence embeddings
        result = 1 - spatial.distance.cosine(SentEmbd[line1], SentEmbd[line2])
        
        #uncomment the following line to get the result of part1 of this problem
        #print(line1+","+line2+"similarity is "+str(result))
        
        #threshold for collection of similar sentences
        #this threshold is not fixed
        if(result > 0.81):
                similarSent[line1].append(line2)
        

similarSent1 = {}
for line1 in similarSent:
    for line2 in similarSent:
        if(set(similarSent[line1]) & set(similarSent[line2])):
            similarSent[line1] = sorted(list(set(similarSent[line1] + similarSent[line2])))
            similarSent[line2] = sorted(list(set(similarSent[line1] + similarSent[line2])))
            
result = set(tuple(tuple(w) for w in similarSent.values()))
result = [list(w) for w in result]
for i in result:
    print(i)



