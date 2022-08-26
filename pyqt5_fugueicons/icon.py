import functools
import os
import typing
from PyQt5 import QtCore, QtGui

@functools.lru_cache
def _iconNames() -> typing.List[str]:
    file      = QtCore.QFile(':/fugue/filenames.txt')
    open_mode = QtCore.QIODevice.OpenModeFlag.ReadOnly | QtCore.QIODevice.OpenModeFlag.Text

    if not file.open(open_mode):
        QtCore.qWarning(f"pyqt5_fugueicons: missing resource file '{file.fileName()}'")
        return []

    stream    = QtCore.QTextStream(file)
    icon_names = []

    while not stream.atEnd():
        line_data = bytes(QtCore.QByteArray(file.readLine()))
        file_name = line_data.decode()
        icon_name = os.path.splitext(file_name)[0]
        icon_names.append(icon_name)

    file.close()

    return sorted(icon_names)

def iconNames() -> typing.List[str]:
    """Returns all icon names sorted alphabetically."""

    return _iconNames().copy()

def icon(name: str, shadowless: bool = False, size: int = 16, fallback_size: bool = False) -> QtGui.QIcon:
    """Returns a `QIcon` matching the parameters.
    
    If `name` is not a valid icon name or if `size` is
    neither 16, 24, or 32, returns an empty `QIcon`.

    Otherwise, tries to load a resource identified by `name`,
    taking into account `shadowless` and `size`. If a resource
    is loaded, a `QIcon` object containing that resource is returned.
    
    However, if loading of a resource fails and `fallback_size`
    is `True`, tries to load a resource with the same `name` and
    `shadowless`, but with a size smaller than `size`, provided
    that it is not less than 16. If such a resource is found, a
    `QIcon` object containing that resource is returned.

    Either way, returns an empty `QIcon` is no resource was found.
    """

    if name not in iconNames():
        QtCore.qWarning(f"pyqt5_fugueicons: '{name}' does not name a Fugue icon")
        return QtGui.QIcon()
        
    if size not in (16, 24, 32):
        QtCore.qWarning(f'pyqt5_fugueicons: icon size must be either 16, 24, or 32 (got: {size})')
        return QtGui.QIcon()

    file_path = ':/fugue/icons'
    
    if shadowless:
        file_path += '/shadowless'
    else:
        file_path += '/shadowed'
    
    while True:
        icon = QtGui.QIcon(file_path + f'/{size}/{name}.png')

        if not icon.pixmap(size).isNull():
            return icon

        shadow_desc = 'shadowless' if shadowless else 'shadowed'

        if size > 16 and fallback_size:
            new_size = size - 8

            QtCore.qWarning(f"pyqt5_fugueicons: '{name}' ({shadow_desc}) was not found with size {size}, trying {new_size}")
            size = new_size
        else:
            QtCore.qWarning(f"pyqt5_fugueicons: '{name}' ({shadow_desc}) was not found with size {size}")
            return QtGui.QIcon()