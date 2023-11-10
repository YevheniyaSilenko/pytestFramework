import re

my_string = ("Place of delivery of goods or place of performance of work or provision of services: 82172, Ukraine, "
             "Lviv Region, Stebnyk, str. Doroshenko, 1 Deadline for delivery of goods, performance of works or "
             "provision of services: 31.12.2023")

if __name__ == '__main__':
    data = {}

    # Country
    match_country = re.search(r', (\w+),', my_string)
    data['country'] = match_country.group(1) if match_country else None

    # Region
    match_region = re.search(r', (\w+ Region),', my_string)
    data['region'] = match_region.group(1) if match_region else None

    # City
    match_city = re.search(r', (\w+), str\.', my_string)
    data['city'] = match_city.group(1) if match_city else None

    # Postal
    match_postal = re.search(r': (\d+),', my_string)
    data['postal'] = match_postal.group(1) if match_postal else None

    # Address
    match_address_part1 = re.search(r', (\w+), (\d+)', my_string)
    match_address_part2 = re.search(r', (\d+)', my_string)
    data['address'] = match_address_part1.group(1) + ', ' + match_address_part2.group(1) if match_address_part1 and match_address_part2 else None

    # Deadline
    match_deadline = re.search(r': (\d{2}\.\d{2}\.\d{4})', my_string)
    data['deadline'] = match_deadline.group(1) if match_deadline else None

    print(data)
