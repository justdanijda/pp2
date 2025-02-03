###classes
#1
class StringManipulator:
   

    def __init__(self):
        
        self.input_string = ""

    def getString(self):
        
        self.input_string = input("Enter a string: ")

    def printString(self):
       
        print(self.input_string.upper())


manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

#2
class Shape:

    def area(self):
        return 0

class Square(Shape):

    def __init__(self, length):
    
        self.length = length

    def area(self):
       
        return self.length ** 2







###Function1
#1
n=float(input())
print(n*28.35)

#2
n=float(input())
print((5/9)*(n-32))

#3

def solve(numheads,numlegs):
    for i in range(numheads+1):
        j=numheads-i
        if i*2+j*4==numlegs:
            return i,j
numheads=35
numlegs=94
result=solve(numheads,numlegs)
print(result)

#8
def spy_game(nums):
    
    s = [0, 0, 7]
    index = 0 
    
    for num in nums:
        if num == s[index]:
            index += 1  
            if index == len(s): 
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))

#9
n=float(input())
print(4*3.14*n**3)

#10
def unique_elements(input_list):
   
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = unique_elements(input_list)
print(result) 

#12
def histogram(numbers):
    
    for num in numbers:
        print("*" * num)


histogram([4, 9, 7])

#13
def guess_the_number():
    
    number_to_guess = random.randint(1, 20)
    

    name = input("Hello! What is your name?")
    print("Well", name, "I am thinking of a number between 1 and 20.")
    
    guesses = 0
    
    while True:
        guess = int(input("Take a guess."))
        guesses += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Good job", name ,"You guessed my number in", guesses ,"guesses!")
            break

guess_the_number()

###Function2

#1
def is_above_5_5(movie):
    
    return movie["imdb"] > 5.5


movie = {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"}
print(is_above_5_5(movie))

#2
def movies_above_5_5(movies):
    
    return [movie for movie in movies if movie["imdb"] > 5.5]


print(movies_above_5_5(movies))

#3
def movies_by_category(movies, category):
   
    return [movie for movie in movies if movie["category"] == category]

print(movies_by_category(movies, "Romance"))

#4
def average_imdb_score(movies):
    
    if not movies:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

print(average_imdb_score(movies))

#5
def average_imdb_score_by_category(movies, category):
    
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)

print(average_imdb_score_by_category(movies, "Romance"))
        
        

