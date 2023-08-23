import random

def print_map(map, name):
    print(f"{name}---------------")
    for line in map:
        print(line)
    print("\n")

def create_map(x, y):
    map = list()

    for line_count in range(y):
        map.append(list())
        for column_count in range(x):
            map[line_count].append(random.randint(0,1))

    return map


#Exercise 1
def create_heatmap(map):
    operations = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    heatmap = list()

    for y, line in enumerate(map):
        heatmap.append(list())
        for x, column in enumerate(line):
            neighbors = 0
            for operation in operations:
                if y+operation[0] < 0 or x+operation[1] < 0 or y+operation[0] >= len(map) or x+operation[1] >= len(line):
                    continue
                
                neighbors += map[y+operation[0]][x+operation[1]]
            heatmap[y].append(neighbors)

    return heatmap

    

initial_map = [
    [0,1,0],
    [0,1,0],
    [0,1,0]
]

test_map = [
    
]

def main():
    map = create_map(6,6)
    print_map(map, "Map")
    heatmap = create_heatmap(map)
    print_map(heatmap, "Heatmap")




if __name__ == "__main__":
    main()