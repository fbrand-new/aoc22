test_val = "12345"
expected_val = "0..111....22222"
expected_move = "022111222......"

expected_val2 = "00...111...2...333.44.5555.6666.777.888899"
expected_move2 = "0099811188827773336446555566.............."
expected_checksum2 = 1928

test_val3 = "1313165"
expected_val3 = "021......33333......"

def dense_to_sparse(layout):
    sparse = []
    for i,n in enumerate(layout):
        idx = i//2
        if i%2 == 0:
            add = [idx for _ in range(int(n))]
        else:
            add = ['.' for _ in range(int(n))]
    
        sparse.extend(add)
        
    return sparse

def move_blocks(disk: list):
    free_space_idx = disk.index('.')
    curr_block_idx = len(disk)-1

    # disk_l = [i for i in disk]

    while(free_space_idx < curr_block_idx):
        if disk[curr_block_idx] != '.':
            disk[curr_block_idx], disk[free_space_idx] = '.', disk[curr_block_idx]
            curr_block_idx -= 1
            free_space_idx = disk.index('.')
        else:
            curr_block_idx -= 1
            
    return disk

def find_sublist_index(lst, sublst):
    n = len(sublst)
    for i in range(len(lst) - n + 1):
        if lst[i:i+n] == sublst:
            return i
    return -1

def move_blocks2(disk: list):
    
    curr_idx = len(disk)-1
    
    while(curr_idx > 0):
        val = disk[curr_idx]
        
        # If we are on a free position go left
        if val == '.':
            curr_idx -= 1
            continue
        
        val_first_idx = disk.index(val)
        val_occurences = curr_idx - val_first_idx + 1
        
        # disk_str = "".join([str(i) for i in disk])
        free_list = ["." for _ in range(val_occurences)]
        free_idx = find_sublist_index(disk,free_list)
        # free_idx = disk_str.find("."*val_occurences)
        
        # If we did not found an available space at all, 
        # Or if the available space is on the right, ignore the block
        if free_idx == -1 or free_idx > curr_idx:
            curr_idx = val_first_idx-1
            continue
        
        disk[free_idx:free_idx+val_occurences] = [val for _ in range(val_occurences)]
        disk[val_first_idx:val_first_idx+val_occurences] = ['.' for _ in range(val_occurences)]
        curr_idx = val_first_idx-1 
    
    return disk

def compute_checksum(disk: list):
    
    components = [i*int(n) for i,n in enumerate(disk) if n!='.']
    return sum(components)


if __name__ == "__main__":
    
    with open('test.txt','r') as f:
            test2 = f.read()
    
    test_sparse = dense_to_sparse(test_val)
    # assert test_sparse == expected_val
    
    test_sparse2 = dense_to_sparse(test2) 
    # assert test_sparse2 == expected_val2
    
    test_moved = move_blocks(test_sparse)
    # assert test_moved == expected_move
    
    test_moved2 = move_blocks(test_sparse2)
    # assert test_moved2 == expected_move2

    checksum2 = compute_checksum(test_moved2)
    # assert checksum2 == expected_checksum2
    
    with open('input.txt','r') as f:
        input = f.read()
        
    sparse_input = dense_to_sparse(input)
    # moved_input = move_blocks(sparse_input)
    moved_input = move_blocks2(sparse_input)
    with open('write.txt','w') as f:
        f.write("".join([str(i) for i in moved_input]))
        
    print(f"The checksum is {compute_checksum(moved_input)}")
    
    # sparse_input = dense_to_sparse(test_val3)
    # # moved_input = move_blocks(sparse_input)
    # moved_input = move_blocks2(sparse_input)
    # print(f"The checksum is {compute_checksum(moved_input)}")
    