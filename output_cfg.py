def output_cfg(blocks):
    print("\n\n====================================================================")
    print("Control Flow Graph:\n")
    for block in blocks:
        successors = ", ".join(str(successor.block_number) for successor in block.successors)
        predecessors = ", ".join(str(predecessor.block_number)
                                 for predecessor in block.predecessors)
        print(f"Block {block.block_number}")
        print(f"  -> Successors   : {successors if successors else 'None'}")
        print(
            f"  <- Predecessors : {predecessors if predecessors else 'None'}\n")

    print("====================================================================")
