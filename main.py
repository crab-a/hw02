import data
import districts
import statistics
import sys


def main(argv):
    the_data = data.Data("dpc-covid19-ita-regioni_sample.csv")  # change to argv[1]
    dist = districts.Districts(the_data)
    dist.determine_day_type()

    #  q1
    print('Question 1:')
    features = ['hospitalized_with_symptoms', 'intensive_care', 'total_hospitalized', 'home_insulation']
    statistic_functions = [statistics.mean, statistics.median]
    dist.print_details(features, statistic_functions)

    #  q2
    print('\nQuestion 2:')
    not_green_count = 0
    dist.determine_day_type()
    districts_class = dist.get_districts_class()
    for district in districts_class.keys():
        if districts_class[district] == 'not green':
            not_green_count += 1
    total_lockdown = not_green_count > 10
    print(f'number of districts: {len(districts_class.keys())}')
    print(f"Number of not green districts: {not_green_count}")
    print(f"Will a lockdown be forced on whole of Italy?: {'yes' if total_lockdown else 'no'}")


if __name__ == '__main__':
    main(sys.argv)
