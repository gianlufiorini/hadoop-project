HADOOP="$HOME/simplehadoop"
PROJECT="$HOME/Documents/hadoop-project"

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