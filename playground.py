import time
class MersenneTwister:
    def __init__(self, seed):
        # Init an array with 624 zeros
        self.state = [0] * 624
        self.index = 0

        # First element as the seed
        self.state[0] = seed
        for i in range(1, 624):
            self.state[i] = (1812433253 * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i) & 0xFFFFFFFF

    def extract_number(self) -> int:
        if self.index == 0:
            self.generate_numbers()

        y = self.state[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 0x9D2C5680)
        y = y ^ ((y << 15) & 0xEFC60000)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        return y

    def generate_numbers(self):
        for i in range(624):
            y = (self.state[i] & 0x80000000) + (self.state[(i + 1) % 624] & 0x7fffffff)
            self.state[i] = self.state[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.state[i] = self.state[i] ^ 0x9908B0DF


# Example usage:
mt = MersenneTwister(seed=int(time.time()))  # Initialize with seed

random_number = mt.extract_number() # Generate random number
print("Random number:", random_number)

