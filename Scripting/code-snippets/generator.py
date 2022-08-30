

class Asset(object):

    def __init__(self, data):
        self.__data = data

    @property
    def name(self):
        return self.__data['name']

    @property
    def category(self):
        return self.__data['category']


def get_assets():
    """Generator of assets.

    Yields:
        Asset: generated asset
    """
    raw_data = [{'name': 'tata', 'id': 123, 'info': 'ceci est un asset', 'category': 'prop'},
                {'name': 'toto', 'id': 234, 'info': 'ceci est un asset', 'category': 'char'},
                {'name': 'toto', 'id': 15, 'info': 'ceci est un asset', 'category': 'prop'},]

    for asset_data in raw_data:
        asset = Asset(asset_data)
        yield asset


def main():
    assets = get_assets()  # This does not create all the assets but rather a generator of asset
    filtered_assets = (a for a in assets if a.name == 'toto')  # Generator comprehension
    filtered_assets = (a for a in filtered_assets if a.category == 'prop')  # Second generator comprehension
    toto = next(filtered_assets)  # Ask for the next filtered asset
    print(toto, toto.name, toto.category)


if __name__ == '__main__':
    main()
