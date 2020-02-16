#!/bin/bash
#This script installs teh required python packages and performs general python setup
dnf install freetype-devel.x86_64
dnf install libpng-devel
dnf install python-devel
dnf install python-pip
pip install scapy
