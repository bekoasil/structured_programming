#inheritance

# Vehicle
# -> Car
# -> Ship 
# -> Plane

from vehicle import Vehicle, Car, Ship, Plane
from hello.hello import hello as selam
from ..week10.file_read import averageFile #.. ile bir ust dizine gidip oradan import yapabiliyon


selam()

veni = Vehicle()
veni.go(100)

vici = Ship() 
vici.sound()
vici.go(200) #Vehicle'in ozelliklerini kalitsal olarak alir

vidi = Plane()
vidi.sound()
vidi.go(1300)

vecihi = Car()
vecihi.sound()
vecihi.go(100)
