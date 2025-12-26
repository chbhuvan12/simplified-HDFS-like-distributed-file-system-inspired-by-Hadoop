.

📁 Mini-HDFS (Simplified HDFS Implementation)
Overview

Mini-HDFS is a simplified implementation of Hadoop Distributed File System (HDFS) built using Python and socket programming.
It demonstrates core distributed systems concepts such as metadata management, block storage, replication, and client–server communication.

This project is designed to be resume-worthy for Google Infra / Cloud / Distributed Systems roles.

Architecture
Client
  |
  |---- PUT / GET
  |
NameNode (Metadata)
  |
  |---- Block locations
  |
DataNodes (Storage)

Components

NameNode

Stores metadata only

Maps files → block IDs → DataNodes

DataNodes

Store actual data blocks on disk

Serve read/write requests

Client

Uploads and downloads files

Talks to NameNode first, then DataNodes

Features

Centralized metadata management (NameNode)

Distributed block storage (DataNodes)

Configurable replication factor

Direct client-to-DataNode data transfer

Fault-tolerant design inspired by HDFS