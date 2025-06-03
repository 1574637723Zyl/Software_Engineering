# A simple improvement to the TD3_BC algorithmAdd commentMore actions
Our improvement method only made two basic modifications to TD3_BC.(1) The internal structure of the Critic network was redesigned: after each layer is fully connected, Layer Normalization is added, and "Squared Q Regularization" is introduced in the critic loss - multiplying the sum of the squares of the two Q curves by 0.01 and adding it to the MSE objective. (2) Additionally, the coefficient of the behavior cloning term was separated as an independent hyperparameter weight.

 As a result, which should be easily satisfied: python==3.8.13, torch==1.11.0, gym==0.18.3, dm-control==1.0.8, numpy==1.23.5, d4rl==1.1, mujoco-py==2.1.2.14
 We summarize the benchmark overview below. We provide two metrics for evaluating the performance of the agent, return and the normalized score, which gives

# Code StructureAdd commentMore actions
 ```
 RTD3_BC-main/
│
├── RTD3_BC.py             #  Main implementation of the RTD3_BC algorithm  
├── main.py                #  Entry script for training and running experiments  
├── test.py                #  Script for evaluation or testing purposes  
├── run_experiments.sh     #  Shell script for running batch experiments  
├── results/               #  Folder to store experimental results  
```
TD3+BC is a simple approach to offline RL where only two changes are made to TD3: (1) a weighted behavior cloning loss is added to the policy update and (2) the states are normalized. Unlike competing methods there are no changes to architecture or underlying hyperparameters. The paper can be found [here](https://arxiv.org/abs/2106.06860).

### Usage
Paper results were collected with [MuJoCo 1.50](http://www.mujoco.org/) (and [mujoco-py 1.50.1.1](https://github.com/openai/mujoco-py)) in [OpenAI gym 0.17.0](https://github.com/openai/gym) with
 # How to Run
The paper results can be reproduced by running:
```Add commentMore actions
python main.py --env walker2d-medium-v0 --seed 1
./run_experiments.sh
```

We explain some key flags below:

--env:is used to specify what the running environment is.

--seed:indicates the current seed to facilitate subsequent reproduction

# Dataset
After our code runs, it will automatically download the corresponding dataset to the directory /.d4rl/datasets/. Of course, you can also download the data from the website [data](http://rail.eecs.berkeley.edu/datasets/offline_rl/gym_mujoco/), and then create a directory /.d4rl/datasets/ to store the dataset. the [D4RL datasets](https://github.com/rail-berkeley/d4rl). Networks are trained using [PyTorch 1.4.0](https://github.com/pytorch/pytorch) and Python 3.6.
