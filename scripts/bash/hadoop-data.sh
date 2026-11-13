HADOOP="$HOME/simplehadoop"
PROJECT="$HOME/Documents/hadoop-project"

#Cleaning data
cd $PROJECT

#The name of the file to process is provided as the first positioinal argument, without the extension.
#The file to process must be placed in the /data directory before running the script
python3 scripts/python/0_ preporcessing.py ldv


cd $HADOOP

#Putting data into hdfs
bin/hadoop fs -mkdir data
bin/hadoop fs -put "$PROJECT/data/ldv.txt" data
bin/hadoop fs -put "$PROJECT/data/ldv_clean.txt" data

#listing files in data folder in HDFS
bin/hadoop fs -ls data