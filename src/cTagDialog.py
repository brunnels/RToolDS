# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.1 on Mon Nov 12 10:50:39 2007

import wx

import Config
from ROMS import MyROMS

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class cTagDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: cTagDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.TagDialog_Label = wx.StaticText(self, -1, _("Enter Tag : "))
        self.Tag_Combo = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN)
        self.OK_Button = wx.Button(self, wx.ID_OK, _("OK"))
        self.Cancel_Button = wx.Button(self, wx.ID_CANCEL, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.On_OK, self.Tag_Combo)
        self.Bind(wx.EVT_BUTTON, self.On_OK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.On_Cancel, id=wx.ID_CANCEL)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: cTagDialog.__set_properties
        self.SetTitle(_("Add Tag to ROMs"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: cTagDialog.__do_layout
        TagDialog_Sizer = wx.FlexGridSizer(2, 1, 0, 0)
        TagDialog_Sizer3 = wx.FlexGridSizer(1, 5, 0, 0)
        TagDialog_Sizer2 = wx.FlexGridSizer(1, 2, 0, 0)
        TagDialog_Sizer2.Add(self.TagDialog_Label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        TagDialog_Sizer2.Add(self.Tag_Combo, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        TagDialog_Sizer2.AddGrowableCol(1)
        TagDialog_Sizer.Add(TagDialog_Sizer2, 1, wx.EXPAND, 0)
        TagDialog_Sizer3.Add((20, 20), 0, 0, 0)
        TagDialog_Sizer3.Add(self.OK_Button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 3)
        TagDialog_Sizer3.Add((50, 20), 0, 0, 0)
        TagDialog_Sizer3.Add(self.Cancel_Button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 3)
        TagDialog_Sizer3.Add((20, 20), 0, 0, 0)
        TagDialog_Sizer3.AddGrowableCol(1)
        TagDialog_Sizer3.AddGrowableCol(3)
        TagDialog_Sizer.Add(TagDialog_Sizer3, 1, wx.EXPAND, 0)
        self.SetSizer(TagDialog_Sizer)
        TagDialog_Sizer.Fit(self)
        TagDialog_Sizer.AddGrowableRow(0)
        TagDialog_Sizer.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade
        
        self.__LocalInit ()
        
    def __LocalInit (self):
        self.Tag_Combo.Clear()
        for Tag in sorted (MyROMS.Get_All_Tags()):
            self.Tag_Combo.Append ( Tag )
        self.Tag_Combo.Append(_("Hidden ROMs"))
        self.Tag_Combo.SetValue (Config.Config ["Last_Tag"])

    def On_OK(self, event): # wxGlade: cTagDialog.<event_handler>
        event.Skip()

    def On_Cancel(self, event): # wxGlade: cTagDialog.<event_handler>
        event.Skip()

# end of class cTagDialog


