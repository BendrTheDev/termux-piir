from piir.io import receive
from piir.decode import decode

keys = {}

while True:
    data = decode(receive(22))
    if data:
        break
keys['keyname'] = data