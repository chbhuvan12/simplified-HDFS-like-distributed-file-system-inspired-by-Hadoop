A Simplified Hadoop Distributed File System (HDFS) Implementation
📌 Overview

Mini-HDFS is a lightweight, educational implementation of the Hadoop Distributed File System (HDFS) written in Python.
It demonstrates the core concepts of distributed storage such as file splitting, replication, metadata management, and fault tolerance in a simplified manner.

This project is intended for learning and experimentation


🎯 Key Objectives

Understand how HDFS works internally

Learn distributed file storage concepts

Simulate NameNode and DataNode behavior

Practice system design fundamentals

🏗 Architecture

Mini-HDFS follows the basic HDFS architecture:

🔹 NameNode

Maintains metadata

Tracks file names, block locations, and replicas

Decides where blocks are stored

🔹 DataNodes

Store actual file blocks

Handle read/write operations

Report status to the NameNode
