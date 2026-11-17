# Runs the whole project: starts Hadoop, cleans the data, uploads it to HDFS
# and runs the five tasks. Results go to the HDFS folders out-1 ... out-8.export HADOOP="$HOME/simplehadoop"

export HADOOP="$HOME/simplehadoop"
export PROJECT="$HOME/Documents/hadoop-project"

# Setup
cd $PROJECT

bash scripts/bash/hadoop-start.sh #Starting hadoop
bash scripts/bash/hadoop-data.sh ldv #Cleaning data and placing them in HDFS

#Running task 1: n-grams of size 2, 3, 4, 5 (arguments: n, output folder)
bash scripts/bash/task-1.sh 2 1
bash scripts/bash/task-1.sh 3 2
bash scripts/bash/task-1.sh 4 3
bash scripts/bash/task-1.sh 5 4

#Running task 2: WordLengthCount (argument: output folder)
bash scripts/bash/task-2.sh 5

#Running task 3: top 2% letters in words of 5 to 9 letters
#(arguments: min length excluded, max length excluded, fraction, output folder)
bash scripts/bash/task-3.sh 4 10 0.02 6

#Running task 4: words following "leonardo" (arguments: word, output folder)
bash scripts/bash/task-4.sh leonardo 7

#Running task 5: sentences containing "leonardo" (arguments: word, output folder)
bash scripts/bash/task-5.sh leonardo 8
