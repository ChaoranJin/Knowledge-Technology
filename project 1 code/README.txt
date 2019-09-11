1.In the edit distance python file, editdistance is imported from edit distance python library. The strings are read from the file misspell and then written into a list. The same process is made to correct file and dict file. 
In the for loop, compare each token from the list with dict list, and the distance will be returned and written into a new list. Find out the smallest value in the distance list and the strings with it will be written into the prediction candidates list. Then a list of candidate strings will be provided. 
The number of candidates for each token, that is length of each candidate list, will be calculated as candidateTotal. At the same time, the this list contains the correct form of token, the precisionTotal will be added 1.
Repeat the steps until all the tokens are compared with the strings in dict file.
According to the definition of recall and precision, the results will be returned after calculation.

2.In the modified GED python file, the strings are read from the file misspell and then written into a list. The same process is made to correct file and dict file. 
In the for loop, compare each token from the list with dict list. The tokens and strings in the dict file are separated as single characters. When comparing these characters, score will be given to each comparison. +1 for a match, -1 for insertion one character, -5 for deletion or replacement of one character. For each comparison, the largest number will be returned as distance written into value list. Find out the largest value for the token, then the strings with it will be the candidates written into candidate list.
The number of candidates for each token, that is length of each candidate list, will be calculated as candidateTotal. At the same time, the this list contains the correct form of token, the precisionTotal will be added 1.
Repeat the steps until all the tokens are compared with the strings in dict file.
According to the definition of recall and precision, the results will be returned after calculation.

3. In the ngram python file, QGram is imported from similarity python library. Set up the parameter of n before the program runs.
he strings are read from the file misspell and then written into a list. The same process is made to correct file and dict file. 
In the for loop, compare each token from the list with dict list, and the distance will be returned and written into the value list. Find out the smallest value in the distance list and the strings with it will be written into the prediction candidates list. Then a list of candidate strings will be provided.
The number of candidates for each token, that is length of each candidate list, will be calculated as candidateTotal. At the same time, the this list contains the correct form of token, the precisionTotal will be added 1.
Repeat the steps until all the tokens are compared with the strings in dict file.
According to the definition of recall and precision, the results will be returned after calculation.

4. In the improvement python file, QGram is imported from similarity python library. Set up the parameter of n before the program runs.
The strings are read from the file misspell and then written into a list. The same process is made to correct file and dict file. 
In the for loop, compare each token from the list with dict list. The tokens and strings in the dict file are separated as single characters. When comparing these characters, score will be given to each comparison. +1 for a match, -1 for insertion one character, -5 for deletion or replacement of one character. For each comparison, the largest number will be returned as distance written into value list. Find out the largest value for the token, then the strings with it will be the candidates written into candidate list.
Then n-grams is deployed to compare the tokens with candidates in the candidate list.The distance will be returned and written into the value1 list. Find out the smallest value in the distance list and the strings with it will be written into the prediction candidates list. Then a list of candidate strings will be provided into prediction list.
The number of candidates for each token, that is length of each prediction list, will be calculated as candidateTotal. At the same time, the this list contains the correct form of token, the precisionTotal will be added 1.
Repeat the steps until all the tokens are compared with the strings in dict file.
According to the definition of recall and precision, the results will be returned after calculation.
 