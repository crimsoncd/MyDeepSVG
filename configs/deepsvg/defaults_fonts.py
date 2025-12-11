from .default_icons import *


class Config(Config):
    def __init__(self, num_gpus=1):
        super().__init__(num_gpus=num_gpus)

        # Dataset
        self.data_dir = "./dataset/svgs_simplified/"
        self.meta_filepath = "./dataset/svg_meta.csv"
