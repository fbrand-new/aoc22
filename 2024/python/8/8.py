from itertools import combinations

def frequencies(antennas_str):
    '''
        Return the frequencies given the full string
    '''
    
    return set(antennas_str)

def create_freq_maps(antennas,freqs):
    
    d = {}
    for freq in freqs:
        tmp = [[i for i,n in enumerate(line) if n==freq] for line in antennas]
        d[freq] = [(i,value) for i,lst in enumerate(tmp) for value in lst]
    return d

def flatten_list(l):
    return [v for sub in l for v in sub]

def is_inside_grid(pos,limx,limy):
    
    if pos[1]<limx and pos[1]>=0 and pos[0]<limy and pos[0]>=0:
        return True
    
    return False 

def create_antinodes(pos1,pos2,limx,limy):
    
    delta_x = pos1[1]-pos2[1]
    delta_y = pos1[0]-pos2[0] #Y axis is reversed
    
    antinode1 = (pos1[0]+delta_y,pos1[1]+delta_x)
    antinode2 = (pos2[0]-delta_y,pos2[1]-delta_x)
    
    antinodes=[]
    if is_inside_grid(antinode1,limx,limy):
        antinodes.append(antinode1)
    if is_inside_grid(antinode2,limx,limy):
        antinodes.append(antinode2)
    
    return antinodes

def create_antinodes_2(pos1,pos2,limx,limy):
    delta_x = pos1[1]-pos2[1]
    delta_y = pos1[0]-pos2[0] #Y axis is reversed
    
    i = 0
    antinode = (pos1[0]+i*delta_y,pos1[1]+i*delta_x)
    antinodes = []
    while is_inside_grid(antinode,limx,limy):
        antinodes.append(antinode)
        antinode = (pos1[0]+i*delta_y,pos1[1]+i*delta_x)
        i += 1
        
    i = -1
    antinode = (pos1[0]+i*delta_y,pos1[1]+i*delta_x)
    while is_inside_grid(antinode,limx,limy):
        antinodes.append(antinode)
        antinode = (pos1[0]+i*delta_y,pos1[1]+i*delta_x)
        i -= 1
        
    return antinodes
        
if __name__ == '__main__':

    with open('input.txt','r') as f:
        antennas_str = f.read()
        antennas = [[i for i in line] for line in antennas_str.splitlines()]
    
    limx = len(antennas[0])
    limy = len(antennas)
    freqs = frequencies(antennas_str.replace('\n','').replace('.',''))
    map = create_freq_maps(antennas=antennas,freqs=freqs)
    
    sum = 0
    antinodes = []
    for freq,freq_map in map.items():
        tmp = [create_antinodes_2(pos1,pos2,limx,limy) for pos1, pos2 in combinations(freq_map,2)]
        antinodes.extend(tmp)
        # print(f"Antinodes for freq {freq}: {tmp}")
        # sum += len(antinodes)
        
    
    antinodes = flatten_list(antinodes)
    print(f"The total number of antinodes is {len(set(antinodes))}")