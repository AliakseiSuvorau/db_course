# How to interact with Sphinx?

Let's review some of the most popular tools to interact with Sphinx:

1. **SphinxAPI (Libraries)**. If Sphinx is run as a stand-alone server, it is possible to use SphinxAPI to
connect an application to it. Official implementations of the API are available for PHP, Java,
Perl, Ruby and Python languages:
    * [PHP](https://github.com/sphinxsearch/sphinx/blob/master/api/sphinxapi.php)
    * [Python](https://github.com/sphinxsearch/sphinx/blob/master/api/sphinxapi.py)
    * [Java](https://clojars.org/sphinxapi)
    * [Perl](https://manpages.org/sphinxsearch/3)
    * [API reference](https://www.nearby.org.uk/sphinx/sphinx.html#api-funcgroup-general) for Sphinx 2.0
2. [**SphinxQL**](http://sphinxsearch.com/docs/current/sphinxql-reference.html). Sphinx provides a SQL-like query language called SphinxQL, which allows users
to perform full-text searches, filter results, and execute complex queries against Sphinx indexes. 
It supports standard querying of all index types with `SELECT`, modifying RealTime indexes with `INSERT`,
`REPLACE`, and `DELETE`, and more.
3. [**Searchd**](https://manpages.ubuntu.com/manpages/bionic/man1/searchd.1.html). Sphinxsearch network daemon.
It provides a convenient interface for managing Sphinx search servers.

[Previous page](../history/history.md) | [Contents](../README.md) | [Next page](../db_engine/engine.md)