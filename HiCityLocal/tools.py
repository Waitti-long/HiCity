class CityFinder:
    """
    城市搜索
    """
    def __init__(self):
        pass

    def find_city(self, city_map, string: str):
        res = []
        for city in city_map.keys():
            if city.startswith(string):
                res.append(city)
        return res[:1]

    def find_city_code(self, city_map, string: str):
        if string in city_map:
            return city_map[string]
        return ""
