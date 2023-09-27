lower = 0
upper = 15
print("The lower and upper range are :",lower, upper)
print("The prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
      for i in range(2, num):
         if (num % i) == 0:
            break
      else:
         print(num)


#another way
def is_prime(number):
   if number<2:
      return False
   test=2
   while test<number:
      if number%test ==0:
         return False
      test+=1
   return True

def find_prime(min,max):
   number=min
   while number<max:
      test =2
      while test<number:
         if number%test==0:
            break
         test+=1
      else:
         print(number,end='\t')
      number+=1
print()

find_prime(0,50)