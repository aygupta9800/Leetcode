// 1. Difference btw mysql and mongodb
// MySQL is a popular, free-to-use, and open-source relational database management system (RDBMS) developed by Oracle.As with other relational systems, MySQL stores data using tables and rows, enforces referential integrity and uses structured query language (SQL) for data access. When users need to retrieve data from a MySQL database, they must construct an SQL query that joins multiple tables together to create the view on the data they require.

// Database schemas and data models need to be defined ahead of time, and data must match this schema to be stored in the database. This rigid approach to storing data offers some degree of safety, but trades this for flexibility. If a new type or format of data needs to be stored in the database, schema migration must occur, which can become complex and expensive as the size of the database grows.


// MongoDB:
// MongoDB is also free to use and open source; however, its design principles differ from traditional relational systems. Often styled as a non-relational (or NoSQL) system, MongoDB adopts a significantly different approach to storing data, representing information as a series of JSON-like documents (actually stored as binary JSON, or BSON), as opposed to the table and row format of relational systems.

// MongoDB documents consist of a series of key/value pairs of varying types, including arrays and nested documents; however, the key difference is that the structure of the key/value pairs in a given collection can vary from document to document. This more flexible approach is possible because documents are self-describing.

// 2. When to use mongodb vs mysql
// The core differences between these two database systems are significant. Choosing which one to use is really a question of approach rather than purely a technical decision.
// a.
// MySQL is a mature relational database system, offering a familiar database environment for experienced IT professionals.

// MongoDB is a well-established, non-relational database system offering improved flexibility and horizontal scalability, but at the cost of some safety features of relational databases, such as referential integrity.

//b. Based on user friendliness
// MongoDB stores data in collections with no enforced schema. This flexible approach to storing data makes it particularly suitable for developers who may not be database experts, yet want to use a database to support the development of their applications.
// Compared to MySQL, this flexibility is a significant advantage: To get the best out of a relational database, you must first understand the principles of normalization, referential integrity, and relational database design.
// MongoDB provides a flexible developer interface for teams that are building applications that don’t need all of the safety features offered by relational systems. A common example of such an application is a web application that doesn't depend on structured schemas; it can easily serve unstructured, semi-structured, or structured data, all from the same MongoDB collection.

//MySQL is a common choice for users who have extensive experience using traditional SQL scripting, designing solutions for relational databases, or who are modifying or updating existing applications that already work with a relational system. Relational databases may also be a better choice for applications that require very complex but rigid data structures and database schemas across a large number of tables.
// A common example of such a system could be a banking application that requires very strong referential integrity and transactional guarantees to be enforced to maintain exact point-in-time integrity of data.

// c. Based on scalability.
// A key benefit of the MongoDB design is that the database is extremely easy to scale. Configuring a sharded cluster allows a portion of the database, called a shard, to also be configured as a replica set. In a sharded cluster, data is distributed across many servers. This highly flexible approach allows MongoDB to horizontally scale both read and write performance to cater to applications of any scale.
// A replica set is the replication of a group of MongoDB servers that hold the same data, ensuring high availability and disaster recovery.

// With a MySQL database system, options for scalability are much more limited. Typically, you have two choices: vertical scalability, or adding read replicas. Scaling vertically involves adding more resources to the existing database server, but this has an inherent upper limit.

// Read replication involves adding read-only copies of the database to other servers. However, this is typically limited to five replicas in total, which can only be used for read operations. This can cause issues with applications that are either write-heavy, or write and read regularly for the database, since it’s common for replicas to lag behind the write master. Multi-master replication support has been added to MySQL, but its implementation is more limited than the functionality available in MongoDB.

// d. Performance
// Assessing the performance of two completely different database systems is very difficult, since both management systems approach the task for data storage and retrieval in completely different ways
// For example: MySQL is optimized for high performance joins across multiple tables that have been appropriately indexed. In MongoDB, joins are supported with the $lookup operation, but they are less needed due to the way MongoDB documents tend to be used; they follow a hierarchical data model and keep most of the data in one document, therefore eliminating the need for joins across multiple documents.

// MongoDB is also optimized for write performance, and features a specific insertMany() API for rapidly inserting data, prioritizing speed over transaction safety wherein MySQL data needs to be inserted row by row.

// Observing some of the high-level query behaviors of the two systems, we can see that MySQL is faster at selecting a large number of records, while MongoDB is significantly faster at inserting or updating a large number of records.

//e. flexibility
// This is an easy one, and a hands down win for MongoDB. The schemaless design of MongoDB documents makes it extremely easy to build and enhance applications over time, without needing to run complex and expensive schema migration processes as you would with a relational database.

//f. security
// MongoDB leverages the popular role-based access control model with a flexible set of permissions. Users are assigned to a role, and that role grants them specific permissions over data sets and database operations. All communication is encrypted with TLS, and it’s possible to write encrypted documents to MongoDB data collections using a master key which is never available to MongoDB, achieving encryption of data at rest.

// MySQL supports the same encryption features as MongoDB; its authentication model is also similar. Users can be granted roles but also privileges, giving them permissions over particular database operations and against particular data sets.





