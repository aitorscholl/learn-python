num_people =  25
portion_of_food = 0.07

amount_of_food_per_person = portion_of_food / num_people 
print(amount_of_food_per_person)

tons_of_food = float(input("How much tons of food did you take? "))

if round(tons_of_food, 5) == round(amount_of_food_per_person, 5):
    print("Good Job you took the right amount of food.")
else: 
    print("You took the wrong amount of food.")