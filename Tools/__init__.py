from biplist import *


class Config:
    def __init__(self, path):
        self.plist = readPlist(path)
        # Clean up the plist
        # ACPI
        del self.plist['#WARNING - 1']
        del self.plist['#WARNING - 2']
        del self.plist['#WARNING - 3']
        del self.plist['#WARNING - 4']
        self.plist['ACPI']['Add'].clear()
        self.plist['ACPI']['Delete'].clear()
        self.plist['ACPI']['Patch'].clear()

        # Booter
        self.plist['Booter']['MmioWhitelist'].clear()
        self.plist['Booter']['Patch'].clear()

        # Kernel
        self.plist['Kernel']['Add'].clear()
        self.plist['Kernel']['Block'].clear()
        self.plist['Kernel']['Force'].clear()
        self.plist['Kernel']['Patch'].clear()

        # Misc
        self.plist['Misc']['Entries'].clear()
        self.plist['Misc']['Tools'].clear()

        # UEFI
        self.plist['UEFI']['Drivers'].clear()
        self.plist['UEFI']['ReservedMemory'].clear()

    def return_plist(self):
        return self.plist

    def edit_plist(self, content):
        self.plist = content

    def save(self, path):
        writePlist(self.plist, path, binary=False)
