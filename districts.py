

class Districts:
    def __init__(self, dataset):
        """
        initial the districts object by using data object
        :param dataset: the dataset that we work with
        """
        self.dataset = dataset

    def filter_districts(self, letters):
        """
        that method receives a list of letters and change the object according to that list and the region names
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
                    print(func(self.dataset.data[feature]))
                else:
                    print("{:.14f}".format(func(self.dataset.data[feature])) + ", ", end="")

    def determine_day_type(self):
        """
        add new column to the dataset which tells if it was a good day
        :return: void
        """
        day_type = []
        values = {}
        for index, day in enumerate(self.dataset.data['data']):
            is_good_day = self.dataset.data['resigned_healed'][index] > self.dataset.data['new_positives'][index]
            day_type.append(is_good_day)
        values['day_type'] = day_type  # im not sure it doesn't add a list with the wrong order
        self.dataset.data.update(values)

    def get_districts_class(self):
        """
        make a dictionary of all districts as keys and the values tells if the district is considered green
        :return: the dictionary
        """
        regions = self.dataset.get_all_districts()
        district_class = dict.fromkeys(regions, 0)
        for entry, day in enumerate(self.dataset.data['data']):
            if self.dataset.data['day_type'][entry]:
                district_class[self.dataset.data['denominazione_region'][entry]] += 1
        for region in regions:
            if district_class[region] > 340:
                district_class[region] = 'green'
            else:
                district_class[region] = 'not green'

        return district_class
