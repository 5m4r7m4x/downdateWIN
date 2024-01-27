import winreg

from utils.registry import set_reg_value

WINLOGON_NOTIFICATIONS_COMPONENTS_REGISTRY_PATH = "SYSTEM\\CurrentControlSet\\Control\\Winlogon\\Notifications\\Components"


def set_winlogon_notification_event(component: str, event: str) -> None:
    winlogon_component_registry_path = f"{WINLOGON_NOTIFICATIONS_COMPONENTS_REGISTRY_PATH}\\{component}"
    set_reg_value(winreg.HKEY_LOCAL_MACHINE, winlogon_component_registry_path, "Events", event, winreg.REG_SZ)
