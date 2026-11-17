# Task 3: most used letters in words whose length is strictly between min and max.
# Usage: task-3.sh <min> <max> <fraction> <output folder>   (e.g. 4 10 0.02 for the top 2%)
# The result is written to the HDFS folder out-<output folder>.
# Requires the HADOOP and PROJECT variables (defined in run-tasks.sh).

cd $HADOOP

#The minimum number of letters to consider is specified as the 1st positional argument.
#The maximum number of letters to consider is specified as the 2nd positional argument.
#The percentage of top letters to report is specified as the 3rd positional argument.
#The output directory is specified as the 4th positional argument.

bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-D mapreduce.job.running.map.tasks=2 \
-D mapreduce.job.reduce.slowstart.completedmaps=0.05 \
-D mapred.reduce.tasks=1 \
-file $PROJECT/scripts/python/map_3.py -mapper  "python3 map_3.py $1 $2"  \
-file $PROJECT/scripts/python/reduce_2.py -combiner "python3 reduce_2.py" \
-file $PROJECT/scripts/python/reduce_3.py -reducer "python3 reduce_3.py $3" \
-input data/ldv_clean.txt \
-output "out-$4"
