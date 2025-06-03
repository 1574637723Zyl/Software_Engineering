# A simple improvement to the TD3_BC algorithm
Our improvement method only made two basic modifications to TD3_BC.(1) The internal structure of the Critic network was redesigned: after each layer is fully connected, Layer Normalization is added, and "Squared Q Regularization" is introduced in the critic loss - multiplying the sum of the squares of the two Q curves by 0.01 and adding it to the MSE objective. (2) Additionally, the coefficient of the behavior cloning term was separated as an independent hyperparameter weight.
# use
 As a result, which should be easily satisfied: python==3.8.13, torch==1.11.0, gym==0.18.3, dm-control==1.0.8, numpy==1.23.5, d4rl==1.1, mujoco-py==2.1.2.14
 We summarize the benchmark overview below. We provide two metrics for evaluating the performance of the agent, return and the normalized score, which gives

 # Code Structure
 

 # How to Run
```
python main.py --env walker2d-medium-v0 --seed 1
```

We explain some key flags below:
--env:is used to specify what the running environment is.
--seed:indicates the current seed to facilitate subsequent reproduction
