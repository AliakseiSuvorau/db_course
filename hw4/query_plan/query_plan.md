# Query planner

[Article](https://www-users.cse.umn.edu/~mokbel/papers/gis15a.pdf).

The query planner in Sphinx is responsible on generating a query
plan for a user query, which is later executed by the query executor. In general, the query planner first generates a single-machine
logical plan, which is never executed. Then, it translates it into a
distributed physical plan which is executed in parallel. 

Sphinx introduces new query plans for both the range query and spatial join
operations, as described below.

## Range Query Plans

A range query is a query used to retrieve documents within a specified numerical range.

Formally speaking, in range query, the input is a query range *A* and a spacial
attribute *x* in a table *R*, while the output is all records *r* ∈ *R* where *r.x* 
overlaps *A*. If the input table *R* is indexed on the search column
*x*, Sphinx utilizes the spatial index to build a more efficient R-tree
search plan. This plan improves over the full scan plan by two new features:
* The early pruning feature which utilizes the global
index to prune partitions that are outside the query area.
* It uses R-tree scanners which utilize the local indexes in selected partitions 
to quickly select matching records.

## Spatial Join Plans

Here we are joining two tables.

More formally, the input is composed of two tables, *R* and *S*, with
designated geometric columns, *R.x* and *S.y*, and a spatial predicate
*θ*, such as touch or overlap. The output is a table *T* that contains all
records *t* = (*r*, *s*), where the predicate *θ* is true for (*r.x*, *s.y*), 
*r* ∈ *R*, and *s* ∈ *S*. Sphinx introduces 3 alternative physical plans
based on whether the two tables are indexed, one table is indexed, or none 
of them are indexed:

* **Overlap Join**. This plan is used if the two input tables are indexed on 
the join columns. The basic idea is to find pairs of overlapping partitions 
and perform a single machine spatial join between every pair of partitions. 
To realize this plan, Sphinx introduces the novel spatial multicast connection
patterns which creates a communication stream between every pair
of machines which are assigned overlapping partitions. To join a
pair of partitions, Sphinx uses the spatial join operator. 

* **Partition Join**. This plan is employed
if only one input table is indexed. In this case, the non-indexed
table, say *R*, is partitioned to match the other (indexed) table. Once
the table *R* is partitioned, there will be a one-to-one correspondence
between the partitions of *R* and *S* where each pair of partitions are
joined using the spatial join operator.

* **Co-partition Join**. If none of the input files are indexed,
sphinx employs the co-partition join. In this plan both input files are 
partitioned using a common uniform grid, and the contents of each grid cell 
from the two files are spatially joined.

### R-tree

The R-tree scanner takes as input one locally-indexed partition
*P* and a rectangular query range *A*, and returns all records in *P* that
overlap *A*. The R-tree scanner starts by computing the estimated
selectivity *s*. Based on the selectivity, the R-tree scanner has three modes
of operation:

* **Match All**: If the *P* is completely contained in
*A*, all records are added to the answer without testing them against
the query *A*.

* **Full Scan**: If the selectivity is
larger than a threshold, the R-tree scanner skips the
index and compares each record against the query range *A*. 

* **R-tree search**: If the selectivity is lower than the threshold, the R-tree
index is utilized to quickly retrieve matching records.

### Spatial Join Operator

The spatial join operator joins two partitions P1 and P2 retrieved from 
the two input files and returns every pair of overlapping records in the 
two partitions. This operator has three
modes of execution based on the local indexes in the two joined
partitions:

* **R-tree Join**: If both partitions are locally indexed using Rtree, this 
execution mode the synchronized traversal algorithm
to concurrently traverse both trees while pruning disjoint tree
nodes.

* **Bulk Index Join**: If only one partition is locally indexed, this execution mode 
uses the bulk index join algorithm which partitions the non-indexed 
partition according to the R-tree
of the indexed partition, and then joins each pair of corresponding partitions.

* **Plane-sweep Join**: If none of the partitions are
indexed, the spatial join operator performs a plane-sweep join algorithm
which works efficiently with non-indexed data.

[Previous page](../query_exec/query_exec.md) | [Contents](../README.md) | [Next page](../transactions/transactions.md)