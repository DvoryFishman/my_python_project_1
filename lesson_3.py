my_str="!!!fff  5yn66"
def func(my_str):
    result = ''.join(c for c in my_str if c.isalpha() | c.isdigit())
    print(result)
func(my_str)

my_str2="💕 Dvory Fishman 💕 !! "
my_str2=my_str2.lower()
print(my_str2)
list_str=my_str2.split()
print(list_str)
max = 0
word=""
for i in list_str:
    if(my_str2.count(i)>max):
        max=my_str2.count(i)
        word=i
print(word)

