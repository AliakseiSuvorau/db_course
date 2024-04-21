# Sharding in Sphinx

As I've already sayed many times, Sphinx is created to optimize
working with distributed databases meaning that parts of data
are on different machines. So, Sphinx supports **horizontal sharding**.

Sphinx primarily focuses on horizontal sharding and **vertical sharding** 
is not one of its features, but you can achieve similar benefits by 
carefully designing your schema and utilizing Sphinx's distributed index
capabilities. (see [Spatial Join Operator](../query_plan/query_plan.md)).

[Previous page](../recovery/recovery.md) | [Contents](../README.md) | [Next page](../data_mining_DWH_OLAP/data_mining_DWH_OLAP.md)