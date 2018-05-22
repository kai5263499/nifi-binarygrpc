nifi-binarygrpc
==

This is a hard fork of the grpc processor that [ships with Nifi 1.5.0+](https://cwiki.apache.org/confluence/display/NIFI/Leveraging+gRPC+Processors)

The reason for this fork is that the existing grpc processor is not intended to work with large payloads and doesn't support binary flowfile content in both directions. The goal of this project is to overcome both of these limitations.
