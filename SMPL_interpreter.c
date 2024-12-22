#include <stdio.h>
#include <string.h>

typedef struct
{
    char command[256];
    char brackets[256];
} TokenResult;

TokenResult tokenize(const char *line)
{
    TokenResult result = {"", ""};

    int commandIndex = 0;
    int bracketIndex = -1;
    int bracketFound = 0;

    for (int i = 0; i < strlen(line); i++)
    {
        if (line[i] == '(')
        {
            bracketFound = 1;
        }
        else if (line[i] == ')')
        {
            bracketFound = 0;
        }

        if (bracketFound == 1)
        {
            result.brackets[bracketIndex++] = line[i];
        }
        else
        {
            result.command[commandIndex++] = line[i];
        }
    }

    result.command[commandIndex - 2] = '\0';

    return result;
}

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

    while (fgets(line, sizeof(line), fptr) != NULL)
    {
        if (line[0] == ' ' || line[0] == '\n' || (line[0] == 'B' && line[1] == 'T' && line[2] == 'W'))
        {
            continue;
        }
        else
        {

            printf("%s", line);

            int lenLine = strlen(line);

            TokenResult result = tokenize(line);

            if (strcmp(result.command, "shout") == 0)
            {
                printf("%s\n", result.brackets);
            }
        }
    }
    fclose(fptr);
    return 0;
}