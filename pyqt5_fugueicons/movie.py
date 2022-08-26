import functools
import typing
from PyQt5 import QtGui

@functools.lru_cache
def _movieNames() -> typing.List[str]:
    return sorted([
        'application-terminal',
        'construction',
        'counter-count-up',
        'counter-count',
        'counter',
        'lock-warning',
        'selection-input',
        'selection-select-input',
        'selection-select',
        'selection',
        'terminal-medium',
        'terminal-network',
        'terminal',
        'ui-progress-bar-indeterminate'
    ])

def movieNames() -> typing.List[str]:
    """Returns all movie names sorted alphabetically.
    
    Note that all movie names are also icon names,
    but since very few icons have movies counterparts,
    this function provides a separate list.
    """

    return _movieNames().copy()

def movie(name: str, shadowless: bool = False, size: int = 16, fallback_size: bool = False) -> QtGui.QMovie:
    """Returns a `QMovie` matching the parameters.
    
    If `name` is not a valid movie name or if `size` is
    neither 16 or 24, returns an empty `QMovie`.

    Otherwise, tries to load a resouce identified by `name`,
    taking into account `shadowless` and `size`. If a resource
    is loaded, a `QMovie` object containing that resource is returned.
    
    However, if loading of a resource fails and `fallback_size`
    is `True`, tries to load a resource with the same `name` and
    `shadowless`, but with a size smaller than `size`, provided
    that it is not less than 16. If such a resource is found, a
    `QMovie` object containing that resource is returned.

    Either way, returns an empty `QMovie` is no resource was found.
    """

    if name not in movieNames():
        print("pyqt5_fugueicons: '", name, "' does not name a Fugue animated icon", sep='')
        return QtGui.QMovie()

    if size not in (16, 24):
        print('pyqt5_fugueicons: animated icon size must be either 16 or 24')
        return QtGui.QMovie()
    
    file_path = ':/fugue/movies'
    
    if shadowless:
        file_path += '/shadowless'
    else:
        file_path += '/shadowed'
    
    while True:
        movie = QtGui.QMovie(file_path + f'/{size}/{name}.gif')

        if movie.isValid():
            return movie

        shadow_desc = '(shadowless)' if shadowless else ''

        if size > 16 and fallback_size:
            new_size = size - 8

            print("pyqt5_fugueicons: '", name, "' ", shadow_desc, " was not found at size ", size, ", trying ", new_size, sep='')
            size = new_size
        else:
            print("pyqt5_fugueicons: '", name, "' ", shadow_desc, " was not found at size ", size, sep='')
            return QtGui.QMovie()