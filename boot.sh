#!/bin/bash
ADB=/usr/bin/adb
"$ADB" push $1 /sdcard/bootanimation.zip
"$ADB" shell "su -c 'mount -o rw,remount /system'"
"$ADB" shell "su -c 'mv /sdcard/bootanimation.zip /system/media/'"
"$ADB" shell "su -c 'chmod 644 /system/media/bootanimation.zip'"
"$ADB" reboot
