#!/bin/bash

openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "dump_image .tmp.4001000.bin 0x40010000 0x4000" -c shutdown
openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "dump_image .tmp.4000000.bin 0x40000000 0x8000" -c shutdown

dd if=/dev/zero of=.tmp.4000000.bin bs=1 count=1 seek=$(( 0x40010000 - 0x40000000 - 1 ))
dd if=/dev/zero of=.tmp.4001000.bin bs=1 count=1 seek=$(( 0x40020000 - 0x40010000 - 1 ))
cat .tmp.4000000.bin .tmp.4001000.bin > "$1"
rm .tmp.*.bin




