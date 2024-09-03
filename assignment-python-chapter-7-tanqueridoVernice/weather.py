# Follow the instructions for coding a weather app
# Vernice Tanquerido
# I used https://www.w3schools.com/python/ref_func_max.asp for reference for the max and min functions.

highs = [62, 64, 79, 52, 46, 50, 58, 66, 71, 75, 78, 78, 76, 80, 77]
lows = [42, 48, 47, 26, 28, 28, 32, 37, 43, 46, 48, 47, 48, 49, 50]
humidities = [0.48, 0.53, 0.46, 0.44, 0.4, 0.6, 0.58,
              0.5, 0.48, 0.43, 0.41, 0.39, 0.39, 0.3, 0.4]
total_high = 0
total_low = 0
total_humidity = 0
max_high = max(highs)
min_low = min(lows)
for temp in highs:
    total_high += temp
    ave_high = total_high/len(highs)

for temp in lows:
    total_low += temp
    ave_low = total_low/len(lows)

for humidity in humidities:
    total_humidity += humidity
    ave_humidity = total_humidity/len(humidities)

print(
    f"Weather forecast for the next 15 days: The average low will be {ave_low:.0f} and average high will be {ave_high:.0f}. The average humidity will be {ave_humidity:.2f}. The highest temperature will be {max_high:.0f}. The lowest temperature will be {min_low:.0f}.")
