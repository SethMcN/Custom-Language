#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct
{
    char command[256];
    char brackets[256];
} TokenResult;


typedef struct
{
    char bracketSplit[256];

} BracketResult;

BracketResult SplitBrackets(char *brackets){
    BracketResult result = {""}; // Reset result structure

    int speechMarkCount = 0;

    int length = strlen(brackets);
    for (int i = 0; i <= length; i++)
    {
        if (brackets[i] == '\"' || brackets[i] == '\'')
        {
            speechMarkCount ++;
        }
    
        bool isOutsideQuotes = (speechMarkCount % 2 == 0);

        if (!isOutsideQuotes)
        {
            result.bracketSplit[i] = brackets[i];
        }
    }

    return result;
    
}

TokenResult tokenize(char *line)
{
    TokenResult result = {"", ""}; // Reset result structure

    int commandIndex = 0;
    int bracketIndex = 0;
    int bracketFound = 0;
    int commandFound = 0;
    int bracketBalance = 0;

    for (int i = 0; i <= strlen(line); i++)
    {
        if (commandFound == 1)
        {

            if (bracketFound == 1 && bracketBalance > 0){
                result.brackets[bracketIndex++] = line[i];
            }

            if (line[i] == '(')
            {
                bracketBalance++;
                bracketFound = 1;
            }

            else if (line[i] == ')')
            {
                bracketBalance--;
            }
            


        }

        else
        {
            result.command[commandIndex++] = line[i];

            if (strcmp(result.command, "shout") == 0)
            {
                commandFound = 1;
            }
        }
    }
    result.command[commandIndex] = '\0';
    result.brackets[bracketIndex-1] = '\0';

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
            TokenResult result = tokenize(line); // Reset for each line

            if (strcmp(result.command, "shout") == 0)
            {
                BracketResult bracketResult = SplitBrackets(result.brackets);
                printf("%s\n", bracketResult.bracketSplit);
            }
        }
    }
    fclose(fptr);
    return 0;
}