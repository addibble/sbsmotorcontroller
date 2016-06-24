#!/bin/bash

openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c targets \
    -c "dump_image dump-4001000.bin 0x40010000 0x4000" \
    -c "dump_image dump-4000000.bin 0x40000000 0x8000" \
    -c 'shutdown'

