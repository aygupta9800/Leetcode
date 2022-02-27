// Kafka: It is a distributed system which we used for pub sub messaging system.

// Feature	Description
// High Throughput:	Support for millions of messages with modest hardware
// Scalability:	Highly scalable distributed systems with no downtime
// Replication:	Messages are replicated across the cluster to provide support for multiple subscribers and balances the consumers in case of failures
// Durability:	Provides support for persistence of message to disk
// Stream Processing:	Used with real-time streaming applications like Apache Spark & Storm
// Data Loss:	Kafka with proper configurations can ensure zero data loss

// componenets of kafka
// Topic – a stream of messages belonging to the same type
// Producer – that can publish messages to a topic
// Consumer – that subscribes to various topics and pulls data from the brokers.
// Brokers – a set of servers where the publishes messages are stored.
// A Kafka broker is a server that works as part of a Kafka cluster (in other words, a Kafka cluster is made up of a number of brokers). Multiple brokers typically work together to build a Kafka cluster, which provides load balancing, reliable redundancy, and failover. The cluster is managed and coordinated by brokers using Apache ZooKeeper. 
// ZooKeeper is also used by Kafka brokers for leader elections, in which a broker is chosen to lead the handling of client requests for a certain partition of a topic.
// Kafka uses Zookeeper to store offsets of messages consumed for a specific topic and partition by a specific Consumer Group.


// A minimum of three brokers should be used to achieve reliable failover; the higher the number of brokers, the more reliable the failover.

// offset
// messages contained in the partitions are assigned a unique ID number that is called the offset. The role of the offset is to uniquely identify every message within the partition.

// 7. Explain the concept of Leader and Follower.
// Every partition in Kafka has one server which plays the role of a Leader, and none or more servers that act as Followers. The Leader performs the task of all read and write requests for the partition, while the role of the Followers is to passively replicate the leader. In the event of the Leader failing, one of the Followers will take on the role of the Leader. This ensures load balancing of the server.

// 8. What roles do Replicas and the ISR play?
// Replicas are essentially a list of nodes that replicate the log for a particular partition irrespective of whether they play the role of the Leader. On the other hand, ISR stands for In-Sync Replicas. It is essentially a set of message replicas that are synced to the leaders.



