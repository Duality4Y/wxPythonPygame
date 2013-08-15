
"""
	the docs are so verry verry handy when trying to decode this code :P
	http://www.wxpython.org/docs/api/wx.Window-class.html
"""
import wx
from wxSDLWindow import wxSDLWindow
import pygame

#class for drawing a circle in a wxPythonPygame window

class CircleWindow(wxSDLWindow):
	#define a drawing function
	def draw(self):
		surface = self.getSurface()
		if surface is not None:
			topcolor = 5
			bottomcolor = 100
			
			pygame.draw.circle(surface, (250, 0, 0), (100, 100), 50)
			
			pygame.display.flip()

def main():
	app = wx.PySimpleApp()
	screen_size = (640, 480)
	window = CircleWindow(None, -1, size=screen_size)
	window.Show(1)
	app.MainLoop()

if __name__ == "__main__":
	main()
