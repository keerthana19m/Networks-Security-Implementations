#include<stdio.h>
long long int diffiecompute(int a,int b,int mod)
{
 long long int t;
 if(b==1)
  return a;
 t=diffiecompute(a,b/2,mod);
 if(b%2==0)
  return (t*t)%mod;
 else
  return (((t*t)%mod)*a)%mod;
}
long long int calculateKey(int a,int x,int n)
{
 return diffiecompute(a,x,n);
}
int main()
{
 int p,g,x,randoma,y,randomb;
 // both parties choose a common p and g value 
 printf("Please enter the value of p and g : ");
 scanf("%d%d",&p,&g);
 
 // Alice chooses secret random num
 printf("Enter the value of random number chosen by Alice: ");
 scanf("%d",&x);
 randoma=diffiecompute(g,x,p);
 
 // Bob chooses secret random num
 printf("Enter the value of random number chosen by Bob: ");
 scanf("%d",&y);
 randomb=diffiecompute(g,y,p);
 
 printf("Alice's secret key is : %lld\n",diffiecompute(randomb,x,p));
 printf("Bob's secret key is : %lld\n",diffiecompute(randoma,y,p));
 return 0;
}
