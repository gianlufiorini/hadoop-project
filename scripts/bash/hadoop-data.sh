HADOOP="$HOME/simplehadoop"
PROJECT="$HOME/Documents/hadoop-project"

#Cleaning data
cd $PROJECT

#The name of the file to process is provided as the first positioinal argument, without the extension.
#The file to process must be placed in the /data directory before running the script
python3 scripts/python/0_preprocessing.py $1


cd $HADOOP

#Putting data into hdfs
#Checking if data folder already exists
bin/hadoop fs -test -d data || bin/hadoop fs -mkdir data

bin/hadoop fs -test -e "data/$1.txt" || bin/hadoop fs -put "$PROJECT/data/$1.txt" data
bin/hadoop fs -test -e "data/${1}_clean.txt" || bin/hadoop fs -put "$PROJECT/data/${1}_clean.txt" data

#listing files in data folder in HDFS
bin/hadoop fs -ls data