package service

import (
	"context"
	"fmt"

	pb "../generated"
)

type FlowFileServiceServer struct{}

func (s FlowFileServiceServer) Send(ctx context.Context, flowfileRequest *pb.FlowFileRequest) (*pb.FlowFileReply, error) {

	if flowfileRequest == nil {
		return nil, fmt.Errorf("empty flowfile request")
	}

	flowFileReply := &pb.FlowFileReply{
		Attributes: map[string]string{
			"myattribute": "attribute value",
		},
		Content: []byte("flowfile reply"),
	}

	return flowFileReply, nil
}
