def edit_boot_args(config, boot_args):
    """
    Edit the Boot-args in the OpenCore-NVRAM configuration.

    :param config: The configuration object.
    :param boot_args: The boot-args to set.
    :return: None
    """
    content = config.return_plist()
    content['NVRAM']['Add']['7C436110-AB2A-4BBB-A880-FE41995C9F82']['boot-args'] = boot_args
    config.edit_plist(content)
