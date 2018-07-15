"""
Created by Sharleen Price spp2122
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. There should be 11
    columns (the "quality" column cannot be used for classificaiton).
    """
    data = np.genfromtxt(csv_filename, delimiter=';', skip_header=1, usecols = (0,1,2,3,4,5,6,7,8,9,10))
        
    return data   
    
def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. For example, 0.9 means that the training portion should contain
    90% of the data. You do not have to randomize the rows. Make sure that 
    there is no overlap. 
    """
    rows = len(dataset) * ratio
    train = dataset[:int(rows)]
    test = dataset[int(rows):]
    
    
    return (train,test)
    
    

def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    avg = sum(data[:,:])/len(data)
    return avg
    
def experiment(ww_train, rw_train, ww_test, rw_test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    
    ww_centroid = compute_centroid(ww_train)
    rw_centroid = compute_centroid(rw_train)
    
   
    list_of_typesww = []
    
    for x in range (0, len(ww_test)): #white wines only
        ww_euclidean = euclidean_distance(ww_centroid,ww_test[x])
        rw_euclidean = euclidean_distance(rw_centroid,ww_test[x])
        if ww_euclidean < rw_euclidean:
            closest_class = "white"
            list_of_typesww.append(closest_class)
        elif ww_euclidean > rw_euclidean:
            closest_class = "red"
            list_of_typesww.append(closest_class)
    
    
    
    
    list_of_typesrw = []
    
    for x in range (0, len(rw_test)): #red wines only
        ww_euclidean = euclidean_distance(ww_centroid,rw_test[x])
        rw_euclidean = euclidean_distance(rw_centroid,rw_test[x])
        if ww_euclidean < rw_euclidean:
            closest_class = "white"
            list_of_typesrw.append(closest_class)
        elif ww_euclidean > rw_euclidean:
            closest_class = "red"
            list_of_typesrw.append(closest_class)
    
    
    count = 0
    for whitewine in list_of_typesww:
        if whitewine == "white":
            count+=1
    for redwine in list_of_typesrw:
        if redwine == "red":
            count+=1
    total = (len(list_of_typesww) + len(list_of_typesrw))
    accuracy = count / total
    accuracy
    
    print("This model has {} correct preditions out of {} total preditions.".format(count,total))
    print("The accuracy is : {}".format(accuracy))
    
    return accuracy
            
    
    
def learning_curve(ww_training, rw_training, ww_test, rw_test):
    """
    Perform a series of experiments to compute and plot a learning curve.
    """
    acc_list = []
    num_list = []
    np.random.shuffle(ww_training)
    np.random.shuffle(rw_training)
    
    x=0
    if len(ww_training) < len(rw_training):
        x = len(ww_training)
    elif len(ww_training) > len(rw_training):
        x = len(rw_training)
    else:
        x = len(ww_training) #randomly chosen since they are equal length
    
    for n in range(1,x+1):
        acc = experiment(ww_training[0:n], rw_training[0:n], ww_test, rw_test)
        acc_list.append(acc)
        num_list.append(n)
    plt.style.use("fivethirtyeight")
    plt.xlabel("Number of Training Items")
    plt.ylabel("Accuracies")
    plt.plot(num_list,acc_list)
    
def cross_validation(ww_data, rw_data, k):
    """
    Perform k-fold crossvalidation on the data and print the accuracy for each
    fold. 
    """
    length_ww = len(ww_data)
    length_rw = len(rw_data)
    
    parts_ww = int(length_ww/k)
    parts_rw = int(length_rw/k)
    total = 0
    count=0
    
    for n in range(0,k): 
        test_ww =[]
        test_ww.extend(ww_data[n*parts_ww:(n+1)*parts_ww])
        test_rw =[]
        test_rw.extend(rw_data[n*parts_rw:(n+1)*parts_rw])

        if n == 0:
            train_ww = []
            train_rw = []
            train_ww.extend(ww_data[parts_ww:])
            train_rw.extend(rw_data[parts_rw:])
            accu=experiment(np.array(train_ww), np.array(train_rw), np.array(test_ww), np.array(test_rw))
            total +=accu
            count +=1
            
        elif (n+1)*parts_ww>= len(ww_data):
            train_ww = []
            train_rw = []
             
            train_ww.extend(ww_data[:n*parts_ww])
            train_rw.extend(rw_data[parts_rw:])
            accu=experiment(np.array(train_ww), np.array(train_rw), np.array(test_ww), np.array(test_rw))
            total +=accu
            count +=1

        else:
            train_ww = []
            train_rw = []
             
            train_ww.extend(ww_data[:n*parts_ww])
            train_ww.extend(ww_data[(n+1)*parts_ww:])
            train_rw.extend(rw_data[:n*parts_rw])
            train_rw.extend(rw_data[(n+1)*parts_rw:])
            accu=experiment(np.array(train_ww), np.array(train_rw), np.array(test_ww), np.array(test_rw))
            total +=accu
            count +=1
         
    average = total/count
      
    return average
    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')


    #Uncomment the following lines for step 2: 
#    ww_train, ww_test = split_data(ww_data, 0.9)
#    rw_train, rw_test = split_data(rw_data, 0.9)
#    experiment(ww_train, rw_train, ww_test, rw_test)
    
     #Uncomment the following lines for step 3
#    ww_train, ww_test = split_data(ww_data, 0.9)
#    rw_train, rw_test = split_data(rw_data, 0.9)
#    learning_curve(ww_train, rw_train, ww_test, rw_test)
    
    # Uncomment the following lines for step 4:
    k = 10
    acc = cross_validation(ww_data, rw_data, k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
    