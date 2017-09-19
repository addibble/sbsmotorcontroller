#include "util.h"

void write_mask(GPIO_TypeDef* gp, uint16_t mask, uint8_t val) {
	  for(int i=0; i<16; i++) {
		  if(mask & 1) {
			  GPIO_WriteBit(gp, 1 << i, val);
		  }
		  mask = mask >> 1;
	  }
}
