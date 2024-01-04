class Home:

    def new(self, arg):
        try:
            arg = int(arg)
            print("Аргумент является целым числом")
        except ValueError:
            print("Аргумент не является целым числом")


home=Home ()
prov = input('введите аргумент ')

home.new(prov)
print(home.new)
