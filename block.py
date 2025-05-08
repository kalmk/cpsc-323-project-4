class Block:
    def __init__(self, block_number, instructions):
        self.block_number = block_number
        self.instructions = instructions # array
        self.start_line_number = 0
        self.successors = []  
        self.predecessors = []  

    def __str__(self):
        return (
            f"Block Number: {self.block_number}\n"
            f"Instructions: {self.instructions}\n"
            f"Start Line Number: {self.start_line_number}\n"
            f"Successors: {self.successors}\n"
            f"Predecessors: {self.predecessors}"
        )
