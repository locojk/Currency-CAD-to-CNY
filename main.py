import requests

url = "https://www.bankofcanada.ca/valet/observations/FXCADCNY/json"
response = requests.get(url)
data = response.json()

# Extract the newest rate
newest_rate = data['observations'][-1]['FXCADCNY']['v']

# Print the newest rate
print()
print(f"The newest rate change for CAD to CNY is {newest_rate}, 1 Canada Dollar equal to {newest_rate} Chinese Yuan")
print()

# Calculate the difference in rate from the previous observation
prev_rate = data['observations'][-2]['FXCADCNY']['v']
diff = round(float(newest_rate) - float(prev_rate), 2)

# Print the difference in rate and whether it is positive or negative
if diff > 0:
    print(f"The rate has increased by {diff} from the previous observation.")
elif diff < 0:
    print(f"The rate has decreased by {abs(diff)} from the previous observation.")
else:
    print("The rate has not changed from the previous observation.")
