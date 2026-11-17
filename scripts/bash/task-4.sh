# Task 4: words that follow a given word, from the most to the least frequent.
# Usage: task-4.sh <word> <output folder>
# The result is written to the HDFS folder out-<output folder>.
# Requires the HADOOP and PROJECT variables (defined in run-tasks.sh).

cd $HADOOP

#The word for which we want to return the expected following word is passed as the 1st positional argument.
#The output directory is specified as the 2nd positional argument.

bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-D mapreduce.job.running.map.tasks=2 \
-D mapreduce.job.reduce.slowstart.completedmaps=0.05 \
-D mapred.reduce.tasks=1 \
-file $PROJECT/scripts/python/map_4.py -mapper  "python3 map_4.py $1"  \
-file $PROJECT/scripts/python/reduce_2.py -combiner "python3 reduce_2.py" \
-file $PROJECT/scripts/python/reduce_4.py -reducer "python3 reduce_4.py" \
-input data/ldv_clean.txt \
-output "out-$2"
