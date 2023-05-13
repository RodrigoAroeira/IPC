data = input().split("/")

data[0], data[1] = data[1], data[0]

print ("/".join(data))