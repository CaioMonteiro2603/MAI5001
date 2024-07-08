def time_to_seconds(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

entrada = input().split(":")
hours = int(entrada[0])
minutes = int(entrada[1])
seconds = int(entrada[2])

total_seconds = time_to_seconds(hours, minutes, seconds)
print(total_seconds)
