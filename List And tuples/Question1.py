# WAP to ask the user to enter 3 movies names and then store it in a list
# and then print the list
a = ("Enter 3 Movie Names: ")
b = input(a)
c = input(a)
d = input(a)
list = [b,c,d]
print(list)

# Another Method
movies = []
mov1 = input("Enter 1st Movie Name:")
mov2 = input("Enter 2nd Movie Name:")
mov3 = input("Enter 3rd Movie Name:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)