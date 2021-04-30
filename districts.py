import data


class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        all_regions_list = self.dataset.get_all_districts()


