def weather(l1):
    average_temp = sum(l1)/len(l1)
    highest_temp = max(l1)
    lowest_temp = min(l1)
    return f"average temprature:{average_temp}, highest temperature:{highest_temp}, lowest temperature:{lowest_temp}"

print(weather([25,28,21,24,27]))