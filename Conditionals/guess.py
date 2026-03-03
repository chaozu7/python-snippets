# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 9  # provide answer
guess = int(input("About what number am I thinking? "))  # provide guess

if answer > guess:  # provide conditional
    result = "Oops!  Your guess was too low."
elif answer < guess:  # provide conditional
    result = "Oops!  Your guess was too high."
elif answer == guess:  # provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)


ver = 4
VER = 7

print(VER)


#     0, 1,  2, 3, 4, 5, 6, 7
li = [1, 10, 2, 9, 0, 1, 10, 8]
x = 0
# in range 8
for i in range(len(li)):
    # li[0] > = li[0]
    # x = 0
    if li[i] >= li[x]:
        x = i
        print("x to ", x)
        print("Wartość i to ", li[i])
        print("Wartość x to ", li[x])
print(x)

s = "artificialintelligence"
print(s[0:10:2])


class Version(object):
    def __init__(self, name):
        self.subversion = 0
        self.name = name

    def update(self):
        self.subversion += 1
        return Version(str(self.name) + "." + str(self.subversion))


v = Version("1")
w = v.update()
y = w.update()
x = w.update()
print(x.name)
