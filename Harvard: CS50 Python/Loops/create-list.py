## Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print (f"{word}\n")

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for username in range(len(usernames)):
    usernames[username] = usernames[username].lower().replace(" ", "_")
   
print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1


print(count)