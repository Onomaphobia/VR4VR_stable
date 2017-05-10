#include "hydraRatioInput.h"
#include <ctime>
// Constructor
HydraRatioInput::HydraRatioInput() :
ArAction("HydraRatioInput", "set ratios"),
clientSocket("192.168.2.196:1121"), networkOut(clientSocket),
serverSocket("0.0.0.0:3343"), networkIn(serverSocket)
{
	pRatioAction = 0;
	myTransRatio = 0;
	myRotRatio = 0;
	myState = 99;
}

// Destructor
HydraRatioInput::~HydraRatioInput(void)
{
}

// Fire action?
ArActionDesired *HydraRatioInput::fire(ArActionDesired currentDesired) 
{
	std::cout << "#### NEW ####" << std::endl;
	std::string inputBuffer;

	//std::cout << "[" << std::time(0) << "] sending REQ" << std::endl;
	// Send the Coordinate Request
	//networkOut << "REQ" << std::endl;

	//std::cout << "[" << std::time(0) << "] sent REQ" << std::endl;
	// Send the Coordinate Request
	//networkOut << "REQ" << std::endl;	

	// Reset the desired action
	//myDesiredAction.reset();

	std::cout << "[" << std::time(0) << "] getting response" << std::endl;
	// Get the coordinate results
	getline(networkIn, inputBuffer);

	sscanf(inputBuffer.c_str(), "%d %lf %lf", &myState, &myTransRatio, &myRotRatio);

	std::cout << "[" << std::time(0) << "] response received" << std::endl;
	// If the command isn't a NOM command, set the marker to now
	if (myState == 99)
	{
		pRatioAction->setRatios(0, 0, 0, 0);
		std::cout<<inputBuffer<<std::endl;
	}
	else if (myState == 52)
	{
		pRatioAction->setRatios(myTransRatio, myRotRatio, 30, 0);
		std::cout<<inputBuffer<<std::endl;
	}



	std::cout << "#### END ####" << std::endl;

	//need that????????????????
	return &currentDesired;
}

void HydraRatioInput::addRatioInput(ArActionRatioInput* ratioAction)
{
	pRatioAction = ratioAction;
}
