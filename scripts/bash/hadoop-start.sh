HADOOP="$HOME/simplehadoop"
PROJECT="$HOME/Documents/hadoop-project"

cd $HADOOP
bin/stop-all.sh #stopping all processes in case they are already running
bin/start-all.sh

jps #showing processes