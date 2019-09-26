#Artificial Intelligence
#Assignment-3
#Likelyhood and Gibbs sampling
import sys
import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#this function will return the length of the observation sample
def retrun_len():
	n=[ ]
	for line in data:
		if line.strip():
			n.append(int(line))
	a=len(n)
	return a


#this function will find the probability of rain samples
def find_probability_rain():
	n=retrun_len()#take length
	probability=[]
	pos=0
	sample=10000
	for i in range(0,sample):#generate for 10000 samples
		pos=0
		j=0
		probability.append([])
		if j==0: #if the first r0 then it is fixed 0.2 and 0.8
			toss=np.random.choice([1,0], p=[0.2,0.8])
			if(toss==1): #append the probability of first sample
				probability[i].append(1)
			else:
				 probability[i].append(0)
			pos=pos+1;
		#find different probabability of rain depending on it's previous rain sample
		j=1
		while(j!=n):
			if(probability[i][j-1]==1):
					toss=toss=np.random.choice([1,0], p=[0.7,0.3])
					if(toss==1):
							probability[i].append(1)
					else:
							probability[i].append(0)
			else:
					toss=toss=np.random.choice([1,0], p=[0.3,0.7])
					if(toss==1):
							probability[i].append(1)
					else:
							probability[i].append(0)
			j=j+1
	return probability,sample	

#finding the probability of umbrella (weight)
def find_umbrella_probability(data,probability):
	U=[ ]
	for line in data:
		if line.strip():
			U.append(int(line))
	weight=[]
	w=1;
	n=retrun_len()
	for i in range(0,sample):
			w=1
			j=0
			while j!=n:
				if probability[i][j]==1 and U[j]==1:
					w=w*0.9
				elif probability[i][j]==1 and U[j]==0:
					w=w*0.1
				elif probability[i][j]==0 and U[j]==1:
					w=w*0.2
				else:	
					w=w*0.8
				j=j+1
			weight.append(w)
	return weight

#it will check how many samples has the 
#same probability to calculate the weight*number of sample
def find_present(prob,find_sample):
	if(len(find_sample)==0):
		return True
	for i in range(0,len(find_sample)):
		if(prob==find_sample[i]):
			return	False
	return True

#thos function will find the number of samples having the same weight
def find_pairs(probability,weight):
	find_sample=[]
	count=0
	key=probability[0]
	counter_sample=[]
	weight_sample=[]
	for j in range(0,len(probability)):
			count=0
			check_list=find_present(probability[j],find_sample)
			if check_list==True:
				for i in range(j,len(probability)):
					if probability[j]==probability[i]:
						count=count+1
						if count == 1:
							find_sample.append(probability[j])
							weight_sample.append(weight[j])
				counter_sample.append(count)		
	return find_sample,weight_sample,counter_sample	

#it will find the likelyhood sampling distribution		
def likelyhood(find_sample,weight_sample,counter_sample):
		n=retrun_len()
		sum_it_true=0
		calculate=1
		#calculate true probability
		for i in range(0,len(find_sample)):
			if(find_sample[i][n-1]==1):
					calculate=weight_sample[i]*counter_sample[i]
					sum_it_true=sum_it_true+calculate
					
		plt.show()						 
		#calculate false probability
		sum_it_false=0
		flase_probability=[]
		for i in range(0,len(find_sample)):
			if(find_sample[i][n-1]==0):
					calculate=weight_sample[i]*counter_sample[i]
					sum_it_false=sum_it_false+calculate	
		true=sum_it_true/(sum_it_true+sum_it_false)
		false=sum_it_false/(sum_it_true+sum_it_false)
		print(true,false, "Likelihood")	

#GIBBS SAMPLING
#this function will generate first sample 
def generate_first_sample(data):
	sample=[]
	n=retrun_len()
	random_choice=random.randint(0,1)
	j=0
	while j != n:
		if random_choice == 1:
			sample.append(1)
		else:
			sample.append(0)
		random_choice=random.randint(0,1)
		j=j+1
	return sample
#this function will find the probability of rain for R0
def lower_boundary(random_choice,sample_one):
	cal=1
	n=[ ]
	for line in data:
		if line.strip():
			n.append(int(line))
	#TRUE PROBABILITY
	sample_one[random_choice]=1
	#current
	cal=cal*0.2
	#next
	if sample_one[random_choice+1]==1:
		cal=cal*0.7
	else:
		cal=cal*0.3
	#umbrella
	if n[random_choice]==1:
		cal=cal*0.9
	else:
		cal=cal*0.1
	#FALSE PROBILITY
	false_cal=1
	sample_one[random_choice]=0
	#current	
	false_cal=false_cal*0.8
	#next
	if sample_one[random_choice+1]==1:
		false_cal=false_cal*0.3
	else:
		false_cal=false_cal*0.7
	#umbrella
	if n[random_choice]==1:
		false_cal=false_cal*0.2
	else:
		false_cal=false_cal*0.8
	#CALCULATE PROBABILITY
	true_prob=cal/(cal + false_cal)
	false_prob=false_cal/(cal+false_cal)
	#TOSS AND DECIDE TRUE OR FALSE DEPENDING ON DISTRIBUTION
	random_toss=np.random.choice([1,0], p=[true_prob,false_prob])
	return random_toss

	
