HADOOP="$HOME/simplehadoop"
PROJECT="$HOME/Documents/hadoop-project"

cd $HADOOP

#Putting data into hdfs
bin/hadoop fs -mkdir data
bin/hadoop fs -put "$PROJECT/data/ldv.txt" data
bin/hadoop fs -put "$PROJECT/data/ldv_clean.txt" data

#listing files in data folder in HDFS
bin/hadoop fs -ls data