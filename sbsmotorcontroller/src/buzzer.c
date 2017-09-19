#include "stm32f10x.h"
#include "buzzer.h"
#include "Timer.h"

void buzzer_init(void) {
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_2MHz;
	GPIO_Init(GPIOA, &GPIO_InitStructure);

}

void buzzer(uint16_t hz, uint16_t msec) {
	uint32_t delay=TIMER_FREQUENCY_HZ/hz/2;
    uint32_t iters=msec*(TIMER_FREQUENCY_HZ/1000)/delay/2;
    while(--iters > 0) {
    	GPIO_WriteBit(GPIOA, GPIO_Pin_4, 1);
    	timer_sleep(delay);
    	GPIO_WriteBit(GPIOA, GPIO_Pin_4, 0);
    	timer_sleep(delay);
    }
}
