# Data recovery

There are some ways to recover data in Sphinx.

* **Backup and Restore**: If you have regular backups of 
your Sphinx indexes, you can restore the data from these
backups in case of data loss.
* **Delta Indexing**: If you're using delta indexing in Sphinx,
you can reindex only the data that has changed since the last
index update. This can help minimize the amount of data that
needs to be recovered in case of data loss.
* **Replication**: Sphinx is usually used in a distributed setup.
So you may be able to recover data from one of the replicas if 
the data loss is limited to a single node.

### Delta indexes

The situation often arises when the volume of data that 
needs to be indexed is too large to regularly update the 
entire index, as this can take many hours. Meanwhile, new 
data is constantly being added to the database, and it is 
necessary for it to also be included in the index. In such 
cases, delta indexes are typically used.

The idea is to create two indexes instead of one: a primary
index and a delta index. The primary index will contain all
the data and will be updated either very rarely or not 
updated at all, instead of periodically merging with the delta 
index. The delta index will contain only the data that has 
changed since the last update of the primary index. Since 
the delta index is usually significantly smaller than the 
primary index, its update can be performed much more 
frequently, and it will be executed much faster.

[Previous page](../transactions/transactions.md) | [Contents](../README.md) | [Next page](../sharding/sharding.md)