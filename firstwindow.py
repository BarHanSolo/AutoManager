import pygame
import thorpy

#Declaration of the application in which the menu is going to live.
application = thorpy.Application(size=(1000, 500), caption='ThorPy stupid Example')

#Setting the graphical theme. By default, it is 'classic' (windows98-like).
thorpy.theme.set_theme('human')

#Declaration of some elements...
useless1 = thorpy.Element.make("This button is useless.\nAnd you can't click it.")

text = "This button also is useless.\nBut you can click it anyway."
useless2 = thorpy.Clickable.make(text)

draggable = thorpy.Draggable.make("Drag me!")

box1 = thorpy.make_ok_box([useless1, useless2, draggable])
options1 = thorpy.make_button("Some useless things...")
thorpy.set_launcher(options1, box1)

text11 = "Jakis guzior"
text12 = "jakis drugi guzior"
mybut1 = thorpy.Clickable.make(text11)
mybut2 = thorpy.Clickable.make(text12)
box3 = thorpy.make_ok_box([mybut1, mybut2])
box3.set_size(500)
options11 = thorpy.make_button("jakies opcje")
thorpy.set_launcher(options11, box3)

inserter = thorpy.Inserter.make(name="Tip text: ",
                                value="This is a default text.",
                                size=(150, 20))

file_browser = thorpy.Browser.make(path="C:/Users/", text="Please have a look.")

browser_launcher = thorpy.BrowserLauncher.make(browser=file_browser,
                                                const_text="Choose a file: ",
                                                var_text="")

color_setter = thorpy.ColorSetter.make()
color_launcher = thorpy.ColorSetterLauncher.make(color_setter,
                                                    "Launch color setter")

options2 = thorpy.make_button("Useful things")
box2 = thorpy.make_ok_box([inserter, color_launcher, browser_launcher])
thorpy.set_launcher(options2, box2)

quit_button = thorpy.make_button("Quit")
quit_button.set_as_exiter()

central_box = thorpy.Box.make([options1, options2, options11, quit_button])
central_box.set_main_color((200, 200, 200, 120))
central_box.center()

#Declaration of a background element - include your own path!
background = thorpy.Background.make(image=thorpy.style.EXAMPLE_IMG,
                                    elements=[central_box])

menu = thorpy.Menu(elements=background, fps=45)
menu.play()

application.quit()
