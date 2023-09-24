# Create a console app that interacts with an API -
    # it gets some data and does a meaningful transformation /
    # use boolean values and if else statements to branch logic to your program //
    # use a data structure: list/ dictionary/ tuple or set to store values /
    # use a for or while loop to reduce repetition /
    # use string slicing /
    # use at least TWO inbuilt functions //
        # print() / help() type() str() float() int() / ord() chr() len() /
    # use any free API to get some information as json /
    # import an additional module and use it /

# Access the API
import requests
import time
import random
endpoint = "https://api.thedogapi.com/v1/breeds";
api_key = "live_zMs6ctnpN7sHIuAPBJnKy18S6FSochsksGfW7yvtMpgGKdoTeUTqDfvOVd8Tnghs"

response = requests.get(endpoint)
data = response.json()



# Get the list of dogs available within the API
def get_dog_breeds():
    url = "https://api.thedogapi.com/v1/breeds"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch dog breeds.")
        return []

# Saves the breed name and temperament to a txt file
filename1 = 'Random_dogs.txt'

def save_breed_data(breeds, filename1):
    with open(filename1, "a+") as file:
        for breed in breeds:
            file.write(f"Name: {breed['name']}\n")
            file.write(f"Temperament: {breed['temperament']}\n")
            file.write("-" * 40 + "\n")

# Saves the people and favourite dog breed to a txt file
filename2 = "Fave_dogs.txt"

def save_people_data(people, filename2):
    with open(filename2, "w") as file:
        for person, breed in people.items():
            file.write(f"Name: {person}\n")
            file.write(f"Favourite Dog Breed: {breed}\n")
            file.write("-" * 40 + "\n")



## ! FOR THE OPTION SELECTION ! ##

# Random Dog breed time!
def random_breed():
    dog_breeds = get_dog_breeds()

    chosen_breed = random.choice(dog_breeds)
    print(f"\nYou got a random breed: {chosen_breed['name']}\n")

    chosen_breeds = [chosen_breed]

    save_breed_data(chosen_breeds, filename1)
    print(f"Breed information saved to ", filename1)



# Favourite Dog Breed
favourite_dog_breeds = {}

def fave_dog():
    person_name = input("Enter name: ")
    favourite_breed = input("What is their favourite dog breed? ")

    favourite_dog_breeds[person_name] = favourite_breed
    print(f"{person_name}'s favourite dog breed, {favourite_breed}, has been recorded.")

    save_people_data(favourite_dog_breeds, "Fave_dogs.txt")


# View favourite dog breeds
def view_favourite_dog_breeds():
    print("Favorite Dog Breeds:")

    for person, breed in favourite_dog_breeds.items():
        short_name = person[:3]
        print(f"{short_name}: {breed}")



# Find dogs saved in txt file
def find_dog_breed_by_name(filename2):
    search_name = input("Enter the name to search for (in the Fave_dog.txt): ").lower()

    try:
        with open(filename2, "r") as file:
            lines = file.readlines()
            found = False

            for i in range(0, len(lines), 3):  # Process lines in sets of 3
                name_line = lines[i].strip()
                breed_line = lines[i + 1].strip()

                if name_line.startswith("Name:") and breed_line.startswith("Favourite Dog Breed:"):
                    name = name_line.split(":")[1].strip().lower()
                    breed = breed_line.split(":")[1].strip()

                    if name == search_name:
                        print(f"Name: {name}".title())
                        print(f"Favourite Dog Breed: {breed}")
                        print("-" * 40)
                        found = True

            if not found:
                print(f"No record found for '{search_name}'.")

    except FileNotFoundError:
        print(f"The file '{filename2}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def option_4():
    print("Option 4: Find Dog Breeds by Name")
    find_dog_breed_by_name("Fave_dogs.txt")



# Dog Person Quiz
def dog_person_quiz():
    dog_intro = input('Do you like dogs? y/n ')
    is_good = dog_intro == 'y'

    dog_intro2 = input('Do you have a dog? y/n ')
    has_dog = dog_intro2 == 'y'

    if is_good and has_dog:
        print('Definitely a dog person')

    if is_good and not has_dog:
        print('You are a dog person')

    if not is_good and not has_dog:
        print('Are you a cat person?')



# Palindrome Fun
def palindrome_fun():
    tacocat_word = input("What is a dog's favourite toy? ")

    def isPalindrome(string):
        leftIdx = 0
        rightIdx = len(string) - 1
        while leftIdx < rightIdx:
            if string[leftIdx] != string[rightIdx]:
                return False
            leftIdx += 1
            rightIdx -= 1
        return True

    print("Is {} a palindrome?: ". format(tacocat_word), isPalindrome((tacocat_word)),"(Regardless if it is a palindrome, they just love to play!")



# Option Selection
print("Welcome! Let's explore some dog breeds!")
print("Copyright 2023, All Rights Reserved by Hayley So")

def print_menu():
    print("--------------------------------------------")
    print("1. Get a random dog breed")
    print("2. What is your favourite dog breed?")
    print("3. View favourite dog breeds")
    print("4. Find dog breeds from name")
    print("5. Are you a dog person?")
    print("6. Palindrome Fun")
    print("--------------------------------------------")

while True:
    print_menu()
    option = int(input("Please select an option "))

    if option == 1:
        random_breed()
        time.sleep(1.25)

    elif option == 2:
        fave_dog()
        time.sleep(1.25)

    elif option == 3:
        view_favourite_dog_breeds()
        time.sleep(1.25)

    elif option == 4:
        option_4()
        time.sleep(1.25)

    elif option == 5:
        dog_person_quiz()
        time.sleep(1.25)

    elif option == 6:
        palindrome_fun()
        time.sleep(1.25)

    else:
        print("Invalid Option. Please select a number between 1 - 6")