# Distributed searching

Original [page](http://sphinxsearch.com/docs/current/distributed.html).

Sphinx has **distributed searching** capabilities. Distributed searching is 
useful to improve query latency (i.e. search time) and throughput (i.e. 
max queries/sec) in multi-server, multi-CPU or multi-core environments. 
This is essential for applications which need to search through huge 
amounts data.

The key idea is to make horizontal partition of searched data across search
nodes and then process it in parallel.

Partitioning is done manually. To do it one should:
* Setup several instances of Sphinx programs on different servers
* Make the instances index and search different parts of data
* Configure a special distributed index on some of the searchd instances
and query this index (This index only contains references to other local
and remote indexes - so it could not be directly reindexed)

When *searchd* receives a query against distributed index, it does the following:
* Connects to configured remote agents
* Issues the query
* Sequentially searches configured local indexes
* Retrieves remote agents' search results
* Merges all the results together, removing the duplicates
* Sends the merged results to client

Any searchd instance could serve both as a master (which aggregates the results)
and a slave (which only does local searching) at the same time.

[Previous page](../queries/query_lang.md) | [Contents](../README.md) | [Next page](../indexes/indexes.md)