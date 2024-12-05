import ctypes
from ctypes import wintypes

# 定义结构和常量
class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", ctypes.c_wchar * 32),
        ("dmSpecVersion", ctypes.c_ushort),
        ("dmDriverVersion", ctypes.c_ushort),
        ("dmSize", ctypes.c_ushort),
        ("dmDriverExtra", ctypes.c_ushort),
        ("dmFields", ctypes.c_ulong),
        ("dmPositionX", ctypes.c_long),
        ("dmPositionY", ctypes.c_long),
        ("dmDisplayOrientation", ctypes.c_ulong),
        ("dmDisplayFixedOutput", ctypes.c_ulong),
        ("dmColor", ctypes.c_ushort),
        ("dmDuplex", ctypes.c_ushort),
        ("dmYResolution", ctypes.c_ushort),
        ("dmTTOption", ctypes.c_ushort),
        ("dmCollate", ctypes.c_ushort),
        ("dmFormName", ctypes.c_wchar * 32),
        ("dmLogPixels", ctypes.c_ushort),
        ("dmBitsPerPel", ctypes.c_ulong),
        ("dmPelsWidth", ctypes.c_ulong),
        ("dmPelsHeight", ctypes.c_ulong),
        ("dmDisplayFlags", ctypes.c_ulong),
        ("dmDisplayFrequency", ctypes.c_ulong),
        ("dmICMMethod", ctypes.c_ulong),
        ("dmICMIntent", ctypes.c_ulong),
        ("dmMediaType", ctypes.c_ulong),
        ("dmDitherType", ctypes.c_ulong),
        ("dmReserved1", ctypes.c_ulong),
        ("dmReserved2", ctypes.c_ulong),
        ("dmPanningWidth", ctypes.c_ulong),
        ("dmPanningHeight", ctypes.c_ulong),
    ]

ENUM_CURRENT_SETTINGS = -1
CDS_UPDATEREGISTRY = 0x01
DISP_CHANGE_SUCCESSFUL = 0

user32 = ctypes.WinDLL("user32")
ChangeDisplaySettings = user32.ChangeDisplaySettingsW

def set_resolution(width, height):
    dm = DEVMODE()
    dm.dmSize = ctypes.sizeof(DEVMODE)
    dm.dmPelsWidth = width
    dm.dmPelsHeight = height
    dm.dmFields = 0x180000

    result = ChangeDisplaySettings(ctypes.byref(dm), CDS_UPDATEREGISTRY)
    if result == DISP_CHANGE_SUCCESSFUL:
        print(f"Resolution changed to {width}x{height}")
    else:
        print("Failed to change resolution")

# 检查当前分辨率并切换
def main():
    current_dm = DEVMODE()
    user32.EnumDisplaySettingsW(None, ENUM_CURRENT_SETTINGS, ctypes.byref(current_dm))
    current_width = current_dm.dmPelsWidth
    current_height = current_dm.dmPelsHeight

    if current_width == 1920 and current_height == 1080:
        set_resolution(1290, 886)
    else:
        set_resolution(1920, 1080)

if __name__ == "__main__":
    main()
