#ifndef TRACE_H
#define TRACE_H
#include <execinfo.h>
#include <stdlib.h>
#include "HomePch.h"
void
print_trace()
{
    void *array[100];
    size_t size;
    char ** strings;
    size_t i;

    size = backtrace(array, 100);
    strings = backtrace_symbols(array, size);

    for(int i=0; i<size; i++)
    {
        HomeLog("TRACE:%s \n", strings[i]);
    }
    free(strings);
}

#endif
