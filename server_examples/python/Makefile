
generate_proto:
	python -m grpc_tools.protoc -I../../src/main/resources/proto --python_out=. --grpc_python_out=. ../../src/main/resources/proto/flowfile_service.proto
	# protoc ../../src/main/resources/proto/flowfile_service.proto --proto_path=../../src/main/resources/proto --python_out=plugins=grpc:generated