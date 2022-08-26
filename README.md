# About

`pyqt5_fugueicons` is a library for PyQt5 that provides the icons in the collection [Fugue Icons][fugue-website] created by Yusuke Kamiyamane. It uses the Qt Resource System to embed icons into the library, which allows them to be used directly in an
application.

# Installation

```sh
> pip install pyqt5-fugueicons
```

# Usage

## Icons

```py
import pyqt5_fugueicons as fugue
from PyQt5 import QtWidgets

icon   = fugue.icon('application-blue')
button = QtWidgets.PushButton(icon, 'application-blue')
...
```

The above call returns the icon named "application-blue" with the dimensions 16x16. The icon can then be assigned to any `QtWidgets` class that supports a `QIcon`.

## Shadowed and Shadowless

There are two versions of icons, shadowed and shadowless. Shadowed icons have a small
shadow, which shadowless ones don't. By default, `icon()` returns the shadowed
version of an icon. This can be changed by passing the parameter `shadowless=True`:

```py
import pyqt5_fugueicons as fugue

icon = fugue.icon('application-blue', shadowless=True)
```

## Size and Fallback

Some icons also have 24x24 and 32x32 counterparts. The parameter `size` allows
one to specify the desired size of an icon, and the parameter `fallback_size`
defines whether the smaller counterparts of an icon should be tried if an icon
with the desired size is not found:

```py
import pyqt5_fugueicons as fugue

icon = fugue.icon('application-blue', size=24, fallback_size=True)
```

In the above code, if the shadowed version of the icon "application-blue" is
not found with dimensions 24x24, the function will try to find the shadowed version
of the same icon with dimensions 16x16. If still no icon is found, an empty
`QIcon` is returned. `size` accepts the values 16, 24, and 32.

## Icon Names

Icon names can be found in the author's [website][fugue-website] or in the file under
`resources/FILENAME.txt`. An icon name is simply its file name without the extension.
The function `iconNames()` returns all icon names:

```py
for name in fugue.iconNames():
    print(name)
```

## Animated Icons

Animated icons in the Fugue collection are returned by the function `movie()`:

```py
import pyqt5_fugueicons as fugue
from PyQt5 import QtWidgets

movie = fugue.movie('terminal')
movie.start()

label = QtWidgets.QLabel()
label.setMovie(movie)
...
```

The reason the library calls it "movie" rather than "animation" is to be
consistent with Qt terminology, since Qt animations are [something else][pyqt-animation-framework]. The class `QMovie` is the one responsible for
showing gifs on the Qt framework, so the library follows that.

`movie()` works similar to `icon()`, with the difference being that there exist
only Fugue animations with the dimensions 16x16 and 24x24, so `size` only accepts the
values 16 and 24. There is also a function `movieNames()` which returns all movie names.

## Examples

More elaborated examples of usage can be found in the folder `samples` of this repository.

# Compiling Resources

Since the icon files are already compiled into `resource.py`, this
repository does not include the icon files from the Fugue's website.
If you want to compile it by yourself, you must [download it][fugue-download],
extract it into the folder `resources`, and run `pyrcc5`:

```sh
pyrcc5 -o pyqt5_fugueicons/resources.py resources/resources.qrc
```

Or `rcc.exe`:

```sh
rcc.exe -g python pyqt5_fugueicons/resources.py resources/resources.qrc
```

In the latter case, `resources.py` has to be manually opened and the line
`from PySide2 import QtCore` must be replaced with `from PyQt5 import QtCore`.


  [fugue-website]: <https://p.yusukekamiyamane.com>
  [pyqt-animation-framework]: <https://doc.qt.io/qtforpython-5/overviews/animation-overview.html>
  [fugue-download]: <https://p.yusukekamiyamane.com/icons/downloads/fugue-icons-3.5.6.zip>