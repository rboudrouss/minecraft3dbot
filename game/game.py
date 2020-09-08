import numpy as np
import sys
import os

if 'emoji_generator' in os.listdir(os.path.abspath(os.getcwd())):
    sys.path.insert(1, './emoji_generator')
    from emoji_generator import DISCORD_EMOJIS_EQ
else:
    raise ModuleNotFoundError


class Game:

    def __init__(self, dimensions):
        self.MAXDEPTH = 5
        self.shape = dimensions
        self.depth_array = np.full(self.shape, 0)
        self.selected_block = [0, 0]
        self.emoji_array = np.full(self.shape, '', dtype='<U6')

    def get_shape(self):
        return list(self.shape)

    def get_depth_array(self):
        return self.depth_array

    def discord_emoji_array(self):
        discord_emojis = np.full(self.shape, '', dtype='<U50')
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                discord_emojis[i,
                               j] = f":{DISCORD_EMOJIS_EQ.get(self.emoji_array[i,j])}:"
        return discord_emojis

    def destroy_block(self, bloc_co):
        if self.depth_array[bloc_co[0], bloc_co[1]] < self.MAXDEPTH:
            self.depth_array[bloc_co[0], bloc_co[1]] += 1
            print(f"bloc {bloc_co} destroyed")
            return True
        else:
            return False

    def render_emojis(self):
        print("generating emojis...")
        self.emoji_array = np.full(self.shape, '', dtype='<U6')
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                current_depth = self.depth_array[i, j]

                if self.selected_block == [i, j]:
                    self.emoji_array[i, j] += 's'

                if j < self.shape[1]-1 and self.depth_array[i, j+1] < current_depth:
                    self.emoji_array[i, j] += 'r'

                if j > 0 and self.depth_array[i, j-1] < current_depth:
                    self.emoji_array[i, j] += 'l'

                if i < self.shape[0]-1 and self.depth_array[i+1, j] < current_depth:
                    self.emoji_array[i, j] += 'u'

                if i > 0 and self.depth_array[i-1, j] < current_depth:
                    self.emoji_array[i, j] += 'd'

                if self.depth_array[i, j] == 0 and self.emoji_array[i, j] == '':
                    self.emoji_array[i, j] = "i"

        print('emojis generated')
        return self.discord_emoji_array()

    def selected_move(self, up: int, down: int):
        """
        up and down must be equal either to 1 or -1
        """
        self.selected_block[0] += up
        self.selected_block[1] += down
        for i in range(len(self.selected_block)):
            if self.selected_block[i] < 0:
                self.selected_block[i] = 0


if __name__ == "__main__":
    game = Game((3, 3))
    game.destroy_block((1, 1))
    game.render_emojis()
    print(game.get_depth_array())
    print(game.render_emojis())
