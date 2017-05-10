#ifndef HYDRARATIOINPUT_H
#define	HYDRARATIOINPUT_H

#include "Aria.h"
#include "SockStream.h"
#include <string>

class HydraRatioInput : public ArAction
{

public:
	

	HydraRatioInput(void); //Constructor
	~HydraRatioInput(void); //Destructor

	// The action
	ArActionDesired *fire(ArActionDesired currentDesired);

public:
	void addRatioInput(ArActionRatioInput* ratioAction);


protected:
	ArActionRatioInput* pRatioAction;
	
	int myState;
	double myTransRatio;
	double myRotRatio;

	//Socket Stuff
	sending_udpsocket clientSocket;
	sockstream networkOut;
	receiving_udpsocket serverSocket;
	sockstream networkIn;
};

#endif	/* HYDRARATIOINPUT_H */