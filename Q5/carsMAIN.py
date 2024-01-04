from cars.bmw import BMW
from cars.audi import Audi
from cars.nissan import Nissan

bmw_car = BMW(model="Xs")
bmw_car.start_engine()
bmw_car.drive()
print()
audi_car = Audi(model="etron")
audi_car.start_engine()
audi_car.drive()
print()
nissan_car = Nissan(model="Altima")
nissan_car.start_engine()
nissan_car.drive()