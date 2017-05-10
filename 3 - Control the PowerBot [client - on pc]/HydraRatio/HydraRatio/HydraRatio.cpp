// HydraRatio.cpp : Defines the entry point for the console application.
//

// hydra_test.cpp : Defines the entry point for the console application.
//


//sixense header and lib
#include <sixense.h>
#include <sixense_utils/derivatives.hpp>
#include <sixense_utils/button_states.hpp>
#include <sixense_utils/event_triggers.hpp>
#include <sixense_utils/controller_manager/controller_manager.hpp>

#include <iostream>
#include <iomanip>

#define PI 3.1415926

using namespace std;

//#include<windows.h>

//socket header
#include "SockStream.h"


// flags that the controller manager system can set to tell the graphics system to draw the instructions
// for the player
static bool controller_manager_screen_visible = true;
std::string controller_manager_text_string;

// This is the callback that gets registered with the sixenseUtils::controller_manager. It will get called each time the user completes
// one of the setup steps so that the game can update the instructions to the user. If the engine supports texture mapping, the 
// controller_manager can prove a pathname to a image file that contains the instructions in graphic form.
// The controller_manager serves the following functions:
//  1) Makes sure the appropriate number of controllers are connected to the system. The number of required controllers is designaged by the
//     game type (ie two player two controller game requires 4 controllers, one player one controller game requires one)
//  2) Makes the player designate which controllers are held in which hand.
//  3) Enables hemisphere tracking by calling the Sixense API call sixenseAutoEnableHemisphereTracking. After this is completed full 360 degree
//     tracking is possible.
void controller_manager_setup_callback(sixenseUtils::ControllerManager::setup_step step) 
{

	if (sixenseUtils::getTheControllerManager()->isMenuVisible()) 
	{

		// Turn on the flag that tells the graphics system to draw the instruction screen instead of the controller information. The game
		// should be paused at this time.
		controller_manager_screen_visible = true;

		// Ask the controller manager what the next instruction string should be.
		controller_manager_text_string = sixenseUtils::getTheControllerManager()->getStepString();

		// We could also load the supplied controllermanager textures using the filename: sixenseUtils::getTheControllerManager()->getTextureFileName();

	}
	else
	{

		// We're done with the setup, so hide the instruction screen.
		controller_manager_screen_visible = false;

	}

}


int main()
{
	
	//UDP socket
	sending_udpsocket clientSocket("192.168.2.112:3343");
    sockstream networkOut(clientSocket);
    receiving_udpsocket serverSocket("0.0.0.0:1121");
    sockstream networkIn(serverSocket);
    string inputBuffer;
	

	// Init sixense
	sixenseInit();

	// Init the controller manager. This makes sure the controllers are present, assigned to left and right hands, and that
	// the hemisphere calibration is complete.
	sixenseUtils::getTheControllerManager()->setGameType(sixenseUtils::ControllerManager::ONE_PLAYER_TWO_CONTROLLER);
	sixenseUtils::getTheControllerManager()->registerSetupCallback(controller_manager_setup_callback);

	// update the controller manager with the latest controller data here
	sixenseSetActiveBase(0);
	sixenseAllControllerData acd;

	double joy_x;
	double joy_y;
	int button = 0;
	int pred_button = 0;
	bool input_on = false;

	networkOut<<"99"<<" "<<"0"<<" "<<"0"<<endl;

	while(true)
	{

		sixenseGetAllNewestData(&acd);
		sixenseUtils::getTheControllerManager()->update(&acd);

		joy_x = (double)acd.controllers[0].joystick_y;
		joy_y = (double)acd.controllers[0].joystick_x;
		joy_x = joy_x*100;
		joy_y = -joy_y*100;
		pred_button = button;
		button = acd.controllers[0].buttons;
		
		//getline(networkIn, inputBuffer);


		//if (inputBuffer.compare("REQ") == 0)
		//{
			if (pred_button == 0 && button == 128)
			{
				if (!input_on)
					input_on = true;

				else
					input_on = false;
			}
		
			if (!input_on)
			{
				networkOut<<"99"<<" "<<"0"<<" "<<"0"<<endl;
				cout<<"stop"<<endl;
			}
			if (input_on)
			{
				networkOut<<"52"<<" "<<joy_x<<" "<<joy_y<<endl;
				cout<<joy_x<<"    "<<joy_y<<"    "<<endl;
			}

			system("cls");
			Sleep(100);
		//}
	}
	return 0;
}


