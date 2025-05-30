weather = input("What's the weather like today? (sunny/rainy/cold): ")
if weather == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommendation = "Dont't forget your umbrella and a raincoat."
elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Invalid input."
print(f"As it is {weather} today {recommendation}")