# aka reaching defintiions
from get_in_out_sets import *

def forward_analysis(list_of_block_nodes):
    # for each block, we initialize in sets and out sets to prepare for reaching definitions
    in_sets, out_sets = get_in_out_sets(list_of_block_nodes)
    for index, block in enumerate(list_of_block_nodes):
        block.in_sets = in_sets[index + 1]
        block.out_sets = out_sets[index + 1]

    iteration = 1

    #  start
    changed = True
    while changed:
        changed = False
        print(f"\n\niteration: {iteration}")
        for block in list_of_block_nodes:
            print("----------------------------------------")
            new_in_sets = set()
            for predecessor in block.predecessors:
                # new_in_sets = new_in_sets.union(predecessor.out_sets)
                new_in_sets |= predecessor.out_sets # or this

            new_out_sets = block.gen_sets | (new_in_sets - block.kill_sets)

            print(f"Block {block.block_number}")
            in_lines = sorted(set(line for _, line in block.in_sets))
            out_lines = sorted(set(line for _, line in block.out_sets))
            print(f"  IN:  {in_lines}")
            print(f"  OUT: {out_lines}")

            if new_in_sets != block.in_sets or new_out_sets != block.out_sets:
                changed = True
                block.in_sets = new_in_sets
                block.out_sets = new_out_sets

        iteration += 1