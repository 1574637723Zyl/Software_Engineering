#!/bin/bash

# Script to reproduce results

envs=(
	"halfcheetah-random-v0"
	"hopper-random-v0"
	"walker2d-random-v0"
	# "halfcheetah-medium-v0"
	# "hopper-medium-v0"
	# "walker2d-medium-v0"
	#"halfcheetah-expert-v0"
	# "hopper-expert-v0"
	# "walker2d-expert-v0"
	# "halfcheetah-medium-expert-v0"
	# "hopper-medium-expert-v0"
	# "walker2d-medium-expert-v0"
	)
# "halfcheetah-medium-replay-v0"
# "hopper-medium-replay-v0"
# "walker2d-medium-replay-v0"

for ((i=0;i<2;i+=1))
do 
    python main.py --env halfcheetah-medium-v0 --seed $i &
	python main.py --env hopper-medium-v0 --seed $i &
	python main.py --env walker2d-medium-v0 --seed $i &
done

# ./run_experiments.sh
# chmod +x run_experiments.sh