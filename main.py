import data
import districts
import statistics
import sys


def main(argv):
    #  q1
    print('Question 1:')

    the_data_q1 = data.Data(argv[1])
    dist1 = districts.Districts(the_data_q1)

    features = ['hospitalized_with_symptoms', 'intensive_care', 'total_hospitalized', 'home_insulation']
    statistic_functions = [statistics.mean, statistics.median]
    letters = ['S', 'L']

    dist1.filter_districts(letters)

    dist1.print_details(features, statistic_functions)

    #  q2
    print('\nQuestion 2:')

    the_data_q2 = data.Data(argv[1])  # dpc-covid19-ita-regioni_sample.csv"
    dist2 = districts.Districts(the_data_q2)
    dist2.determine_day_type()

    not_green_count = 0
    dist2.determine_day_type()
    districts_class = dist2.get_districts_class()
    for district in districts_class.keys():
        if districts_class[district] == 'not green':
            not_green_count += 1
    total_lockdown = not_green_count > 10

    print(f'Number of districts: {len(districts_class.keys())}')
    print(f"Number of not green districts: {not_green_count}")
    print(f"Will a lockdown be forced on whole of Italy?: {'yes' if total_lockdown else 'no'}")


if __name__ == '__main__':
    main(sys.argv)
