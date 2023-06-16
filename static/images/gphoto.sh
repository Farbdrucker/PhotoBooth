#!/bin/bash

while true; do
    gphoto2 --get-all-files --skip-existing --keep
    sleep 2
done