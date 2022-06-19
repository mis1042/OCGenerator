def edit_quirks(config, quirk, status):
    """
    Edit the quirk status in the OpenCore-Booter configuration.

    :param config: The configuration object.
    :param quirk: The Quirk name.
    :param status: The Quirk status.
    :return: None
    """
    content = config.return_plist()
    content['Booter']['Quirks'][quirk] = status
    config.edit_plist(content)
