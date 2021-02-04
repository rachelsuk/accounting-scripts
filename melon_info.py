"""Print out all the melons in our inventory."""
from melons import melons_info

def print_melon(melon, data):
    """Print each melon with corresponding attribute information."""
    print(melon)
    for data_title, data_value in data.items():
        print((' ' * 4) + f'{data_title}: {data_value}')


for melon, data in melons_info.items():
    print_melon(melon, data)