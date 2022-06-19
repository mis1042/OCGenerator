def add_driver(config, path):
    content = config.return_plist()
    content['UEFI']['Drivers'].append({'Arguments': '', 'Comment': '', 'Enabled': True, 'Path': path})
    config.edit_plist(content)


def edit_quirks(config, quirk, status):
    content = config.return_plist()
    content['UEFI']['Quirks'][quirk] = status
    config.edit_plist(content)
