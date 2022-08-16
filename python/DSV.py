import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class DSV(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        def setBackground():
            screen = Gdk.Screen.get_default()
            provider = Gtk.CssProvider()
            style_context = Gtk.StyleContext()
            style_context.add_provider_for_screen(
                screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )

            css = ""
            with open('main.css', 'r') as file:
                css = file.read()
                css = bytes(css, 'utf-8')
            
            provider.load_from_data(css)

            self.entry = Gtk.Entry()
            self.entry.set_name("myentry")
            self.add(self.entry)

        setBackground()
        self.fullscreen()
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()

if __name__ == '__main__':
    dsv = DSV()
