#!/bin/bash/

tar -xvzf bittwist-linux-2.0.tar.gz
cd bittwist-linux-2.0
/usr/bin/dnf install gcc
/usr/bin/dnf install libcap-devel
dnf install libpcap-devel.x86_64
make
make install

##You might see a warning which says : 
#src/bittwiste.c:165:22: warning: implicit declaration of function ‘strptime’ [-Wimplicit-function-declaration]
#                 if (!strptime(cp, "%d/%m/%Y,%T", tm))


#This is expected. Ignore it
