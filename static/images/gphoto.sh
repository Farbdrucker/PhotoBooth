#!/bin/bash

while true; do
    gphoto2 --get-al-files --skip-existing --keep
    sleep 2
done