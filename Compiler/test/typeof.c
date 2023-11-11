#include "test.h"

int main(){
    ASSERT(3,({typedef(int) x=3;x;}));
    ASSERT(3,({typedef(1) x=3;x;}));
    ASSERT(4,({int x;typedef(x) y; sizeof(y);}));
    ASSERT(8,({int x;typedef(&x)y;sizeof(y);}));
    ASSERT(4,({typedef("foo")x;sizeof(x);}));
    ASSERT(12,sizeof(typedef(struct{int a,b,c;})));

    printf("All testcases passed\n");
    return 0;
}