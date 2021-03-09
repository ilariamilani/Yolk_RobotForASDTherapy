//
// Created by Lorenzo and Ilaria on 10/31/2020.
//

#ifndef BLUECOIN_BLUECOINCONTROLLER_H
#define BLUECOIN_BLUECOINCONTROLLER_H

#include "AudioSerialLib/AudioModuleSerialLib.h"
#include "Exceptions.cpp"
#include <iostream>

#define COM_BAUDRATE  921600
#define Audio_Module_ADDR    50


class BlueCoinController {
private:
    int com_N;
    TAudioStatus AudioStatusInstance;
    AudioModuleSerialLib *AudioSL;


public:
    BlueCoinController(int com_N);

    void connectToCOMPort();

    int getAngle();
    int setThreshold();
    int getdB();
    int setOutput();

};


#endif //BLUECOIN_BLUECOINCONTROLLER_H
