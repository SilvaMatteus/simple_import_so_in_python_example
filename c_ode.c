#include "c_ode.h"
#include "stdio.h"

void c_print() {
    printf("This is my printf written in C!\n");
}

int c_add(int a, int b) {
    return a + b;
}

char * c_bytes(int8_t *p, int len) {
    for (int8_t i = 0; i < len; i++) {
        printf("%c\n", p[i]);
    }
    return "Hello, c.";
}
