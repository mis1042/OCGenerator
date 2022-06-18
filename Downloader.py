import requests


def download_oc():
    # Download OpenCore
    response = requests.get('https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest')
    lastest_release = response.json()["tag_name"]
    try:
        open(f'Database/OpenCore/OpenCore-{lastest_release}-RELEASE.zip')
        print(f"OpenCore founded, {lastest_release}")
    except FileNotFoundError:
        print("OpenCore not found, downloading...")
        # Use Requests to download files
        response = requests.get(
            f'https://github.com/acidanthera/OpenCorePkg/releases/download/{lastest_release}/OpenCore-{lastest_release}-RELEASE.zip')
        with open(f'Database/OpenCore/OpenCore-{lastest_release}-RELEASE.zip', 'wb') as f:
            f.write(response.content)
        print("Downloaded OpenCore")


def download_acpi(acpi_name,path):
    """
    Download an ACPI file from the Database.

    :param acpi_name: ACPI File Name
    :return: None
    """

    try:
        f = open('Database/ACPI/acpi.json')
        lists = eval(f.read())
    except FileNotFoundError:
        print("ACPI Database is losing....")
        exit()

    for i in lists:
        if i["Name"] == acpi_name:
            print(i["Url"])
            response = requests.get(i["Url"])
            with open(f'{path}/{acpi_name}', 'wb') as f:
                f.write(response.content)
            return
        return "ACPI not found"
