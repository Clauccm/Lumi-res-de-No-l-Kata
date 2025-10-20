import re

def solve_part1(instructions):
    grid = [[False] * 1000 for _ in range(1000)]
    
    for instruction in instructions:
        action = None
        if instruction.startswith('turn on'):
            action = 'on'
        elif instruction.startswith('turn off'):
            action = 'off'
        elif instruction.startswith('toggle'):
            action = 'toggle'
        
        coords = list(map(int, re.findall(r'\d+', instruction)))
        x1, y1, x2, y2 = coords
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == 'on':
                    grid[x][y] = True
                elif action == 'off':
                    grid[x][y] = False
                elif action == 'toggle':
                    grid[x][y] = not grid[x][y]
    
    return sum(sum(row) for row in grid)

def solve_part2(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    
    for instruction in instructions:
        action = None
        if instruction.startswith('turn on'):
            action = 'on'
        elif instruction.startswith('turn off'):
            action = 'off'
        elif instruction.startswith('toggle'):
            action = 'toggle'
        
        coords = list(map(int, re.findall(r'\d+', instruction)))
        x1, y1, x2, y2 = coords
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == 'on':
                    grid[x][y] += 1
                elif action == 'off':
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif action == 'toggle':
                    grid[x][y] += 2
    
    return sum(sum(row) for row in grid)

def main():
    # Instructions données
    instructions = [
        "turn on 887,9 through 959,629",
        "turn on 454,398 through 844,448",
        "turn off 539,243 through 559,965",
        "turn off 370,819 through 676,868",
        "turn off 145,40 through 370,997",
        "turn off 301,3 through 808,453",
        "turn on 351,678 through 951,908",
        "toggle 720,196 through 897,994",
        "toggle 831,394 through 904,860"
    ]
    
    # Résultats
    part1 = solve_part1(instructions)
    part2 = solve_part2(instructions)
    
    print(f"Part 1 - Lights lit: {part1}")
    print(f"Part 2 - Total brightness: {part2}")
    
    return part1, part2

if __name__ == "__main__":
    main()
