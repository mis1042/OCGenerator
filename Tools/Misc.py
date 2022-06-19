def edit_debug(config, name, value):
    content = config.return_plist()
    content['Misc']['Debug'][name] = value
    config.edit_plist(content)


def edit_security(config, name, value):
    content = config.return_plist()
    content['Misc']['Security'][name] = value
    config.edit_plist(content)
