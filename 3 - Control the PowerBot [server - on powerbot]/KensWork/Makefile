CC		= g++
CFLAGS	= -c -Wall -I/usr/local/Aria/include/
LDFLAGS = -L/usr/local/Aria/lib/ -lAria -ldl -lpthread -lrt

all: hydra_control_server

clean:
	rm hydra_control_server *.o

hydra_control_server: MainApplication.o hydraRatioInput.o SockStream.o
	$(CC) -o $@ $^ $(LDFLAGS)

MainApplication.o: main.cpp
	$(CC) $(CFLAGS) -o $@ $^

hydraRatioInput.o: hydraRatioInput.cpp
	$(CC) $(CFLAGS) -o $@ $^

SockStream.o: SockStream.cpp
	$(CC) $(CFLAGS) -o $@ $^
