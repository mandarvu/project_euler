#include <stdio.h>
#include <math.h>

int primes(int n) //simple program to check prime parity of a number i.e whether a number is prime or not.
{
  if (n == 1)
    return -1;
  if (n == 2)
    return 1;
  else if (n%2 == 0)
    return 0;
  else
  {
    for (int i = 3;i<= sqrt(n);i += 2)
    {
      if (n % i == 0)
      {
        return 0;
      }
    }
  }
  return 1;
}

int main()
{
  long int cnt = 0, n = 2, summ = 0;
  while (1)
  {
    if (primes(n) == 1)
      summ += n;
    if (n == 2000000)
      break;
    n++;
  }
  printf("%ld\n",summ);
}
