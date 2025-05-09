import re # for matching strings such as "goto X" or "if X then goto Y" to link blocks

def link_blocks(list_of_block_nodes):
    # list_of_block_nodes is an array of blocks
    # print(f"-----------------inside of link_blocks func:")
    
    # create a map of key: number, value: block
    blocks_map = {block.block_number: block for block in list_of_block_nodes} # map contains only blocks such as 11 blocks for test case #1
    # print(f"block map: {blocks_map}\n")

    for i, block in enumerate(list_of_block_nodes):
        # print(f"current block num: {i + 1}")
        if not block.instructions:
            continue

        last_instruction = block.instructions[-1].strip() # strip() for removing newlines
        # print(f"{i + 1} last_instruction: {last_instruction}")

        match_unconditional_goto = re.match(r'goto (\d+)', last_instruction) # match if unconditional goto
        match_conditional_goto = re.match(r'if .+ then goto (\d+)', last_instruction) # match if conditional

        if last_instruction == "return":
            continue # because no successors
        if match_unconditional_goto:
            block_num_to_jump = int(match_unconditional_goto.group(1)) # if it is "goto 5", it gets 5

            for candidate in list_of_block_nodes:
                if candidate.start_line_number == block_num_to_jump:
                    block.successors.append(candidate)
                    candidate.predecessors.append(block)
                    # print(f"block successor: {block.successors}")
                    break 

        if match_conditional_goto:
            block_num_to_jump = int(match_conditional_goto.group(1)) # if it is "goto 5", it gets 5

            for candidate in list_of_block_nodes:
                if candidate.start_line_number == block_num_to_jump:
                    block.successors.append(candidate)
                    candidate.predecessors.append(block)
                    # print(f"block successor: {block.successors}")
                    break 

        else: # fall through to next block
            if i + 1 < len(list_of_block_nodes):
                next_default_block = list_of_block_nodes[i + 1]
                block.successors.append(next_default_block)
                next_default_block.predecessors.append(block)



