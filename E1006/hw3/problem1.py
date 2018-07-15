#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:38:32 2017

@author: sharleen price spp2122
"""

def count_ngrams(file_name, n=2): 
    """
    This function reads an input file and returns a dictionary of n-gram counts.  
    file_name is a string, n is an integer. 
    The result dictionary maps n-grams to their frequency (i.e. the count of 
    how often that n-gram appears). Each n-gram key is a tuple and the count is
    an int.
    """
    f = open(file_name, "r")
    fixed_line = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # all punctuations
    count = 0
    some_dict = {}
    for line in f:
        for char in line:
            if char not in punctuations:
                fixed_line =fixed_line + char
                word_list = fixed_line.strip().replace('\n'," ").lower().split(" ")
                ngram_list = []
                for i in range(len(word_list)-n+1):
                    ngram_list.append(word_list[i:i+n])
                    
    for x in range(0,len(ngram_list)):
        count = ngram_list.count(ngram_list[x])
        item = tuple(ngram_list[x])
        some_dict[item]=count
            
    return some_dict


def single_occurences(ngram_count_dict): 
    """
    This functions takes in a dictionary (in the format produces by 
    count_ngrams) and returns a list of all ngrans with only 1 occurence.
    That is, this function should return a list of all n-grams with a count
    of 1. 
    """
    single_ngrams = []
    for key in ngram_count_dict:
        if ngram_count_dict[key] == 1:
            single_ngrams.append(key)
            
    return single_ngrams 

def most_frequent(ngram_count_dict, num = 5): 
    """
    This function takes in two parameters: 
        ngram_count_dict is a dictionary of ngram counts. 
        num denotes the number of n-grams to return.       
    This function returns a list of the num n-grams with the highest
    occurence in the file. For example if num=10, the method should 
    return the 10 most frequent ngrams in a list. 
    """
    # Hint: For this you will need to sort the information in the dict 
    # Python does not support any way of sorting dicts 
    # You will have to convert the dict into a list of (frequency, n-gram)
    # tuples, sort the list based on frequency, and return a list of the num
    # n-grams with the highest frequency. 
    # NOTE: you should NOT return the frequencies, just a list of the n-grams
    
    ngram_list = []
    for key in ngram_count_dict:
        temp = (ngram_count_dict[key], key)
        ngram_list.append(temp)
    
    new_list = sorted(ngram_list, key = lambda x: x[0], reverse = True)

    return new_list[0:num] 

def main():
    filename = "alice.txt"
    n = 2
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()


