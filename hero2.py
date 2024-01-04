class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        print(f"Имя героя: {self.name}")

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}\nСуперспособность: {self.superpower}\nЗдоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    location = 'воздушные'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self, true_phrase):
        return true_phrase in str(self.fly)


class EarthHero(SuperHero):
    location = 'земные'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self, true_phrase):
        return true_phrase in str(self.fly)


class CosmicHero(SuperHero):
    location = 'космические'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self, true_phrase):
        return true_phrase in str(self.fly)


class Villain(CosmicHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, other_hero):
        other_hero.health_points **= self.damage


# Создание объектов и вызов методов
air_hero = AirHero("Sky Master", "Воздушный Властелин", "Контроль над воздухом", 80, "Я владыка ветров!", damage=5)
earth_hero = EarthHero("Earth Guardian", "Земной Страж", "Сила земли", 90, "Защитник природы!", damage=7)
cosmic_hero = CosmicHero("Star Voyager", "Звездный Путешественник", "Сверхскорость", 120, "В бескрайние галактики!", damage=10)

villain = Villain("Dark Destroyer", "Темный Уничтожитель", "Тьма и разрушение", 150, "Твой конец близок!", damage=15)

air_hero.double_health_points()
print(air_hero)
print(air_hero.true_in_true_phrase(True))

earth_hero.double_health_points()
print(earth_hero)
print(earth_hero.true_in_true_phrase(True))

cosmic_hero.double_health_points()
print(cosmic_hero)
print(cosmic_hero.true_in_true_phrase(True))

villain.crit(air_hero)
print(f"Здоровье {air_hero.name} после атаки врага: {air_hero.health_points}")