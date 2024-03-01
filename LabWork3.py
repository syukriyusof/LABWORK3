"""
 Program Purpose: To ask user to input data for booking room at Hotel Ceria and calculate the total cost.
 Programmer: MUHAMMAD SYUKRI BIN MHD YUSOF (AM2307013981)
 Date: 1 March 2024
"""

def display_room_types_and_rates(room_types, nightly_rates):
    print("Room Types:")
    for i in range(len(room_types)):
        print(f"{i + 1}. {room_types[i]} - RM{nightly_rates[i]} per night")

def calculate_total_cost(room_type_index, num_rooms, duration_of_stay, nightly_rate, additional_services):
    total_cost = num_rooms * duration_of_stay * nightly_rate
    for service in additional_services:
        total_cost += service_costs.get(service, 0)
    return total_cost

def display_confirmation(room_type, num_rooms, check_in, check_out, total_cost, additional_services):
    print("\nReservation Details:")
    print(f"Room Type: {room_type}")
    print(f"Number of Rooms: {num_rooms}")
    print(f"Check-in Date: {check_in}")
    print(f"Check-out Date: {check_out}")
    print("Additional Services:")
    for service in additional_services:
        print(f"- {service}")
    print(f"Total Cost: RM{total_cost}")

room_types = ["Single", "Double", "Suite"]
nightly_rates = [100, 150, 250]
service_costs = {"Breakfast": 20, "WiFi": 10, "Parking": 15}

print("Welcome to Hotel Ceria Reservation System!\n")

display_room_types_and_rates(room_types, nightly_rates)

# Input room type
room_type_index = int(input("\nEnter the number of your desired room type as per listed above: ")) - 1
num_rooms = int(input("Enter the number of rooms: "))

# Input check-in and check-out dates
check_in = input("Enter check-in date (YYYY-MM-DD): ")
check_out = input("Enter check-out date (YYYY-MM-DD): ")

# Select additional services
additional_services = []
while True:
    service = input("Would you like to add Breakfast, WiFi, or Parking?\n(Enter service name and after that enter 'Done' to finish. Please proceed to enter 'Done' if you don't want any additional service): ").capitalize()
    if service == "Done":
        break
    elif service in service_costs:
        additional_services.append(service)
    else:
        print("Invalid service. Please choose from Breakfast, WiFi, or Parking.")

nightly_rate = nightly_rates[room_type_index]
duration_of_stay = (int(check_out[8:]) - int(check_in[8:]))

total_cost = calculate_total_cost(room_type_index, num_rooms, duration_of_stay, nightly_rate, additional_services)

display_confirmation(room_types[room_type_index], num_rooms, check_in, check_out, total_cost, additional_services)

# Confirm reservation
confirm = input("Confirm your reservation? (yes/no): ").lower()
if confirm == "yes":
    print("Reservation confirmed. Thank you!")
else:
    print("Reservation canceled.")