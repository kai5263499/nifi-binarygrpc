
generate_proto:
	# pip install grpcio-tools
	python -m grpc_tools.protoc -I../../src/main/resources/proto --python_out=. --grpc_python_out=. ../../src/main/resources/proto/flowfile_service.proto
	# protoc -I ../../protos --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ../../protos/route_guide.proto
