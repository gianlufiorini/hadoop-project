# Task 2: WordLengthCount, number of words of each length.
# Usage: task-2.sh <output folder>
# The result is written to the HDFS folder out-<output folder>.
# Requires the HADOOP and PROJECT variables (defined in run-tasks.sh).

cd $HADOOP

#The output directory is specified as the 1st positional argument.

bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-D mapreduce.job.running.map.tasks=2 \
-D mapreduce.job.reduce.slowstart.completedmaps=0.05 \
-D mapred.reduce.tasks=1 \
-file $PROJECT/scripts/python/map_2.py -mapper  "python3 map_2.py"  \
-file $PROJECT/scripts/python/reduce_2.py -combiner "python3 reduce_2.py" \
-file $PROJECT/scripts/python/reduce_2.py -reducer "python3 reduce_2.py" \
-input data/ldv_clean.txt \
-output "out-$1"
