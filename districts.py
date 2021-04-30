import pandas
import data


class Districts:
    def __init__(self, dataset):
        """
        initial the districts object by using data object
        :param dataset: the dataset that we work with
        """
        self.dataset = dataset

    def filter_districts(self, letters):
        """
        that method receives a list of letters and change the object according that list and the region names
        in the object
        :param letters: a list of letters to convert the object by
        :return: void
        """
        all_regions_list = self.dataset.get_all_districts()
        relevant_regions_list = []
        for region in all_regions_list:
            if region[0] in letters:
                relevant_regions_list.append(region)
        self.dataset.set_districts_data(relevant_regions_list)

    def print_details(self, features, statistic_functions):
        """
        that method receives lists of features and statistic_funcs and print the results of the funcs according
        the features which are keys in the object
        :param features: a list of features to print stats for
        :param statistic_functions: a list of statistic funcs
        :return: void
        """
        for feature in features:
            print(feature + ": ", end="")
            for func in statistic_functions:
                if func == statistic_functions[-1]:
                    print(func(data[feature]))
                else:
                    print("{:.14f}".format(func(data[feature])) + ", ", end="")





