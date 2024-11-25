
# Identifiez le périphérique USB en fonction de son Vendor ID (VID) et Product ID (PID)
VENDOR_ID = 0x17CC  # xx17CC = ID Native Instruments
PRODUCT_ID = 0x2120  # Remplacez par votre PID 2120 = Komplete Kontrol S88, 1700=Maschine Mikro mk3

device_path = r"\\.\PhysicalDrive3"  # Remplacez '1' par le bon numéro
try:
    with open(device_path, 'rb') as device:
        print("Périphérique ouvert avec succès.")
except FileNotFoundError:
    print("Chemin invalide ou périphérique non trouvé.")
except PermissionError:
    print("Permissions insuffisantes pour accéder au périphérique.")