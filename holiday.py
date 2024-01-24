def flight_cost(city_flight): # User def for the selection of the city.
    ticket = 0
    if city_flight == 1:
        ticket = 975
    elif city_flight == 2:
        ticket = 1150
    elif city_flight == 3:
        ticket = 1350
    elif city_flight != 1 or 2 or 3:
        print("You have not entered 1, 2 or 3. Your flight information will not be included in this calculation.")    
    return ticket

def accommodation_cost(num_nights): # User def for the number of nights times the nightly rate.
    return num_nights * 1725

def car_rental_cost(rental_days):  # User def for the number of days the user would like to use the rental car.
    return rental_days * 480

# User input for the selection of the flight, number of nights and number of days for the rental.
city_flight = int(input("1. Johannesburg\n2. Cape Town\n3. Durban\nPlease select the city you would like to fly to: ")) 
num_nights = int(input("Please enter the number of nights you would like to stay in your preferred city: "))
rental_days = int(input("Please enter the number of days you would like to rent a car: "))


flight_cost_value = flight_cost(city_flight)
accommodation_cost_value = accommodation_cost(num_nights)
car_rental_cost_value = car_rental_cost(rental_days)

# Output of all the costs
print(f"The cost of the chosen flight will be R{flight_cost_value}")
print(f"The cost of accommodation will be R{accommodation_cost_value}")
print(f"The cost of car rental will be R{car_rental_cost_value}")

total_cost = flight_cost_value + accommodation_cost_value + car_rental_cost_value
print(f"The total cost of your trip will be R{total_cost}")
