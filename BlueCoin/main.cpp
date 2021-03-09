#include <iostream>
#include <fstream>

#include "BlueCoinController.h"
#ifndef CCOMPORT_NO_QT
#include <QThread>
#include <QCoreApplication>
#endif



int main() {
    int com_N = 1; //dmesg in terminale e controlla la ttyACM 0 o 1 o 2 e scrivi qui
    int angle;
    int i;
    int meanangle=0;
    int result;
    int nosound=0;
    std::cout << "Hello, World!" << std::endl;
    BlueCoinController blueCoinController(com_N);
   
    blueCoinController.connectToCOMPort();
    result = blueCoinController.getAngle();
    blueCoinController.setThreshold();
    //while (1) {
      //  printf("Angle: %d\n",blueCoinController.getAngle());
        //sleep(1);
    //}
    for(i=0; i<5; i++) {
        result = blueCoinController.getAngle(); 
        //printf("##result##%d##",result);
        if(result >= 0) {
            meanangle = meanangle + result;
        }  
        else  { nosound ++; }
    }
    if(nosound > 4) { 
        angle = -100;
    }
    else if(meanangle == 0) {
        angle = 0;
    }
    else { angle = meanangle / (i-nosound); }
    /*if(TAudioStatus.GeneralStatus.AlgorithmActivation & ALGO_ACTIVATION_SL)
    {
        cout << "Source Localization, Algorithm " << (int)AudioStatusInstance.SLocStatus.Algorithm << ", Threshold: " << (int)AudioStatusInstance.SLocStatus.Threshold <<endl;
    }*/
    //printf("##meanangle##%d##",meanangle);
    //printf("##nosound##%d##",nosound);
    //angle = blueCoinController.getAngle();
    printf("##ANGLE##%d##",angle);
    //printf("dB: %d\n",blueCoinController.getdB());
    /*while (1) {
        for(i=0; i<5; i++) {
            result = blueCoinController.getAngle(); 
            printf(" %d ",result);
            if(result >= 0) {
                meanangle = meanangle + result;
            }  
            else  { nosound ++; }
        }
        
        if(nosound > 4) { 
            angle = -100;
        }
        else if(meanangle == 0) {
            angle = 0;
        }
        else { angle = meanangle / (i-nosound); }
        printf(" ANGLE = %d \n",angle);
        nosound = 0;
        meanangle = 0;
    }*/
    //return angle;
    return 0;
}

int int_getAngle() {
    int com_N = 0;
    int angle;
    std::cout << "Hello, World!" << std::endl;
    BlueCoinController blueCoinController(com_N);
    blueCoinController.connectToCOMPort();
    //printf("Angle: %d\n",blueCoinController.getAngle());
    //sleep(1);
    //printf("dB: %d\n",blueCoinController.getdB());
    //sleep(1);
    angle = blueCoinController.getAngle();
    std::cout << "Angle:" << angle << std::endl;
    return(angle);
}


extern "C" {
    int getangle() {
        int angle = 10;
        angle = int_getAngle();
        return(angle);
    }
}
