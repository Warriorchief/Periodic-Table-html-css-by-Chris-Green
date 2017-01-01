#Project Euler #1

#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

div_by_3_or_5=[];

i=1
while i<1000:
    if (i%3==0 or i%5==0):
        div_by_3_or_5.append(i);
    i+=1;

total=0
j=0
while j<len(div_by_3_or_5):
    total+=div_by_3_or_5[j];
    j+=1;
print(total);

#CORRECT ANSWER: 223168


