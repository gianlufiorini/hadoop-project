# (Re)starts all the Hadoop daemons (NameNode, DataNode, JobTracker, TaskTracker).
# Requires the HADOOP and PROJECT variables (defined in run-tasks.sh).

cd $HADOOP

bin/stop-all.sh #stopping all processes in case they are already running
bin/start-all.sh

jps #showing processes
