# Query working out process

The query executor is the component that executes the physical
query plans, created by the query planner, in the distributed environment.

Work with a query is divided into several stages:

0. **Data Indexing**: Before queries can be executed, the data needs to be
indexed. This stage involves creating an index data structure.
1. **Query Analysis**: After a client has sent a query, a Sphinx server analyzes
and parses it, and determines what tokens or keywords it contains. It also 
includes data normalization such as converting all letters to lowercase, 
removing punctuation, or stripping accents from characters. It includes
use of built-in morphology and text-processing tools.
2. **Searching the Index**: Sphinx queries the index to find matches to the query.
3. **Ranking**: After Sphinx retrieves matching documents for a query, it may need to rank
these results to determine their relevance to the query. You can even look at the weights 
Sphinx has given to each record by looking at `weight` attribute.
4. **Sending the results to the client**.

[Previous page](../indexes/indexes.md) | [Contents](../README.md) | [Next page](../query_plan/query_plan.md)