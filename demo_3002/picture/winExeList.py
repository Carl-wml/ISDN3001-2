import winreg

def get_installed_apps():
    # Open the registry key for installed applications
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    # Get the number of subkeys (installed applications)
    num_apps = winreg.QueryInfoKey(key)[0]
    # Iterate over the subkeys and retrieve the display name, publisher, and installation path for each installed application
    apps = []
    for i in range(num_apps):
        app_key = winreg.EnumKey(key, i)
        app_subkey = winreg.OpenKey(key, app_key)
        try:
            display_name, _ = winreg.QueryValueEx(app_subkey, "DisplayName")
            publisher, _ = winreg.QueryValueEx(app_subkey, "Publisher")
            install_location, _ = winreg.QueryValueEx(app_subkey, "InstallLocation")
            apps.append((display_name, publisher, install_location))
        except OSError:
            pass
        app_subkey.Close()
    key.Close()
    return apps

# Example usage
# apps = get_installed_apps()
# counter = 0
# for app in apps:
#     # if (app[0] != None) and (app[1] != None) and (app[2] != ""):
#         print(counter,":")
#         counter += 1
#         print(app[0], "by", app[1], "installed at", app[2])



# import winreg

# def get_installed_apps():
#     # Open the registry keys for installed applications
#     keys = [winreg.HKEY_LOCAL_MACHINE,
#             winreg.HKEY_CURRENT_USER,
#             winreg.HKEY_USERS]
#     subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
#     # Iterate over the keys and get the number of subkeys (installed applications) for each key
#     num_apps = 0
#     for key in keys:
#         try:
#             key_obj = winreg.OpenKey(key, subkey)
#             num_apps += winreg.QueryInfoKey(key_obj)[0]
#             key_obj.Close()
#         except OSError:
#             pass
#     # Iterate over the subkeys and retrieve the display name, publisher, and installation path for each installed application
#     apps = []
#     for key in keys:
#         try:
#             key_obj = winreg.OpenKey(key, subkey)
#             for i in range(num_apps):
#                 app_key = winreg.EnumKey(key_obj, i)
#                 app_subkey = winreg.OpenKey(key_obj, app_key)
#                 try:
#                     display_name, _ = winreg.QueryValueEx(app_subkey, "DisplayName")
#                     publisher, _ = winreg.QueryValueEx(app_subkey, "Publisher")
#                     install_location, _ = winreg.QueryValueEx(app_subkey, "InstallLocation")
#                     apps.append((display_name, publisher, install_location))
#                 except OSError:
#                     pass
#                 app_subkey.Close()
#             key_obj.Close()
#         except OSError:
#             pass
#     return apps

# # Example usage
# apps = get_installed_apps()
# for app in apps:
#     print(app[0], "by", app[1], "installed at", app[2])