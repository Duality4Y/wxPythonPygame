
"""
	the docs are so verry verry handy when trying to decode this code :P
	http://www.wxpython.org/docs/api/wx.Window-class.html
"""

import os
import sys
import wx
import pygame

class wxSDLWindow(wx.Frame):
	def __init__(self, parent, id, title='SDL window', **options):
		options['style'] = wx.DEFAULT_FRAME_STYLE|wx.TRANSPARENT_WINDOW
		wx.Frame.__init__(self, parent, id, title, **options)
		
		self._initialized = 0
		self._resized = 0
		self._surface = None
		self.__needsDrawing = 1
		self.SurfaceSize = None
		
		wx.EVT_IDLE(self, self.OnIdle)
	def OnIdle(self, event):
		#if the system is not initialized or resized
		#check if not initialized then get a handle
		#a window ID on linux, and set the sdl window to that ID
		if not self._initialized or self._resized:
			if not self._initialized:
				#get the handle:
				hwnd = self.GetHandle()
				
				os.environ['SDL_WINDOWID'] = str(hwnd)
				if sys.platform == 'win32':
					os.environ['SDL_VIDEODRIVER'] = 'windib'
				
				#init pygame.
				pygame.init()
				
				wx.EVT_SIZE(self, self.OnSize)
				self._initialized = 1
		else:
			self._resized = 0
		
		#get the size of the window
		self.SurfaceSize = self.GetSizeTuple()
		#create an internal representation of a Pygame Surface.
		self._surface = pygame.display.set_mode(self.SurfaceSize)
		
		if self.__needsDrawing:
			self.draw()
	#a drawing function that call for action to draw
	def OnPaint(self, ev):
		self.__needsDrawing = 1
	#a sizing function that calls for action to resize
	def OnSize(self, ev):
		self._resized = 1
		ev.Skip()
	#the main drawing function
	def draw(self):
		raise NotImplementedError('please define a .draw() method!')
	#the main UI creating function
	def InitUI(self):
		raise NotImplementedError('please define a .InitUI method!')
	#a function that returns the surface to draw upon
	def getSurface(self):
		return self._surface
