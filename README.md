# edge-impulse-audio
Instructions for deploying an Edge Impulse Audio model on the Raspberry Pi.

```
edge-impulse-linux-runner --download modelfile.eim
```

There are some libraries needed by the system:
See the edge impulse [installation guide](https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux/linux-python-sdk) for reference.
```
sudo apt install portaudio19-dev
sudo apt install cmake
```

???
```sudo apt install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev```

```
sudo ln -s /usr/lib/arm-linux-gnueabihf/libssl.so.1.1 /usr/lib/arm-linux-gnueabihf/libssl.so.3
sudo ln -s /usr/lib/arm-linux-gnueabihf/libcrypto.so.1.1 /usr/lib/arm-linux-gnueabihf/libcrypto.so.3
```

