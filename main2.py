from widgets import Botao, Input
import pyglet

class MinhaJanela(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height,
            caption="MinhaJanela")

        self.input_nome = Input(100, 400, 300, 70, "Seu nome")
        self.btn_ajuda = Botao(100, 200, 200, 70, "Ajuda")
        self.btn_sair = Botao(100, 100, 200, 70, "Sair")
        self.widgets = [self.btn_ajuda, self.btn_sair, self.input_nome]

    def on_draw(self):
        self.clear()
        for widget in self.widgets:
            widget.draw()
    
    def on_text(self, text):
        for widget in self.widgets:
            widget.digita(text)
        
    def on_key_press(self, symbol, modifiers):
        for widget in self.widgets:
            if symbol == pyglet.window.key.BACKSPACE:
                widget.digita("BACKSPACE")

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            widget.clica(x, y)

window = MinhaJanela(800, 600)

pyglet.app.run()
