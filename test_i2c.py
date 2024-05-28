# Importer les bibliothèques utilisées
import machine

# Créer le périphérique I2C
sdaa=machine.Pin(8)
scla=machine.Pin(9)
i2c=machine.I2C(0,sda=sdaa, scl=scla, freq=400000)

# Scanner le bus I2C
print('Scan du bus i2c...')
devices = i2c.scan()

if len(devices) == 0:
    print("Aucun composant détecté !")
else:
    print('Composant(s) détectés :',len(devices))

for device in devices:
    print("Adresse en décimal : ",device," | Adresse en Hexadécimal : ",hex(device))
