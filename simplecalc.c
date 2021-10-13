#include<stdio.h>
#include<conio.h>
int main()
{
  char ch;
  float a,b,c;
  printf("Enter two numbers: \n");
  scanf("%f%f",&a,&b);
  printf("Enter an operator (+,-,*,\): \n");
  scanf("%c",&ch);
  switch(ch)
  {
      case '+':
  			c = a + b;
        printf("Sum of two numbers are: %f",c);
  			break;
  		case '-':
  			c = a - b;
        printf("Difference of two numbers are: %f",c);
  			break;  			
  		case '*':
  			c = a * b;
        printf("Product of two numbers are: %f",c);
  			break;
  		case '/':
  			c = a / b;
        printf("Ratio of two numbers are: %f",c);
  			break;
		default:
			printf("\n You have enetered an Invalid Operator ");
  }
  getch();
}
  
