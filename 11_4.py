from abc import ABC, abstractmethod


class Store():
    def __init__(self, amount):
        self.amount = amount
        self.store_equipment = dict()

    def transfer_to(self, of_eq, count):
        add_to_store = False

        if not isinstance(of_eq, OfficeEquipment):
            raise ValueError('Неправильный объект техники для передачи на склад.')

        if not isinstance(count, int) or count <= 0:
            raise ValueError(f'Неправильное количество ({count}) передаваемой на склад техники.')

        if self.amount < count:
            raise OutOfStockEx(self.amount, count)
        else:
            for i in self.store_equipment.keys():
                if of_eq.model in i.model:
                    self.store_equipment[i] += count
                    add_to_store = True
                    break
            if not add_to_store:
                self.store_equipment[of_eq] = count
            self.amount -= count
            return f'Оргтехника {of_eq.model} в количестве {count} шт. помещена на склад.'

    def transfer_from(self, model, count, department):
        is_model = False
        is_count_null = False

        if not isinstance(count, int) or count <= 0:
            raise ValueError(f'Неправильное количество ({count}) передаваемой в отдел техники.')

        if not isinstance(department, Department):
            raise ValueError('Неправильный отдел для получения техники.')

        for i in self.store_equipment.keys():
            if model in i.model:
                is_model = True
                if self.store_equipment[i] >= count:
                    self.store_equipment[i] -= count
                    if self.store_equipment[i] == 0:
                        is_count_null = i
                    department.add_equipment(i, count)
                    self.amount += count
                    break
                else:
                    return f'Нет запрашиваемого количества {model}.'

        if is_count_null:
            del self.store_equipment[is_count_null]

        if is_model:
            return f'{model} в количестве {count} шт. переданы со склада в {department.name}.'
        else:
            return (f'Запрашиваемой модели {model} нет на складе.')

    @property
    def inventory(self):
        item = 1
        result = 'На складе имеются в данный момент:'

        for key, value in self.store_equipment.items():
            result = ''.join([result, f'\n{item}. В количестве {value} шт.\n{key}'])
            item += 1
        result = ''.join([result, f'\nНа складе осталось мест: {self.amount}.'])
        return result


class OutOfStockEx(Exception):
    def __init__(self, amount, count):
        self.amount = amount
        self.count = count

    def __str__(self):
        return f'Оргтехника ({self.count} шт.) не помещается на склад. Осталось {self.amount} мест.'


class OfficeEquipment(ABC):
    def __init__(self, model, max_size, warranty):
        self.model = model
        self.max_size = max_size
        self.warranty = warranty

    @abstractmethod
    def __str__(self):
        """Характеристики оргтехники"""


class Printer(OfficeEquipment):
    def __init__(self, model, max_size, warranty, laser, color, speed_print, capacity):
        super().__init__(model, max_size, warranty)
        self.laser = laser
        self.color = color
        self.speed_print = speed_print
        self.capacity = capacity

    def __str__(self):
        return f'Принтер {self.model} имеет следующие характеристики:' \
               f'\n\tтехнология печати: {self.laser}' \
               f'\n\tцветной/ч-б: {"цветной" if self.color else "черно-белый"}' \
               f'\n\tскорость печати А4 (стр./мин.): {self.speed_print}' \
               f'\n\tлоток подачи емкость (лист.): {self.capacity}' \
               f'\n\tмакс. формат бумаги: {self.max_size}' \
               f'\n\tгарантия (мес.): {self.warranty}'


class Scaner(OfficeEquipment):
    def __init__(self, model, max_size, warranty, resolution, speed_scan, autofeed, duplex_scan):
        super().__init__(model, max_size, warranty)
        self.resolution = resolution
        self.speed_scan = speed_scan
        self.autofeed = autofeed
        self.duplex_scan = duplex_scan

    def __str__(self):
        return f'Сканер {self.model} имеет следующие характеристики:' \
               f'\n\tмакс. формат бумаги: {self.max_size}' \
               f'\n\tразрешение сканирования (dpi): {self.resolution}' \
               f'\n\tскорость сканирования (стр./мин.): {self.speed_scan}' \
               f'\n\tавтоподача оригиналов: {"есть" if self.autofeed else "нет"}' \
               f'\n\tдвустороннее сканирование: {"есть" if self.duplex_scan else "нет"}' \
               f'\n\tмакс. формат бумаги: {self.max_size}' \
               f'\n\tгарантия (мес.): {self.warranty}'


