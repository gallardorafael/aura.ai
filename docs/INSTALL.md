# Installation

## Prerequisites

### Ubuntu:

Instructions from [here](http://portaudio.com/docs/v19-doxydocs/compile_linux.html):
1. Install the ALSA sound API:
    
    sudo apt install libasound-dev

2. Download the PortAudio repository: 

   mkdir resources && cd resources && wget http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz

3. Untar the file and delete the compressed file: 

    tar zxvf pa_stable_v190700_20210406.tgz && rm pa_stable_v190700_20210406.tgz && cd portaudio

4. Configure and build PortAudio: 

    ./configure && make

5. Install the compiled files:

    sudo make install && ldconfig

## Installing aura.ai
Once you have met all the requirements, you can install aura.ai by simply running:

    pip install .