#this function will find the distribution for last sample of rain RT
def upper_bound(random_choice,sample_one):
	cal=1
	n=[ ]
	for line in data:
		if line.strip():
			n.append(int(line))
	#TRUE PROBABILITY
	sample_one[random_choice]=1
	#last one (current)
	if sample_one[random_choice-1]==1:
		cal=cal*0.7
	else:
		cal=cal*0.3
	#umbrella
	if n[random_choice]==1:
		cal=cal*0.9
	else:
		cal=cal*0.1
	#FALSE PROBABILITY
	false_cal=1
	sample_one[random_choice]=0
	#last one (current)
	if sample_one[random_choice-1]==1:
		false_cal=false_cal*0.3
	else:
		false_cal=false_cal*0.7
	#umbrella
	if n[random_choice]==1:
		false_cal=false_cal*0.2
	else:
		false_cal=false_cal*0.8
	#FIND PROBABILITY
	true_prob=cal/(cal + false_cal)
	false_prob=false_cal/(cal+false_cal)
	random_toss=np.random.choice([1,0], p=[true_prob,false_prob])
	return random_toss
#this function will find the distribution for rain sample between
#R0 and Rt
def general(random_choice,sample_one):
	cal=1
	n=[ ]
	for line in data:
		if line.strip():
			n.append(int(line))
	#TRUE PROBABILITY
	sample_one[random_choice]=1
	#current
	if sample_one[random_choice-1]==1:
		cal=cal*0.7
	else:
		cal=cal*0.3
	#next_one
	if sample_one[random_choice+1]==1:
		cal=cal*0.7
	else:
		cal=cal*0.3
	#umbrella	
	if n[random_choice]==1:
		cal=cal*0.9
	else:
		cal=cal*0.1

	#FALSE PROBABILITY
	false_cal=1
	sample_one[random_choice]=0
	#current
	if sample_one[random_choice-1]==1:
		false_cal=false_cal*0.3
	else:
		false_cal=false_cal*0.7
	#next_one
	if sample_one[random_choice+1]==1:
		false_cal=false_cal*0.3
	else:
		false_cal=false_cal*0.7
	#umbrella
	if n[random_choice]==1:
		false_cal=false_cal*0.2
	else:
		false_cal=false_cal*0.8
	
	#FIND THE PROBABILITY
	true_prob=cal/(cal + false_cal)
	false_prob=false_cal/(cal+false_cal)
	random_toss=np.random.choice([1,0], p=[true_prob,false_prob])
	return random_toss

#GIBBS SAMPLER
def gibbs(sample_one):
		n=retrun_len()#Length of the observation sample 
		random_count=0
		count=0
		false_count=0
		for i in range (0,10000):
				#for first R0
				random_choice=0
				random_count=lower_boundary(random_choice,sample_one)
				if random_count == 1:
					sample_one[random_choice]=1
				else:
					sample_one[random_choice]=0
				#Between R0 and Rt
				j=1
				while j <n-1:
					random_choice=j
					random_count=general(random_choice,sample_one)
					if random_count == 1:
						sample_one[random_choice]=1
					else:
						sample_one[random_choice]=0
					j=j+1

				#for Rt
				random_choice=n-1
				random_count=upper_bound(random_choice,sample_one)
				if random_count == 1:
					sample_one[random_choice]=1

				else:
					sample_one[random_choice]=0
				
				#count true and false sample to find the gibbs sample
				if sample_one[n-1]==1:
					count=count+1 #true
				else:
					false_count=false_count+1#false

				true=count/(count+false_count)
				false=false_count/(count+false_count)
				
		print(true , false , "Gibbs")
		

#program will start from here		
with open(sys.argv[1],'r')as my_file:
	#LIKELYHOOD
	#read the data from file
	data=my_file.read()
	#lilkelyhood rain probability
	probability,sample=find_probability_rain()
	#find weight
	weight=find_umbrella_probability(data,probability)
	#find the pairs which has the same weight
	find_sample	,weight_sample,counter_sample=find_pairs(probability,weight)
	#likelyhood
	likelyhood(find_sample,weight_sample,counter_sample)

	#GIBBS
	#first sample
	sample_one=generate_first_sample(data)
	#gibbs sampling
	gibbs(sample_one)