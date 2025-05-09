import re

# access each block and get all the definition variables and their line number
def get_definitions(list_of_block_nodes):
    # (variable lhs, line number of that lhs)
    # set is used to avoid duplicates. definitions should be unique of their line number
    definitions = set()

    for block in list_of_block_nodes:
        # print("----------------")
        # print(f"{block}\n")

        # access each instruction inside array of instructions per block
        for index, instruction in enumerate(block.instructions):
            instruction = instruction.strip()  # to remove newline
            # print(f"instruction: {instruction}")

            # match assignments such as X = Y; returns None if no assignments
            assignment_match = re.match(r'(\w+)\s*=', instruction)
            # print(f"match: {assignment_match}")
            if assignment_match:
                variable_lhs = assignment_match.group(1) # for example, J = X; J is the lhs
                # print(f"variable: {variable_lhs}")
                # print(f"index: {index}")
                line_number = block.start_line_number + index
                # print(f"line_number for that instruction: {line_number}")
                definitions.add((variable_lhs, line_number))

    return definitions
