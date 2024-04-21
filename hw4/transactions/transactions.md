# Transactions in Sphinx

Sphinx involves transactions, particularly when it comes to 
indexing and searching data. 

* In the context of indexing, Sphinx performs transactions 
when adding, updating, or deleting documents from its index.
These operations ensure data consistency and integrity within
the index.

* When performing searches, Sphinx may handle transactions
to ensure that the search results are accurate and up-to-date,
especially in scenarios where real-time data retrieval is 
crucial.

[Previous page](../query_plan/query_plan.md) | [Contents](../README.md) | [Next page](../recovery/recovery.md)