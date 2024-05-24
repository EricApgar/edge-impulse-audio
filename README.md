# edge-impulse-audio
This project is designed to run offline wakeword detection on a Raspberry Pi after using [Edge Impulse](https://edgeimpulse.com/) as a service to collect data and train a voice model. It is capable of handling multiple wakewords.

The actual use (inference) of the deployed wakeword model happens offline. Collecting audio data and training a model requires connecting the device to your Edge Impulse account (free to make, easy to use, well structured with extensive guides and help).

# Hardware Requirements
This project is designed to run on the Raspberry Pi.

## Raspberry Pi
Not all models of RPi are able to run this project.

| Hardware | Success | Details |
|-|-|-|
| Raspberry Pi 4B (1 GB) | Yes | Works well. |
| Raspberry Pi Zero 2 W | No | Issues installing system libraries (cmake). |
| Raspberry Pi Pico | ? | Supoosedly Edge Impulse can deploy to the Pico, though I haven't tested it. |

## Audio Device
A connected audio recording device is required to do wakeword detection. Any recording device compatible with a Raspberry Pi should work, though only certain audio HATs have been specifically tested. For Pi recording device options and installation, see [this wiki](https://github.com/EricApgar/raspberry-pi-how-to/wiki/Audio-Recording-Basics). 

# Installation

## Python
* Python 3.11.0
    * Other versions may work but have not been tested.
 
## Virtual Environment
Create a virtual environment with the correct version of python and install the appropriate python packages.
```
pip install -r requirements.txt
```

# Edge Impulse
Edge Impulse is a service that allows you to collect data, train a model, and deploy the model for a variety of machine learning tasks. It is free to use (enterprise use costs money) and has an extensive array of user guides and step by step walkthroughs to help you train and deploy a model.

The principle is that you connect your device to Edge Impulse, sample the necessary data (audio, visual, etc.) on the connected device and it goes straight to your account. Then, you train a model on Edge Impulse and can deploy the model back to your device. Deploying the model will download the trained model and let you use it offline and disconnected from the internet.

## Installation
Several libraries are required on the Raspberry Pi to work with Edge Impulse. The official [Edge Impulse Guide](https://docs.edgeimpulse.com/docs/edge-ai-hardware/cpu/raspberry-pi-4) has more detailed instructions, but the important bits have been extracted below.

Install edge impulse for Linux.
```
sudo apt update
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
```

The official instructions say ```curl ... setup_16.x ...``` but this was giving me warnings and errors about being an out of date version for the software. Instead I ran the recommended 20.x version that was suggested by the warning and that seemed to work. It did hang at one point in the process, but I just hard rebooted the RPi and ran the same commands over again and it worked the second time.

Install portaudio.
```
sudo apt install portaudio19-dev
```

## Connect Device to Edge Impulse
This will connect the device to your Edge Impulse account to allow you to collect data through the device. Since the connection tries to link the camera and microphone by default, it will throw an error if you try to connect without either of those devices. You just have to specify which ones you want to ignore (in this repo the camera since we need a microphone for audio detection).

```
edge-impulse-linux --disable-camera
```
You will be prompted for an email and password that you use to sign in to your Edge Impulse account.

## Record Samples and Train Model
Follow the Edge Impulse instructions for recording audio samples and training a model.

## Deploy
Deploy the model (instructions on Edge Impulse) by compiling your ML model into a Linux friendly format. Note that you want to compile for Linux if you're on the Raspberry Pi 4B, and NOT compile for the RP2040 chip which is the Raspberry Pi Pico option.

There are two ways to deploy a model:
1. Deploy directly from Edge Impulse.
   * Good for quickly checking that the model works.
0. Compile and download the model, and then run the Edge Impulse [Linux Python SDK](https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux/linux-python-sdk).
   * Good for using the model as part of a larger python project.

I recommend doing #1 to check that the model behaves as expected, and then doing #2 once you need to tie the model into a larger python project.

### 1. Deploy directly from Edge Impulse.
```
edge-impulse-linux-runner
```

### 2. Download the model to the RPi.
```
edge-impulse-linux-runner --download modelfile.eim
```

Once downloaded, the model can be run using ["classify.py"](https://github.com/edgeimpulse/linux-sdk-python/blob/master/examples/audio/classify.py) found in the Edge Impulse GitHub for example audio scripts.
```
python classify.py modelfile.eim <recording device>
```

Note that ```<recording device>``` is not the name as the *hardware device number* that is referenced to when you setup a recording device on the RPi. This appears to be an index that Edge Impulse uses when it collects all the recording devices it sees on your RPi. This argument is optional, and if you don't specify it then it will prompt you for user input with the list of all recording devices and you can just make a note of it then for use next time. 
