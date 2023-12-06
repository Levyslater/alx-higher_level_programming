#include <stdio.h>
#include <string.h>

int main()
{
    const char *name = "radarradarradar";
    int start = 0, end, count = 0;
    
    end = strlen(name) - 1;
    
    while (start < end)
    {
        if (name[start] != name[end])
        {
            count++;
            break;
        }
        start += 1;
        end -= 1;

    }
    if (!count)
    printf("Word: %s is a Palindrome\n", name);
    else
    printf("Word: %s is not a palindrome\n", name);
    return (0);
}