class Xerox(OfficeEquipment):
    def __init__(self, model, max_size, warranty, laser, color, desktop, speed_copy, capacity, resolution):
        super().__init__(model, max_size, warranty)
        self.laser = laser
        self.color = color
        self.desktop = desktop
        self.speed_copy = speed_copy
        self.capacity = capacity
        self.resolution = resolution

    def __str__(self):
        return f'Ксерокс {self.model} имеет следующие характеристики:' \
               f'\n\tтехнология печати: {self.laser}' \
               f'\n\tцветной/ч-б: {"цветной" if self.color else "черно-белый"}' \
               f'\n\tразмещение: {"настольный" if self.desktop else "напольный"}' \
               f'\n\tскорость копирования А4 (стр./мин.): {self.speed_copy}' \
               f'\n\tлоток подачи емкость (лист.): {self.capacity}' \
               f'\n\tразрешение сканирования (dpi): {self.resolution}' \
               f'\n\tмакс. формат бумаги: {self.max_size}' \
               f'\n\tгарантия (мес.): {self.warranty}'


class Department:
    def __init__(self, name):
        self.name = name
        self.equipment = dict()

    def add_equipment(self, of_eq, count):
        for i in self.equipment.keys():
            if of_eq.model in i.model:
                self.equipment[i] += count
                count = 0
                break
        if count != 0:
            self.equipment[of_eq] = count

    @property
    def inventory(self):
        return ''.join(f'{self.name}: {key.model} - {value} шт.\n' for key, value in self.equipment.items())


if __name__ == "__main__":
    x1 = Xerox('Pantum M6500', 'A4', 24, 'лазерный', False, True, 22, 150, 1200)
    x2 = Xerox('HP Laser 135w', 'A4', 12, 'лазерный', False, True, 20, 150, 600)
    x3 = Xerox('Xerox WorkCentre 7120', 'A3', 12, 'лазерный', True, False, 20, 1090, 600)
    p1 = Printer('Xerox Phaser 3020', 'A4', 12, 'лазерный', False, 20, 150)
    p2 = Printer('Canon Pixma G1411', 'A4', 12, 'струйный', True, 8, 100)
    p3 = Printer('Pantum P2207', 'A4', 24, 'лазерный', False, 20, 150)
    s1 = Scaner('Canon image Formula DR-C225W', 'A4', 36, 600, 25, True, True)
    s2 = Scaner('Fujitsu ScanShap iX1600', 'A4', 12, 600, 40, True, True)
    # print(x2)
    our_store = Store(20)
    try:
        print(our_store.transfer_to(x1, 2))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    print(our_store.inventory)
    try:
        print(our_store.transfer_to(x2, 3))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(x3, 1))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(p1, 5))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(p2, 2))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(p3, 7))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(s1, 1))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(s2, 1))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    try:
        print(our_store.transfer_to(p2, 1))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
    # print(our_store.inventory)
    d1 = Department('Секретариат')
    try:
        print(our_store.transfer_from('Pantum M6500', 2, d1))
    except ValueError as err:
        print(err)
    try:
        print(our_store.transfer_from('Canon Pixma G1411', 5, d1))
    except ValueError as err:
        print(err)
    try:
        print(our_store.transfer_from('ABC', 2, d1))
    except ValueError as err:
        print(err)
    # print(our_store.inventory)
    print(d1.inventory)
    try:
        print(our_store.transfer_to(p2, 1))
    except ValueError as err:
        print(err)
    except OutOfStockEx as err:
        print(err)
