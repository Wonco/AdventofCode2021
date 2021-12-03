# Day2 part1
url = "https://raw.githubusercontent.com/Wonco/AdventofCode2021/main/2021-12-02/Part1_Dataset.txt"
req = requests.get(url)

# Turn dataset into list of lists.
data = [
    line.split()
    for line in req.content.decode('utf-8').split('\n')
]

# convert list emelement to int.
int_data = [[int(element) if element.isdigit() else element for element in row] for row in data]
int_data.pop(1000) # remove last empty list.

forward_count = 0
down_count = 0
up_count = 0

for sub in int_data:
    if sub[0] == "forward":
        forward_count += sub[1]
    if sub[0] == "down":
        down_count += sub[1]
    if sub[0] == "up":
        up_count += sub[1]

total_depth = down_count - up_count
print(forward_count * total_depth)
