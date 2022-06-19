from Tools import Config, ACPI, Booter, Kernel, Misc, NVRAM, UEFI, Downloader
import json
import zipfile
import shutil

# Download OpenCore
version = Downloader.download_oc()


def init():
    # Clean the folder
    shutil.rmtree('output', ignore_errors=True)

    # Unzip OpenCore
    with zipfile.ZipFile(f'Database/OpenCore/OpenCore-{version}-RELEASE.zip', 'r') as zip_ref:
        zip_ref.extractall('.tmp/')

    # Building
    print("Building OpenCore Files")
    shutil.move('.tmp/X64', 'output/')
    shutil.move('.tmp/Docs/Sample.plist', 'output/EFI/OC/config.plist')

    # Cleaning
    shutil.rmtree('.tmp/')


def generator(config_path):
    init()
    # Load the config
    config_json = json.loads(open(config_path).read())
    # Load OpenCore config
    c = Config('output/EFI/OC/config.plist')

    # Set the config

    # ACPI-Add
    for i in config_json["ACPI"]['Add']:
        ACPI.add_aml(c, i, i)
    # ACPI-Patch
    for i in config_json["ACPI"]['Patch']:
        ACPI.add_patcher(c, comment=i["Comment"], count=i["Count"], limit=i["Limit"], find=i["Find"],
                         replace=i["Replace"])
    # Booter-Quirks
    for i in config_json["Booter"]['Quirks']:
        name = i.split(',')[0]
        status = bool(i.split(',')[1])
        Booter.edit_quirks(c, name, status)

    # Kernel-Quirks
    for i in config_json["Kernel"]['Quirks']:
        name = i.split(',')[0]
        status = bool(i.split(',')[1])
        Kernel.edit_quirks(c, name, status)

    # Misc-Debug
    for i in config_json["Misc"]['Debug']:
        if type(i) == dict:
            name = i['Name']
            status = i['Value']
            Misc.edit_debug(c, name, status)
        else:
            name = i.split(',')[0]
            status = i.split(',')[1]
            if status == "True" or status == "False":
                status = bool(status)
            Misc.edit_debug(c, name, status)

    # Misc-Security
    for i in config_json["Misc"]['Security']:
        if type(i) == dict:
            name = i['Name']
            status = i['Value']
            Misc.edit_security(c, name, status)
        else:
            name = i.split(',')[0]
            status = i.split(',')[1]
            if status == "True" or status == "False":
                status = bool(status)
            Misc.edit_security(c, name, status)

    # UEFI-Drivers
    for i in config_json["UEFI"]['Drivers']:
        UEFI.add_driver(c, i)

    # UEFI-Quirks
    for i in config_json["UEFI"]['Quirks']:
        name = i.split(',')[0]
        status = bool(i.split(',')[1])
        UEFI.edit_quirks(c, name, status)

    c.save('output/EFI/OC/config.plist')

    # Get ACPI Files
    for i in config_json["ACPI"]['Add']:
        print(f"Downloading {i}")
        Downloader.download_acpi(i, 'output/EFI/OC/ACPI')

    print("Generator Compete!, OpenCore is ready to be used, please check the output folder")
    print("We don`t remove redundant Drivers and Tools,You can load Other Drivers and Tools")