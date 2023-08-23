import random
import time
import os

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


#Exercise 3
def life_or_death(map):
    heatmap = create_heatmap(map)
    new_map = list()

    for y, line in enumerate(heatmap):
        new_map.append(list())
        for x, column in enumerate(line):
            if column == 3:
                new_map[y].append(1)
            elif column < 2 or column > 3:
                new_map[y].append(0)
            else:
                new_map[y].append(map[y][x])

    return new_map


#Exercise 4
def hash_map(map):
    string = ""
    for line in map:
        for column in line:
            string += str(column)

    return string

def iterate(map):
    os.system("cls")
    previous_iterations = list()

    while True:
        iteration = hash_map(map)
        if not iteration in previous_iterations:
            previous_iterations.append(iteration)
            print_map(map, f"Iteration {len(previous_iterations) - 1}")
            map = life_or_death(map)

        else:
            print(f"Simulation ended after {len(previous_iterations) - 1} iterations")
            return
        
        time.sleep(1)


    

initial_map = [
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,0,0,0]
]

test_map = [
    [0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0]
]

def main():
    #map = create_map(6,6)
    #print_map(initial_map, "Map")
    #heatmap = create_heatmap(initial_map)
    #print_map(heatmap, "Heatmap")
    #new_map = life_or_death(initial_map)
    #print_map(new_map, "New Map")
    iterate(test_map)





if __name__ == "__main__":
    main()