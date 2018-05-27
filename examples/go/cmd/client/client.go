package main

import (
	"github.com/davecgh/go-spew/spew"
	"golang.org/x/net/context"
	"google.golang.org/grpc"

	pb "../../generated"
)

func main() {
	conn, _ := grpc.Dial("localhost:9001", grpc.WithInsecure())
	defer conn.Close()
	client := pb.NewFlowFileServiceClient(conn)
	ffRequest := &pb.FlowFileRequest{
		Id: 2,
		Attributes: map[string]string{
			"myattribute": "my value",
		},
	}

	ffResponse, _ := client.Send(context.Background(), ffRequest)

	spew.Dump(ffResponse)
}
