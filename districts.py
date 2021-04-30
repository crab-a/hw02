import pandas
import data


class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        all_regions_list = self.dataset.get_all_districts()
        relevant_regions_list = []
        for region in all_regions_list:
            if region[0] in letters:
                relevant_regions_list.append(region)
        self.dataset.set_districts_data(relevant_regions_list)

    def print_details(self, features, statistic_functions):
        for feature in features:
            print(feature + ": ", end="")
            for func in statistic_functions:
                if func == statistic_functions[-1]:
                    print(func(data[feature]))
                else:
                    print("{:.14f}".format(func(data[feature])) + ", ", end="")





