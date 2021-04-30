import pandas


class Data:

    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        regions_set = {}
        for region in self.data["denominazione_region"]:
            regions_set.add(region)
        return list(regions_set)

    def set_districts_data(self, districts):

