#include <stdio.h>

int main()
{
    char name[50];
    int age;
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);  // Reading a string with spaces
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("\nHello, %sYou are %d years old.\n", name, age);

    return 0;
}
