# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.1 on Fri Nov 09 08:21:46 2007

import wx

import GFX
import Config
import Utils

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class cNFODialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        self.Current_Ctrl = kwds["Current_Ctrl"]
        del kwds["Current_Ctrl"]
        # begin wxGlade: cNFODialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.NFODialog_Panel = wx.Panel(self, -1)
        self.Zoom_In_Button = wx.BitmapButton(self.NFODialog_Panel, -1, (GFX.catalog ["GFX_Zoom_In16"].getBitmap()))
        self.Zoom_Out_Button = wx.BitmapButton(self.NFODialog_Panel, -1, (GFX.catalog ["GFX_Zoom_Out16"].getBitmap()))
        self.Font_Button = wx.BitmapButton(self.NFODialog_Panel, -1, (GFX.catalog ["GFX_Icon_Options16"].getBitmap()))
        self.Zoom_Size_Text = wx.StaticText(self.NFODialog_Panel, -1, _("Size"))
        self.NFO_Text = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.TE_RICH2)
        self.OK_Button = wx.Button(self, wx.ID_OK, _("OK"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.On_Zoom_In, self.Zoom_In_Button)
        self.Bind(wx.EVT_BUTTON, self.OnZoomOut, self.Zoom_Out_Button)
        self.Bind(wx.EVT_BUTTON, self.OnFontChange, self.Font_Button)
        self.Bind(wx.EVT_BUTTON, self.On_OK, id=wx.ID_OK)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: cNFODialog.__set_properties
        self.SetTitle(_("NFO File Viewer"))
        self.SetSize((500, 400))
        self.Zoom_In_Button.SetSize(self.Zoom_In_Button.GetBestSize())
        self.Zoom_Out_Button.SetSize(self.Zoom_Out_Button.GetBestSize())
        self.Font_Button.SetSize(self.Font_Button.GetBestSize())
        self.NFO_Text.SetFocus()
        # end wxGlade
        ToolSize = Config.Config ["Toolbar_Size"]
        self.Zoom_In_Button.SetBitmapLabel (eval ( "GFX.getGFX_Zoom_In"+ToolSize+"Bitmap" )())
        self.Zoom_Out_Button.SetBitmapLabel(eval ( "GFX.getGFX_Zoom_Out"+ToolSize+"Bitmap" )())
        self.Font_Button.SetBitmapLabel(eval ( "GFX.getGFX_Icon_Options"+ToolSize+"Bitmap" )())

    def __do_layout(self):
#        self.Freeze()
        # begin wxGlade: cNFODialog.__do_layout
        NFODialog_Sizer = wx.FlexGridSizer(3, 1, 0, 0)
        Panel_Sizer = wx.FlexGridSizer(1, 4, 0, 0)
        Panel_Sizer.Add(self.Zoom_In_Button, 0, wx.TOP|wx.BOTTOM, 3)
        Panel_Sizer.Add(self.Zoom_Out_Button, 0, wx.TOP|wx.BOTTOM, 3)
        Panel_Sizer.Add(self.Font_Button, 0, wx.TOP|wx.BOTTOM, 3)
        Panel_Sizer.Add(self.Zoom_Size_Text, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        self.NFODialog_Panel.SetSizer(Panel_Sizer)
        Panel_Sizer.AddGrowableCol(3)
        NFODialog_Sizer.Add(self.NFODialog_Panel, 1, wx.EXPAND, 0)
        NFODialog_Sizer.Add(self.NFO_Text, 0, wx.EXPAND, 0)
        NFODialog_Sizer.Add(self.OK_Button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.SetSizer(NFODialog_Sizer)
        NFODialog_Sizer.AddGrowableRow(1)
        NFODialog_Sizer.AddGrowableCol(0)
        self.Layout()
        # end wxGlade

        self.__LocalInit ()

#        self.Thaw()
        
    def __LocalInit ( self ):
        try:
            self.ROM = self.Current_Ctrl.Get_ROM ( self.Current_Ctrl.GetFocusedItem() )
        except:
            self.Close()
            
        self.Orig_Encoding = wx.GetDefaultPyEncoding()
        wx.SetDefaultPyEncoding( "cp437" )

        self.SetSize( Config.Config ["NFO_Size"] )
        
        if Config.Config ["NFO_Position"] [ 0 ] == -1:
            self.CentreOnScreen ()
        else:
            self.SetPosition( Config.Config ["NFO_Position"] )
            
        self.Bind( wx.EVT_SIZE, self.On_Window_Size )
        self.Bind( wx.EVT_MOVE, self.On_Window_Move )
        
#        font = wx.Font( Config.Config ["NFO_Zoom"], wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, "Lucida Console", wx.FONTENCODING_CP437 )
        font = wx.Font( Config.Config ["NFO_Zoom"], Config.Config ["NFO_Family"], Config.Config ["NFO_Style"], Config.Config ["NFO_Weight"], False, Config.Config ["NFO_Face"], wx.FONTENCODING_CP437 )
        self.NFO_Text.SetFont( font )

        Data = Utils.Get_NFO (self.ROM)
        if Data != "":
            self.NFO_Text.AppendText( Data )
        else:
            self.NFO_Text.AppendText( "None Available\n")

        self.NFO_Text.ShowPosition( 0 )
        self.Zoom_Size_Text.SetLabel( " Zoom Size : %d" % Config.Config ["NFO_Zoom"] )

    def On_Window_Size ( self, event ):
        Config.Config ["NFO_Size"] = self.GetSize()
        event.Skip ()
    
    def On_Window_Move ( self, event ):
        Config.Config ["NFO_Position"] = self.GetScreenPosition()
        event.Skip ()

    def On_OK(self, event): # wxGlade: cNFODialog.<event_handler>
        wx.SetDefaultPyEncoding( self.Orig_Encoding )
        event.Skip()

    def On_Zoom_In(self, event): # wxGlade: cNFODialog.<event_handler>
        Config.Config ["NFO_Zoom"] += 1
        if Config.Config ["NFO_Zoom"] > 24:
            Config.Config ["NFO_Zoom"] = 24;
        font = wx.Font( Config.Config ["NFO_Zoom"], Config.Config ["NFO_Family"], Config.Config ["NFO_Style"], Config.Config ["NFO_Weight"], False, Config.Config ["NFO_Face"], wx.FONTENCODING_CP437 )
        self.NFO_Text.SetFont( font )
        self.Zoom_Size_Text.SetLabel( " Zoom Size : %d" % Config.Config ["NFO_Zoom"] )

    def OnZoomOut(self, event): # wxGlade: cNFODialog.<event_handler>
        Config.Config ["NFO_Zoom"] -= 1
        if Config.Config ["NFO_Zoom"] < 6:
            Config.Config ["NFO_Zoom"] = 6;
        font = wx.Font( Config.Config ["NFO_Zoom"], Config.Config ["NFO_Family"], Config.Config ["NFO_Style"], Config.Config ["NFO_Weight"], False, Config.Config ["NFO_Face"], wx.FONTENCODING_CP437 )
        self.NFO_Text.SetFont( font )
        self.Zoom_Size_Text.SetLabel( " Zoom Size : %d" % Config.Config ["NFO_Zoom"] )

    def OnFontChange(self, event): # wxGlade: cNFODialog.<event_handler>
        data = wx.FontData()
        data.EnableEffects(False)
        data.SetInitialFont(wx.Font( Config.Config ["NFO_Zoom"], Config.Config ["NFO_Family"], Config.Config ["NFO_Style"], Config.Config ["NFO_Weight"], False, Config.Config ["NFO_Face"], wx.FONTENCODING_CP437 ))

        dlg = wx.FontDialog(self, data)
        
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
            Config.Config ["NFO_Zoom"] = font.GetPointSize()
            Config.Config ["NFO_Family"] = font.GetFamily()#wx.FONTFAMILY_SWISS
            Config.Config ["NFO_Style"] = font.GetStyle()
            Config.Config ["NFO_Weight"] = font.GetWeight()
            Config.Config ["NFO_Face"] = font.GetFaceName()
            font = wx.Font( Config.Config ["NFO_Zoom"], Config.Config ["NFO_Family"], Config.Config ["NFO_Style"], Config.Config ["NFO_Weight"], False, Config.Config ["NFO_Face"], wx.FONTENCODING_CP437 )
            self.NFO_Text.SetFont( font )
            self.Zoom_Size_Text.SetLabel( " Zoom Size : %d" % Config.Config ["NFO_Zoom"] )

# end of class cNFODialog