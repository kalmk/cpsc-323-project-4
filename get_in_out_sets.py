def get_in_out_sets(list_of_block_nodes):
    # in[B] is empty
    # out[B] is equal to gen[B]
    
    in_sets = {}
    out_sets = {}

    for block in list_of_block_nodes:
        in_sets[block.block_number] = set()
        out_sets[block.block_number] = block.gen_sets.copy()

    return in_sets, out_sets

        

