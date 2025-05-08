class Block:
    def __init__(self, block_number, instructions):
        self.block_number = block_number
        self.instructions = instructions
        self.successors = []  
        self.predecessors = []  
