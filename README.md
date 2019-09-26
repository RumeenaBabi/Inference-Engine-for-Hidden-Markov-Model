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
