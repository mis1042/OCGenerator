def add_kext(config, comment, kext, executablepath):
    content = config.return_plist()
    content['Kernel']['Add'].append(
        {'Arch': 'Any', 'BundlePath': kext, 'Comment': comment, 'Enabled': True, 'ExecutablePath': executablepath,
         'MaxKernel': '', 'MinKernel': '', 'PlistPath': 'Contents/Info.plist'})
    config.edit_plist(content)


def edit_quirks(config, quirk, status):
    content = config.return_plist()
    content['Kext']['Quirks'][quirk] = status
    config.edit_plist(content)
