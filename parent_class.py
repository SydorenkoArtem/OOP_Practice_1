class Element:
    t_solid = 1538
    t_gas = 2862

    def __init__(self, temperature: int, temperature_variety: str):
        self.temperature: int = temperature
        self.temperature_variety: str = temperature_variety

    def scale_degree(self):
        if self.temperature_variety == "f":
            t = ((self.temperature - 32) * 5) / 9
            return self.agg_state(t)
        elif self.temperature_variety == "k":
            t = self.temperature - 273.15
            return self.agg_state(t)

    def agg_state(self, t):
        if t > self.t_gas:
            return 'Т испарения'
        elif self.t_solid <= t < self.t_gas:
            return 'Т плавления'
        else:
            return 'Т твердения'


class Iron(Element):
    pass


print(Iron(2000, "f").scale_degree())
