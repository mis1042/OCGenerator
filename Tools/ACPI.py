def add_aml(config, comment, path):
    """
    Add a new AML file to the OpenCore-ACPI configuration.

    :param config: The configuration object.
    :param comment: The aml file comment.
    :param path: The aml file path.
    :return: None
    """
    content = config.return_plist()
    content['ACPI']['Add'].append({'Comment': comment, 'Enabled': True, 'Path': path})
    config.edit_plist(content)


def add_patcher(config, comment, count, limit, find, replace):
    """
    Add a new patcher to the OpenCore-ACPI configuration.

    :param config: The configuration object.
    :param comment: The patcher comment.
    :param count: The patcher count.
    :param limit: The patcher limit.
    :param find: The value that this patch should look for
    :param replace:The value that this patch should replace
    :return:None
    """
    content = config.return_plist()
    content['ACPI']['Patch'].append(
        {'Comment': comment, 'Count': count, 'Enabled': True, 'Find': find, 'Limit': limit, 'Replace': replace})
    config.edit_plist(content)


def edit_quirks(config, quirk, status):
    """
    Edit the quirk status in the OpenCore-ACPI configuration.

    :param config: The configuration object.
    :param quirk: The Quirk name.
    :param status: The Quirk status.
    :return: None
    """
    content = config.return_plist()
    content['ACPI']['Quirks'][quirk] = status
    config.edit_plist(content)