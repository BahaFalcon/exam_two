#---вариант №1-------------

class Country:
    def __init__(self, name, population, territory, status):
        self.name = name if isinstance(name, str) else "Нет названия"
        self.population = population
        self.territory = territory
        self.status = status

    def set_population(self, population):
        if isinstance(population, int):
            self.population = population

    def set_territory(self, territory):
        if isinstance(territory, float):
            self.territory = territory

    def set_name(self, name):
        if isinstance(name, int):
            self.name = name

    def set_status(self):
        return self.status

    def display_info(self):
        return f"Страна:{self.name}\n" \
               f"Количество жителей:{self.population}\n" \
               f"Территория:{self.territory}км\n" \
               f"Государственный строй:{self.status}"

land = Country('Кыргызстан', '7 миллионов', '200 km2', 'демократия')
print(land.display_info())

#-------вариант №2 -----------

def country(name, **kwargs):
    print(f'{name}')
    for i in kwargs:
        print(f'{i} - {kwargs[i]}')

print(country(name='USA', population='330 million', is_democratic=True))
print(country(name='Kyrgyzstan', area='200 km2',
    have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China']))
