#!/bin/bash

# Install dependencies for OpenCV
sudo apt-get update
sudo apt-get install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libjpeg-dev libpng-dev libtiff-dev libxvidcore-dev libx264-dev libatlas-base-dev gfortran libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev

# Clone and build OpenCV
git clone https://github.com/opencv/opencv.git
cd opencv
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j$(nproc)
sudo make install

# Install TensorFlow Lite
curl -O https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.5.0-cp38-none-linux_aarch64_download.sh
chmod +x tensorflow-2.5.0-cp38-none-linux_aarch64_download.sh
./tensorflow-2.5.0-cp38-none-linux_aarch64_download.sh
sudo pip3 install tensorflow-2.5.0-cp38-none-linux_aarch64.whl

sudo apt-get install python3-pip
pip install opencv-python

