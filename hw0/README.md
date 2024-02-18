## Home task 0

According to CAP theorem, with which part can you associate following DBMS?

* DragonFly
* ScyllaDB
* ArenadataDB

### Answer:

* DragonFly provides partition tolerance because 
when you set number the replicas more than one, the Dragonfly will automatically 
make one instance a master and the rest - its replicas. 
As these pods go down, it will automatically reconfigure
replication to maintain the desired number of replicas with one master 
available at all times. Also, DragonFly ensures data consistency before 
decommissioning the old master.
Taking into account written above one can associate DragonFly with CP 
(Consistency and Partition Tolerance). 

* ScyllaDB is based on Cassandra, which is already a part of AP group.
Also, it implements RAFT algorithm to ensure partition tolerance.
So, it can be associated with AP (Availability and Partition Tolerance).

* ArenadataDB has restore point, in which a state with verified data consistency, 
so that we can make a rollback to this point is something goes wrong. But consistency
is not provided at every moment. If a node in the cluster fails, the system can
automatically detect the failure and redirect client requests to other healthy 
nodes that contain replicas of the data. Implementing RAFT algorithm, it ensures 
tolerance to partitions. 
In conclusion, ArenadataDB can be associated with AP (Availability and Partittion tolerance).

