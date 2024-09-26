user_choice = input("What's the weather like today? (sunny/rainy/cold): ")

if user_choice == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_choice == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_choice == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")