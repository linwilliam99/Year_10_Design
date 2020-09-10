def isEven(a):
	if a % 2 ==0 :
		return True
	else :
		return False

#assertion test cases for isEven
def testIsEven():
	assert(isEven(4) == True)
	assert(isEven(3) == False)

#print test cases for isEven

# print(isEven(9))
# print(isEven(3))
# print(isEven(2))

print("Passed!")


#codingbat Warmup1 missing_char
def missing_char(str, n):
  newStr =""
  newStr =str[0:n] + str[n+1 : len(str)]
  return newStr

def testMissingChar():
 	assert(missing_char(hello,1) =="hllo")
 	assert(missing_char(ucc,0) =="cc")
 	assert(missing_char(uppercanadacollege,5) =="upperanadacollege")
print("Passed!")
  
