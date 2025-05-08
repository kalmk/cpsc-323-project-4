# CPSC 323
# Project 4
from leader import *
from block import *
from link_blocks import *

if (__name__ == "__main__"):
    tac_code = {}
    filename = 'test_cases/test1.in'

    # Read lines from input and store them
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            tac_code[index + 1] = line

    # print(tac_code)

    # Find Leaders
    leaders = find_leaders(tac_code)
    # print(f"leaders: {leaders}")
    # print(f"size: {len(leaders)}")

    # Find Blocks
    blocks = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line_num in enumerate(leaders):
            if (index == 0):
                continue
            block = []
            for i in range(leaders[index - 1] - 1, leaders[index] - 1):
                block += [lines[i]]

            blocks.append(block)
        
        # Still need to append last block
        block = []
        for i in range(leaders[-1] - 1, len(tac_code)):
            block += [lines[i]]
        blocks.append(block)
    
    # Print out all blocks
    # for index, block in enumerate(blocks):
    #     print(f"Block {index + 1}: {block}")

    # print(blocks)

    # instantiate blocks with line number and its instructions
    list_of_block_nodes = []
    for i, array_of_instruc in enumerate(blocks):
        block_node = Block(i + 1, array_of_instruc)
        list_of_block_nodes.append(block_node)

    # starting number for each blocks (line number for leaders)
    for index_for_leaders, block in enumerate(list_of_block_nodes):
        block.start_line_number = leaders[index_for_leaders]

    # links successors and predecessors for each block via jump targets, and fall throughs
    link_blocks(list_of_block_nodes)

    # check each node information
    # for i in list_of_block_nodes:
    #     print(i)
    #     print("-----")

    





    

