# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class SpotifyLyrics
###########################################################################

class SpotifyLyrics ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.TopPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.TopPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel3 = wx.Panel( self.TopPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer51.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_textCtrl8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button6 = wx.Button( self.m_panel3, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_button6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer51 )
        self.m_panel3.Layout()
        bSizer51.Fit( self.m_panel3 )
        bSizer4.Add( self.m_panel3, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.progress = wx.StaticText( self.TopPanel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.progress.Wrap( -1 )

        bSizer15.Add( self.progress, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider = wx.Slider( self.TopPanel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        self.slider.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )

        bSizer15.Add( self.slider, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

        self.duration = wx.StaticText( self.TopPanel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.duration.Wrap( -1 )

        bSizer15.Add( self.duration, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )


        bSizer4.Add( bSizer15, 1, wx.EXPAND, 5 )


        self.TopPanel.SetSizer( bSizer4 )
        self.TopPanel.Layout()
        bSizer4.Fit( self.TopPanel )
        bSizer2.Add( self.TopPanel, 0, wx.ALL|wx.EXPAND, 5 )

        self.LyricsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.LyricsPanel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.lyricText = wx.richtext.RichTextCtrl( self.LyricsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer14.Add( self.lyricText, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


        self.LyricsPanel.SetSizer( bSizer14 )
        self.LyricsPanel.Layout()
        bSizer14.Fit( self.LyricsPanel )
        bSizer2.Add( self.LyricsPanel, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass






    def updateText(self, string):
        self.lyricText.SetValue(string)

    def updateTime(self, ps, pm, ds, dm, p):
        progress = str(pm) + ":" + str(ps)
        duration = str(dm) + ":" + str(ds)
        self.progress.SetLabel(progress)
        self.duration.SetLabel(duration)
        self.slider.SetValue(p)
