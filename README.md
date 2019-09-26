# Inference-Engine-for-Hidden-Markov-Model
In this model, there
are a sequence of latent(unobserved) random variables {R0,R1,...,RT} which
represent if it is raining outside and a sequence of observed random variables
(evidence) {U0;U1,...,UT}  indicating whether the director arriving with an umbrella. Here, we use Rt = True denotes raining and Ut = True represents that an umbrella is observed. We deine the following probabilities:

P(R0 = True) = 0.2

P(Rt = True|Rt-1 = True) = 0.7

P(Rt = True|Rt-1 = False) = 0.3

P(Ut = True|Rt = True) = 0.9

P(Ut = True|Rt = False) = 0.2

We are interested in estimating the distribution of P(RT jU0;U1,...,UT ). To
calculate this distribution, you are required to use both likelihood weighted
sampling method and Gibbs sampling method to perform the approximate in-
ference.

Solution:
Approximate Inference:
			Here two methods are used to estimate the inference Likelihood weighted sampling method and Gibbs sampling method. This two methods estimate the distribution for P(RT|U0,U1,...,UT),for both RT=true and RT=false.
Observation file means evidence (umbrella) is given from which we need to find out the probability of raining (approximate inference)    
Likelihood Sampling Method:
			First we randomly need to make one sample and depending on the previous state for rain samples we draw the chain of rain from R0 to Rt  for which P(R0=True)=0.2 , P(Rt = True|Rt-1 = True) = 0.7P(Rt = True|Rt-1 = False) = 0.3 is given depending on that we create a samples from R0 to Rt .As we are given the observation sample so we find out the weight for each sample depending on rain sample . and after that we find out how many number of samples has the same weight so we multiply the weight by number of samples and we have many different weights for different possible samples so we sum them and we can find the probability of true and false and lastly we normalize it by "1/true  + false "so that we can get clear inference
Observation-1 Answers:			Observation-2 Answers:
0.7087   0.2913  Likelihood			0.8655   0.1345  Likelihood

Gibbs sampling Method:
			  Here we randomly make only one sample like e.g.1 1 0 and after that we loop through each and every sample for about 10000 iteration. Here for lower boundary R0 we calculate the distribution like p(R0)*p(R0+1/R0)*p(U0/R0)
and upper boundary as p(Rt/Rt-1)*p(Ut/Rt) and for other Samples between R0 and Rt we find the distribution by p(Rt/Rt-1)*p(Rt+1/Rt)*p(Ut/Rt) and here in this calculation we use property of Markov Blanket. Here for Each sample we count the number of Rt being True and number of Rt Being false and after normalizing we get Gibbs sampling distribution 

 Observation-1 Answers:			Observation-2 Answers:
 0.7072  0.2928  Gibbs		             0.8562   0.1438  Gibbs
