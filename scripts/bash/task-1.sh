HADOOP="$HOME/simplehadoop"
PROJECT="$HOME/Documents/hadoop-project"

cd $HADOOP

#Running task for ngrams of size GSIZE

bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-D mapreduce.job.running.map.tasks=2 \
-D mapreduce.job.reduce.slowstart.completedmaps=0.05 \
-D mapred.reduce.tasks=1 \
-file $PROJECT/scripts/python/map_1.py -mapper  "python3 map_1.py $1"  \
-file $PROJECT/scripts/python/reduce_1.py -combiner "python3 reduce_1.py" \
-file $PROJECT/scripts/python/reduce_1.py -reducer "python3 reduce_1.py" \
-input data/ldv_clean.txt \
-output "out-$2"