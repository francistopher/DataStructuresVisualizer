import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Intro(Gtk.Label):
    
    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_markup('<span color="red">Designed By Christopher Francisco</span>\n')

