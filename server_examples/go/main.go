package main

import (
	"fmt"

	pb "./generated"
	"./service"

	"log"
	"net"

	"github.com/Sirupsen/logrus"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

type Config struct {
	GrpcPort    int    `config:"default=9000;usage="`
	UseTLS      bool   `config:"default=false;usage="`
	SSLCertFile string `config:"default=ssl.crt;usage=SSL public key file"`
	SSLKeyFile  string `config:"default=ssl.key;usage=SSL private key file"`
}

type Server struct {
	conf          *Config
	serviceServer pb.FlowFileServiceServer
	lis           *net.Listener
	grpcServer    *grpc.Server
}

func (s *Server) Start() error {
	listenAddress := fmt.Sprintf("localhost:%d", s.conf.GrpcPort)

	lis, err := net.Listen("tcp", listenAddress)

	if err != nil {
		logrus.Errorf("unable to create network listener err=%#v", err)
		return err
	}

	s.lis = &lis

	logrus.Infof("listening on %s", listenAddress)

	if !s.conf.UseTLS {
		if err != nil {
			log.Fatalf("failed to listen: %v", err)
			return err
		}
		s.grpcServer = grpc.NewServer()
	} else {
		certFile := s.conf.SSLCertFile
		keyFile := s.conf.SSLKeyFile
		creds, err := credentials.NewServerTLSFromFile(certFile, keyFile)
		if err != nil {
			log.Fatalf("failed to listen: %v", err)
			return err
		}
		s.grpcServer = grpc.NewServer(grpc.Creds(creds))
	}

	pb.RegisterFlowFileServiceServer(s.grpcServer, s.serviceServer)

	logrus.Infof("now serving")

	return s.grpcServer.Serve(lis)
}

func main() {
	config := &Config{
		GrpcPort: 9000,
	}
	serviceServer := service.FlowFileServiceServer{}
	service := &Server{
		conf:          config,
		serviceServer: serviceServer,
	}
	service.Start()
}
