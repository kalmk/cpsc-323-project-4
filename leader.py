# leader.py
# Used to find leaders in TAC code

# 3 Rules for finding Leaders in TAC Code
#   1. First instruction is always a leader
#   2. Targets of jumps are leaders
#   3. Instructions following jumps are leaders

def find_target_of_goto(line):
    goto_index = line.index("goto")
    # print(goto_index)
    line_num_str = ""
    for char in line[goto_index + 5:]:
        # print(f"DEBUG: char = {char}")
        if (char.isdigit()):
            line_num_str += char
        else:
            break
    if (not line_num_str.isnumeric()):
        raise("Line num is not numeric, something went wrong")
    line_num = int(line_num_str)
    return line_num

def find_leaders(tac_code):
    lines_of_code = len(tac_code)
    print(f"length of tac code = {lines_of_code}")
    leaders = []

    for line_num, line in tac_code.items():
        # Check if first line
        if (line_num == 1):
            leaders.append(line_num)

        # Check if we have a 'goto' in line
        if ("goto" in line):
            # Check target of goto statement
            target_line_num = find_target_of_goto(line)
            # print(target_line_num)
            if (target_line_num not in leaders):
                leaders.append(target_line_num)

            # Check if next line exists
            if (((line_num + 1) <= lines_of_code) and ((line_num + 1) not in leaders)):
                leaders.append(line_num + 1)

    # print(leaders)
    leaders.sort()
    return leaders