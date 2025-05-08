# cfg_builder.py
# Constructs the Control Flow Graph from basic blocks

from leader import find_target_of_goto 

def build_cfg(blocks, leaders):
    cfg = {}

    # Map each leader line number to a block number (1-based)
    line_to_block = {line: idx + 1 for idx, line in enumerate(leaders)}

    def get_block_num_from_line(target_line):
        # Returns block number that starts at target line
        return line_to_block.get(target_line)
    
    for idx, block in enumerate(blocks):
        block_num = idx + 1
        successors = []

        # Get the last instruction in the current block
        last_instr = block[-1].strip()

        # Case 1: Conditional jump 
        if "if" in last_instr and "goto" in last_instr:
            target = find_target_of_goto(last_instr)
            target_block = get_block_num_from_line(target)
            if target_block:
                successors.append(block_num + 1)
        
        # Case 2: Unconditional jump
        elif last_instr.startswith("goto"):
            target = find_target_of_goto(last_instr)
            target_block = get_block_num_from_line(target)
            if target_block:
                successors.append(target_block)
        
        elif last_instr.startswith("return"):
            pass
        
        else:
            if block_num < len(blocks):
                successors.append(block_num + 1)
        
        cfg[block_num] = successors
    
    return cfg



    # Step 3:
    # cfg = build_cfg(blocks, leaders)
    # print("\n=== Control Flow Graph ===")
    # for block_num, successors in cfg.items():
    #     print(f"Block {block_num} -> {successors}")