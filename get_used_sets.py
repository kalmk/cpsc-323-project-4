import re

def get_used_sets(list_of_block_nodes):
    used = {}

    for block in list_of_block_nodes:  # inside of a block
        # store for each block
        used_set = set()
        defined_set = set()

        for index, instruction in enumerate(block.instructions):
            instruction = instruction.strip()

            # Extract left-hand side (LHS) and right-hand side (RHS)
            match = re.match(r"(\w+)\s*=\s*(.*)", instruction)
            if match:
                lhs = match.group(1)
                rhs = match.group(2)

                # Identify used variables (before they are defined)
                rhs_vars = set(re.findall(r"\b[a-zA-Z_]\w*\b", rhs))
                used_set.update(rhs_vars - defined_set)

                # Mark LHS as defined
                defined_set.add(lhs)
        
        used[block.block_number] = used_set
    
    return used
