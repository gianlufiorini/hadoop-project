export HADOOP="$HOME/simplehadoop"
export PROJECT="$HOME/Documents/hadoop-project"

cd $PROJECT

bash scripts/bash/hadoop-start.sh #Starting hadoop
bash scripts/bash/hadoop-data.sh ldv #Cleaning data and placing them in HDFS

#Running task 1
bash scripts/bash/task-1.sh 2 1
bash scripts/bash/task-1.sh 3 2
bash scripts/bash/task-1.sh 4 3
bash scripts/bash/task-1.sh 5 4

#Running task 2
bash scripts/bash/task-2.sh 5

#Running task 3
bash scripts/bash/task-3.sh 4 10 0.02 6

#Running task 4
bash scripts/bash/task-4.sh leonardo 7

#Running 
bash scripts/bash/task-5.sh leonardo 8