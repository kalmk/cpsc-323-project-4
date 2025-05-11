class Block:
    def __init__(self, block_number, instructions):
        self.block_number = block_number
        self.instructions = instructions  # array
        self.start_line_number = 0
        self.successors = []
        self.predecessors = []
        self.used_sets = set()
        self.gen_sets = set()
        self.kill_sets = set()
        self.in_sets = set()
        self.out_sets = set()

    def __str__(self):
        return (
            f"block number: {self.block_number}\n"
            # f"instructions: {self.instructions}\n"
            # f"start line Number: {self.start_line_number}\n"
            f"successors: {[b.block_number for b in self.successors]}\n"
            f"predecessors: {[b.block_number for b in self.predecessors]}\n"
            # f"gen set: {self.gen_sets}\n"
            # f"kill set: {self.kill_sets}\n"
            # f"in set: {self.in_sets}\n"
            # f"out set: {self.out_sets}\n"
        )
