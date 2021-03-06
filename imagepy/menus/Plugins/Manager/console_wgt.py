# -*- coding: utf-8 -*-
import wx
from wx.py.shell import Shell
import scipy.ndimage as ndimg
import numpy as np
# from imagepy import IPy

from imagepy.core.engine import Free
from sciapp import Source

cmds = {'app':'app', 'np':np, 'ndimg':ndimg, 'update':None, 'get_img':None}

class Macros(dict):
    def __init__(self):
        for i in Source.manager('plugin').names():
            if not isinstance(i, str) or i == 'Command Line':
                #print(PluginsManager.plgs[i])
                continue
            name = ''.join(list(filter(str.isalnum, i)))
            exec("self.run_%s = lambda para=None, plg=Source.manager('plugin').get(i):plg().start(cmds['app'], para)"%name)

class Plugin(wx.Panel):
    title = 'Command Line'
    single = None
    def __init__(self, parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, 
                                pos = wx.DefaultPosition, size = wx.Size( 500,300 ), 
                                style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        cmds['app'] = parent
        cmds['get_img'] = lambda name=None, app=self: self.app.get_img()
        cmds['update'] = lambda app=self: self.app.get_img().update()
        shell = Shell(self, locals=cmds)
        bSizer = wx.BoxSizer( wx.VERTICAL )
        bSizer.Add( shell, 1, wx.EXPAND|wx.ALL, 5 )
        self.SetSizer(bSizer)
        cmds['plgs'] = Macros()
        shell.run('# plgs.run_name() to call a ImagePy plugin.\n')
        shell.run('# app is avalible here, and get_img() to get the current ImagePlus, update() to redraw.\n')