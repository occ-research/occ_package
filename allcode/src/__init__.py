import importlib.metadata as ilm

msg = ilm.metadata("occlab")

__name__ = msg["Name"]
__version__ = msg["Version"]
__license__ = msg["License"]
__email__ = msg["Maintainer-email"]
__description__ = msg["Summary"]
__requires__ = msg["Requires-Dist"]
__requires_python__ = msg["Requires-Python"]

import spmap
import wocemaps


from spmap import south_pole_map