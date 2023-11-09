from datetime import datetime

# Get the departure time from the user
departure_time_str = input("Enter the departure time (HH:MM): ")

# Get the arrival time from the user
arrival_time_str = input("Enter the arrival time (HH:MM): ")

# Convert the time strings to datetime objects
departure_time = datetime.strptime(departure_time_str, "%H:%M")
arrival_time = datetime.strptime(arrival_time_str, "%H:%M")

# Calculate the trip time
trip_time = arrival_time - departure_time

# Extract hours and minutes from the trip time
hours, remainder = divmod(trip_time.seconds, 3600)
minutes = remainder // 60

# Display the trip time
print(f"The trip time is: {hours} hr and {minutes} min")
