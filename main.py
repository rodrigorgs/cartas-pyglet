import pyglet
from carta import Baralho, Carta, Naipe

class MainWindow(pyglet.window.Window):
  def __init__(self):
    super().__init__(960, 540, resizable=False)
    self.baralho = Baralho()
    self.carta = self.baralho.cartas[1]
    self.seta_direita_pressionada = False

  def on_draw(self):
    self.clear()
    self.carta.draw()
    if self.seta_direita_pressionada:
        self.carta.x += 5
    
  def on_key_press(self, symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()
    if symbol == pyglet.window.key.RIGHT:
        self.seta_direita_pressionada = True

  def on_key_release(self, symbol, modifiers):
    if symbol == pyglet.window.key.RIGHT:
        self.seta_direita_pressionada = False

  def on_mouse_press(self, x, y, button, modifiers):
    if self.carta.inclui_ponto(x, y):
        print('Clicou na carta')
    else:
        print('Clicou fora da carta')

if __name__ == '__main__':
    window = MainWindow()
    pyglet.app.run()
