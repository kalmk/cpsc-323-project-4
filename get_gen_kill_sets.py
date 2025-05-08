import re

# returns gen, kill sets
# gen = what this block defines keeps
# kill = what it erases from other block definition
def get_gen_kill_sets(list_of_block_nodes, all_definitions):
    gen = {}
    kill = {}

    for block in list_of_block_nodes:  # inside of a block
        # store for each block
        gen_set = set()
        kill_set = set()

        # print("----------------")
        # print(f"{block}\n")

        for index, instruction in enumerate(block.instructions):
            instruction = instruction.strip()

            # match assignments like X = Y, and X[T16]
            match_lhs = re.match(r'^(\w+)(\[[^\]]+\])?\s*=', instruction)
            # print(f"match: {match_lhs}")

            if match_lhs:
                # makes X = Y into just X, while Z[17] turns just Z
                variable = match_lhs.group(1)
                # print(f"var: {variable}")
                line_number = block.start_line_number + index
                # print(f"line number: {line_number}")
                definition = (variable, line_number)
                # print(f"definition: {definition}")
                gen_set.add(definition)
                # print(f"print: {gen_set}")

        # for kill set, find all definitions with the same variables but with different line numbers
        # definition is tuple (variable_lhs , line number)
        for definition in all_definitions:
            variable, line_number = definition
            # any() returns True if at least one element is True, if all false, return False
            # print(f"print: {gen_set}")
            # checking only the variable of tuple (v, n)
            if any(definition[0] == variable for definition in gen_set) and definition not in gen_set:
                    kill_set.add(definition)

        gen[block.block_number] = gen_set
        kill[block.block_number] = kill_set

    return gen, kill
                
                
