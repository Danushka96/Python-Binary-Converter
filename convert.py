#Developer Danushka Herath (Student Of UCSC)
#This programme is for Converting Decimal Numbers to binary
#Limitations >> Max number of bits=32

#Get the Decimal Number From the User
x=int(input("Enter The Decimal Number: "))

#Find How many Bits For the Inserted Number
for i in range(0,32):
	if x<=2**i:
		p=i+1
		break

#create a list for the number of bits
k=[0]*p

#Calculate the Decimal Number in Binary
i=0
while x!=0:
	y=x%2
	x=x//2
	k[i]=y
	i=i+1

#reverse the list
k=k[::-1]

#Genarate The Result in one line code and print it
p=str(0)
l=len(k)
for j in range(0,l):
	p=str(p)+str(k[j])

print("The Binary Number is ",p)