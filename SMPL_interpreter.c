#include <stdio.h>
#include <string.h>
int main()
{
    FILE *fptr;
    fptr = fopen("firstCode.smpl", "r");
    if (fptr == NULL)
    {
        printf("Error! File not found\n");
        return 0;
    }

    char line[256];
    printf("The content of the file SMPL_interpreter.txt is:\n");
    printf("------------------------------------------------\n");

    while (fgets(line, sizeof(line), fptr))
    {
        if (line[0] == ' ' || line[0] == '\n'){
            continue;
        }

        else{
            printf("%s", line);
            char *result = strstr(line, "say_my_name");

        }
    }
    return 0;
}