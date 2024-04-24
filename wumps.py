import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = (0, 0)
        self.gold_pos = self.generate_random_position()
        self.wumpus_pos = self.generate_random_position(exclude=[self.agent_pos, self.gold_pos])
        self.pit_pos = [self.generate_random_position(exclude=[self.agent_pos, self.gold_pos, self.wumpus_pos]) for _ in range(size)]
        self.has_gold = False
        self.has_arrow = True
        self.game_over = False

    def generate_random_position(self, exclude=[]):
        pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        while pos in exclude:
            pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        return pos

    def move_agent(self, direction):
        x, y = self.agent_pos
        if direction == 'up':
            x = max(0, x - 1)
        elif direction == 'down':
            x = min(self.size - 1, x + 1)
        elif direction == 'left':
            y = max(0, y - 1)
        elif direction == 'right':
            y = min(self.size - 1, y + 1)
        self.agent_pos = (x, y)

    def shoot_arrow(self, direction):
        if not self.has_arrow:
            print("No arrows left!")
            return
        self.has_arrow = False
        if direction == 'up' and self.wumpus_pos[1] == self.agent_pos[1] and self.wumpus_pos[0] < self.agent_pos[0]:
            self.wumpus_pos = (-1, -1)
            print("Wumpus killed!")
        elif direction == 'down' and self.wumpus_pos[1] == self.agent_pos[1] and self.wumpus_pos[0] > self.agent_pos[0]:
            self.wumpus_pos = (-1, -1)
            print("Wumpus killed!")
        elif direction == 'left' and self.wumpus_pos[0] == self.agent_pos[0] and self.wumpus_pos[1] < self.agent_pos[1]:
            self.wumpus_pos = (-1, -1)
            print("Wumpus killed!")
        elif direction == 'right' and self.wumpus_pos[0] == self.agent_pos[0] and self.wumpus_pos[1] > self.agent_pos[1]:
            self.wumpus_pos = (-1, -1)
            print("Wumpus killed!")
        else:
            print("Missed the shot!")

    def check_perceptions(self):
        perceptions = []

        # Check adjacent cells for pits and the Wumpus
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (dx != 0 or dy != 0) and (0 <= self.agent_pos[0] + dx < self.size) and (0 <= self.agent_pos[1] + dy < self.size):
                    if (self.agent_pos[0] + dx, self.agent_pos[1] + dy) in self.pit_pos:
                        perceptions.append("Breeze")
                    if (self.agent_pos[0] + dx, self.agent_pos[1] + dy) == self.wumpus_pos:
                        perceptions.append("Stench")

        # Check if gold is in adjacent cell
        for dx in [-1, 1]:
            if (0 <= self.agent_pos[0] + dx < self.size) and (self.agent_pos[0] + dx, self.agent_pos[1]) == self.gold_pos:
                perceptions.append("Glitter")
            if (0 <= self.agent_pos[1] + dx < self.size) and (self.agent_pos[0], self.agent_pos[1] + dx) == self.gold_pos:
                perceptions.append("Glitter")

        return perceptions

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_pos:
                    print("A", end=' ')
                elif (i, j) == self.gold_pos:
                    print("G", end=' ')
                elif (i, j) == self.wumpus_pos or (i, j) in self.pit_pos:
                    print("-", end=' ')
                else:
                    print("-", end=' ')
            print()

    def play(self):
        while not self.game_over:
            print("\nAgent's current position:")
            self.print_board()
            print("Perceptions:", self.check_perceptions())
            action = input("Enter action (move/shoot/exit): ")
            if action == 'exit':
                break
            elif action == 'move':
                direction = input("Enter direction (up/down/left/right): ")
                self.move_agent(direction)
            elif action == 'shoot':
                direction = input("Enter direction to shoot (up/down/left/right): ")
                self.shoot_arrow(direction)
            if self.agent_pos == self.gold_pos:
                self.has_gold = True
                self.game_over = True
                print("Agent found the gold!")
            if self.agent_pos == self.wumpus_pos:
                self.game_over = True
                print("Agent encountered the Wumpus and died!")
            if self.agent_pos in self.pit_pos:
                self.game_over = True
                print("Agent fell into a pit and died!")
        print("Game over!")

# Main loop
if __name__ == "__main__":
    size = int(input("Enter size of the Wumpus World (e.g., 4 for a 4x4 grid): "))
    wumpus_world = WumpusWorld(size=size)
    wumpus_world.play()
