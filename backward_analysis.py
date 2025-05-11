# aka reaching defintiions
from get_in_out_sets import *

DEBUG = True


def debug_print(msg):
    if DEBUG:
        print(msg)

def backward_analysis(list_of_block_nodes):
    # for each block, we initialize in sets and out sets to prepare for reaching definitions
    in_sets, out_sets = get_in_out_sets(list_of_block_nodes)
    for index, block in enumerate(list_of_block_nodes):
        block.in_sets = in_sets[index + 1]
        block.out_sets = out_sets[index + 1]

    iteration = 1
    #  start
    print("========================================================================")
    print("Backward Analysis")
    changed = True
    while changed:
        changed = False
        debug_print(f"\n\nIteration: {iteration}")
        for block in list_of_block_nodes:
            debug_print("----------------------------------------")
            new_out_sets = set()

            # Ask if this needs to be reversed
            for successor in reversed(block.successors):
                # new_in_sets = new_in_sets.union(predecessor.out_sets)
                new_out_sets |= successor.in_sets  # or this
            
            # Look into how to make used sets
            new_in_sets = block.used_sets | (new_out_sets - block.kill_sets)

            debug_print(f"Block {block.block_number}")
            in_lines = sorted(set(line for _, line in block.in_sets))
            out_lines = sorted(set(line for _, line in block.out_sets))
            debug_print(f"  IN:  {in_lines}")
            debug_print(f"  OUT: {out_lines}")

            if new_in_sets != block.in_sets or new_out_sets != block.out_sets:
                changed = True
                block.in_sets = new_in_sets
                block.out_sets = new_out_sets

        iteration += 1

    print("\n\nBackward Analysis done.")