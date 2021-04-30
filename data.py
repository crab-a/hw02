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
        new_data = {}
        for i in self.data.keys():
            new_data.add(i)
        for index, region in enumerate(self.data["denominazione_region"]):
            if region in districts:
                for key in self.data.keys():
                    new_data[key][index] = self.data[key][index]
        self.data = new_data

