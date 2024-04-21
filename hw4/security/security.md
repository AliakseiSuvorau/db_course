# Security

Sphinx implements SHA1 (because of MySQL protocol). The developing
team explains that compatibility with various clients
(even with old ones) is the priority, and Sphinx usually is used
within a secure perimeter. So it's crucial to ensure that the data source 
itself is secure, because Sphinx is only indexing this data.

However, the developers point out: Sphinx never stores plain text 
passwords. So grabbing the passwords themselves is not possible.
Sphinx stores SHA1 hashes of the passwords. And if an attacker gains 
access to those, they can:
* access any other Sphinx or MySQL instances that use that 
hash
* attempt to reverse the hash for the password

[Previous page](../data_mining_DWH_OLAP/data_mining_DWH_OLAP.md) | [Contents](../README.md) | [Next page](../developers/developer.md)