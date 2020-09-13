import numpy as np
import sys
import os


class Game:

    def __init__(self, dimensions):
        self.MAXDEPTH = -5
        self.shape = dimensions
        self.depth_array = np.full(self.shape, 0)
        self.selected_block = [0, 0]
        self.emoji_array = np.full(self.shape, '', dtype='<U6')

    def get_shape(self):
        return list(self.shape)

    def get_depth_array(self):
        return self.depth_array

    def get_emoji_array(self):
        return self.emoji_array

    def interact_block(self, interaction_type):
        """
        interaction_type = -1 to destroy or 1 to place
        """
        self.depth_array[
            self.selected_block[0],
            self.selected_block[1],
        ] += interaction_type
        print(f"bloc at {self.selected_block} " +
              "detroyed" if interaction_type == -1 else "placed")

    def render_emojis(self):
        print("\ngenerating emojis...")
        self.emoji_array = np.full(self.shape, '', dtype='<U6')
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                current_depth = self.depth_array[i, j]

                if self.selected_block == [i, j]:
                    self.emoji_array[i, j] += 's'

                # respect the order rlud
                if j < self.shape[1]-1 and self.depth_array[i, j+1] < current_depth:
                    self.emoji_array[i, j] += 'r'

                if j > 0 and self.depth_array[i, j-1] < current_depth:
                    self.emoji_array[i, j] += 'l'

                if i > 0 and self.depth_array[i-1, j] < current_depth:
                    self.emoji_array[i, j] += 'u'

                if i < self.shape[0]-1 and self.depth_array[i+1, j] < current_depth:
                    self.emoji_array[i, j] += 'd'

                if self.depth_array[i, j] == 0 and self.emoji_array[i, j] == '':
                    self.emoji_array[i, j] = "i"

        print('emojis generated\n')
        return self.emoji_array

    def selected_move(self, vertical, horizontal):
        """
        up and down must be equal either to 1 or -1
        """
        self.selected_block[0] += vertical
        self.selected_block[1] += horizontal
        for i in range(len(self.selected_block)):
            if self.selected_block[i] < 0:
                self.selected_block[i] = 0


if __name__ == "__main__":
    game = Game((3, 3))
    game.destroy_block((1, 1))
    print(game.get_depth_array())
    print(game.render_emojis())
