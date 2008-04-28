# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.1 on Mon Nov 12 11:21:36 2007

import sys
import wx
import wx.lib.filebrowsebutton as filebrowse
import copy
import os

from ColumnListCtrlMixin import ColumnListCtrlMixin
import Config
#from ROMS import MyROMS
import Utils

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class cOptions( wx.Dialog ):
    def __init__( self, *args, **kwds ):
        try:
            self.GoToSaves = kwds["GoToSaves"]
            del kwds["GoToSaves"]
        except:
            self.GoToSaves = False
        # begin wxGlade: cOptions.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.Notebook = wx.Notebook(self, -1, style=0)
        self.Notebook_pane_6 = wx.Panel(self.Notebook, -1)
        self.Notebook_pane_5 = wx.Panel(self.Notebook, -1)
        self.NotebookPanel4 = wx.Panel(self.Notebook, -1)
        self.NotebookPanel3 = wx.Panel(self.Notebook, -1)
        self.NotebookPanel2 = wx.Panel(self.Notebook, -1)
        self.NotebookPanel1 = wx.Panel(self.Notebook, -1)
        self.sizer_4_staticbox = wx.StaticBox(self.NotebookPanel1, -1, _(" Device Directories "))
        self.sizer_3_staticbox = wx.StaticBox(self.NotebookPanel1, -1, _(" ROM Directories "))
        self.ROM_Path = filebrowse.DirBrowseButton(self.NotebookPanel1, -1, changeCallback = self.dbbCallback, startDirectory = Config.Config ["ROM_Path"], dialogTitle = _("Select ROMs Directory") + " : ", newDirectory = True)
        self.Image_Path = filebrowse.DirBrowseButton(self.NotebookPanel1, -1, changeCallback = self.dbbCallback, startDirectory = Config.Config ["Image_Path"], dialogTitle = _("Select Images Directory") + " : ", newDirectory = True)
        self.NFO_Path = filebrowse.DirBrowseButton(self.NotebookPanel1, -1, changeCallback = self.dbbCallback, startDirectory = Config.Config ["NFO_Path"], dialogTitle = _("Select NFO Directory") + " : ", newDirectory = True)
        self.Save_Path = filebrowse.DirBrowseButton(self.NotebookPanel1, -1, changeCallback = self.dbbCallback, startDirectory = Config.Config ["Save_Path"], dialogTitle = _("Select Save Game Database Directory") + " : ", newDirectory = True)
        self.Device_Path = filebrowse.DirBrowseButton(self.NotebookPanel1, -1, changeCallback = self.dbbCallback, startDirectory = Config.Config ["Device_Path"], dialogTitle = _("Select Device Directory") + " : ", newDirectory = True)
        self.Save_Dir_On_Cart = filebrowse.DirBrowseButton(self.NotebookPanel1, -1, changeCallback = self.dbbCallback, startDirectory = Config.Config ["Device_Path"], dialogTitle = _("Select Save Game Directory") + " : ", newDirectory = True)
        self.Show_Splash = wx.CheckBox(self.NotebookPanel2, -1, _("Show Splash Screen on Start-up"))
        self.Use_Trimmed = wx.CheckBox(self.NotebookPanel2, -1, _("Enable ROM Trimming"))
        self.label_1_copy = wx.StaticText(self.NotebookPanel2, -1, _("Safe Trim Bytes to Keep : "))
        self.Safe_Trim = wx.SpinCtrl(self.NotebookPanel2, -1, "0", min=0, max=65534)
        self.RealTime_Search = wx.CheckBox(self.NotebookPanel2, -1, _("Enable Real-Time Search"))
        self.Filter_Use_Exact_Sizes = wx.CheckBox(self.NotebookPanel2, -1, _("Add Exact ROM Sizes to Filter"))
        self.Parse_Subdirs = wx.CheckBox(self.NotebookPanel2, -1, _("Parse Sub-Directories in ROM Directory"))
        self.Swap_SS_and_Case = wx.CheckBox(self.NotebookPanel2, -1, _("Swap Screenshot and Case Images"))
        self.Find_Unknown = wx.CheckBox(self.NotebookPanel2, -1, _("Enable Unknown/Homebrew ROM File Detection"))
        self.Confirm_Delete = wx.CheckBox(self.NotebookPanel2, -1, _("Confirm Deletes on Device"))
        self.AutoCloseUpdate = wx.CheckBox(self.NotebookPanel2, -1, _("Automatically Close Update Window"))
        self.label_6_copy = wx.StaticText(self.NotebookPanel2, -1, _("Utilise Selected for the ROM List Search Method : "))
        self.Search_Method = wx.Choice(self.NotebookPanel2, -1, choices=[_("ROM Title"), _("ROM Filename"), _("Archive Filename")])
        self.label_6 = wx.StaticText(self.NotebookPanel2, -1, _("Utilise Selected for Unknown/Homebrew ROM Titles : "))
        self.Unknown_Name = wx.Choice(self.NotebookPanel2, -1, choices=[_("Archive Filename"), _("ROM Filename")])
        self.label_8 = wx.StaticText(self.NotebookPanel2, -1, _("Colour to use for Alternating Lines in ROM List : "))
        self.Alternate_Colour = wx.Button(self.NotebookPanel2, -1, "")
        self.label_8_copy = wx.StaticText(self.NotebookPanel2, -1, _("Colour to use for ROMs Waiting to be Applied : "))
        self.Pending_Colour = wx.Button(self.NotebookPanel2, -1, "")
        self.Search_Device_Subdirs = wx.CheckBox(self.NotebookPanel2, -1, _("Auto Scan Sub-Directories on Device to Find ROMs"))
        self.label_9 = wx.StaticText(self.NotebookPanel2, -1, _("Subdirectories to Scan First : "))
        self.Device_Dirs_to_Search = wx.TextCtrl(self.NotebookPanel2, -1, "")
        self.label_1_copy_1 = wx.StaticText(self.NotebookPanel3, -1, _("Number of Save Games to Keep : "))
        self.Save_Games_to_Keep = wx.SpinCtrl(self.NotebookPanel3, -1, "0", min=1, max=99)
        self.Auto_Backup_Saved_Games = wx.CheckBox(self.NotebookPanel3, -1, _("Automatically Backup Recent Save Games from Device"))
        self.AutoCopySaves = wx.CheckBox(self.NotebookPanel3, -1, _("Automatically Copy Latest Save Game with ROM to Device"))
        self.Delete_Saves_with_ROM = wx.CheckBox(self.NotebookPanel3, -1, _("When Deleting ROMs from Device, also Delete Corresponding Save Games"))
        self.Use_Original_Save_Time = wx.CheckBox(self.NotebookPanel3, -1, _("Use Original Save Game Date and Time"))
        self.UseShortSaveName = wx.CheckBox(self.NotebookPanel3, -1, _("Enable Short Name Save Files (eg. SuperCard DS ONE)"))
        self.Convert_Imports = wx.CheckBox(self.NotebookPanel3, -1, _("On Save Game Import, Enable Conversion"))
        self.label_10 = wx.StaticText(self.NotebookPanel3, -1, _("Default Linker Device Type :"))
        self.Default_Device = wx.Choice(self.NotebookPanel3, -1, choices=[])
        self.label_12 = wx.StaticText(self.NotebookPanel3, -1, _("Note: Save Games are Automatically Converted to the Selected Default Linker Device Type,"))
        self.label_13 = wx.StaticText(self.NotebookPanel3, -1, _("File Extension, and Size."))
        self.Use_Rename_Popup = wx.CheckBox(self.NotebookPanel4, -1, _("Enable ROM Renamer Popup on Apply"))
        self.Use_Renaming = wx.CheckBox(self.NotebookPanel4, -1, _("Enable Automatic ROM Renaming Mask on Apply"))
        self.Rename_Label1 = wx.StaticText(self.NotebookPanel4, -1, _("Copy to Device Filename Mask :"))
        self.Rename_Mask = wx.TextCtrl(self.NotebookPanel4, -1, "")
        self.Rename_Label2 = wx.StaticText(self.NotebookPanel4, -1, _("(N) : Release Number"))
        self.Rename_Label3 = wx.StaticText(self.NotebookPanel4, -1, _("(T) : Title"))
        self.Rename_Label4 = wx.StaticText(self.NotebookPanel4, -1, _("(R) : Region"))
        self.Rename_Label5 = wx.StaticText(self.NotebookPanel4, -1, _("(G) : Source (Group)"))
        self.Rename_Label6 = wx.StaticText(self.NotebookPanel4, -1, _("(P) : Publisher"))
        self.Rename_Label7 = wx.StaticText(self.NotebookPanel4, -1, _("(S) : Save Type"))
        self.Rename_Label8 = wx.StaticText(self.NotebookPanel4, -1, _("(C) : CRC"))
        self.ROM_Columns = ColumnListCtrlMixin(self.Notebook_pane_5, -1)
        self.ROMColUP = wx.Button(self.Notebook_pane_5, wx.ID_UP, "")
        self.ROMColDown = wx.Button(self.Notebook_pane_5, wx.ID_DOWN, "")
        self.label_11 = wx.StaticText(self.Notebook_pane_5, -1, _("Note: Removing the Icon Column Requires a Restart"))
        self.Device_Columns = ColumnListCtrlMixin(self.Notebook_pane_6, -1)
        self.CartColUP = wx.Button(self.Notebook_pane_6, wx.ID_UP, "")
        self.CartColDown = wx.Button(self.Notebook_pane_6, wx.ID_DOWN, "")
        self.label_11_copy = wx.StaticText(self.Notebook_pane_6, -1, _("Note: Removing the Icon Column Requires a Restart"))
        self.OptionsOK = wx.Button(self, wx.ID_OK, _("OK"))
        self.OptionsCancel = wx.Button(self, wx.ID_CANCEL, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.On_Alternate_Colour, self.Alternate_Colour)
        self.Bind(wx.EVT_BUTTON, self.On_Pending_Colour, self.Pending_Colour)
        self.Bind(wx.EVT_CHOICE, self.On_Device_Type_Change, self.Default_Device)
        self.Bind(wx.EVT_CHECKBOX, self.On_Use_Renaming, self.Use_Renaming)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnColumnsListCtrlItemDeSelected, self.ROM_Columns)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnColumnsListCtrlItemSelected, self.ROM_Columns)
        self.Bind(wx.EVT_BUTTON, self.On_Column_Up, self.ROMColUP)
        self.Bind(wx.EVT_BUTTON, self.On_Column_Down, self.ROMColDown)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnColumnsListCtrlItemDeSelected, self.Device_Columns)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnColumnsListCtrlItemSelected, self.Device_Columns)
        self.Bind(wx.EVT_BUTTON, self.On_Column_Up, self.CartColUP)
        self.Bind(wx.EVT_BUTTON, self.On_Column_Down, self.CartColDown)
        self.Bind(wx.EVT_BUTTON, self.On_OK, id=wx.ID_OK)
        # end wxGlade

    def __set_properties( self ):
        # begin wxGlade: cOptions.__set_properties
        self.SetTitle(_("Options"))
        self.SetSize((545, 484))
        self.Search_Method.SetSelection(0)
        self.Unknown_Name.SetSelection(0)
        self.Alternate_Colour.SetMinSize((60, 20))
        self.Pending_Colour.SetMinSize((60, 20))
        self.Search_Device_Subdirs.Enable(False)
        self.Device_Dirs_to_Search.Enable(False)
        self.Convert_Imports.Hide()
        self.Default_Device.SetMinSize((150, 21))
        self.Notebook.SetMinSize((500, 400))
        # end wxGlade

    def __do_layout( self ):
        # begin wxGlade: cOptions.__do_layout
        Options_Sizer = wx.FlexGridSizer(2, 1, 0, 0)
        OptionsButtonsSizer = wx.FlexGridSizer(1, 5, 0, 0)
        grid_sizer_7 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_12 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_6 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_11 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_11 = wx.FlexGridSizer(10, 1, 0, 0)
        grid_sizer_11_copy_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_4_copy = wx.FlexGridSizer(10, 1, 0, 0)
        grid_sizer_20 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_10_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_4 = wx.FlexGridSizer(20, 1, 0, 0)
        grid_sizer_19 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_18_copy = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_18 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_10 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_10_copy = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_10_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.HORIZONTAL)
        grid_sizer_2 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        sizer_5 = wx.FlexGridSizer(4, 1, 0, 0)
        sizer_7 = wx.FlexGridSizer(4, 2, 0, 0)
        sizer_7.Add((1, 20), 0, 0, 0)
        sizer_7.Add(self.ROM_Path, 1, wx.ALL|wx.EXPAND, 3)
        sizer_7.Add((1, 20), 0, 0, 0)
        sizer_7.Add(self.Image_Path, 1, wx.ALL|wx.EXPAND, 3)
        sizer_7.Add((1, 20), 0, 0, 0)
        sizer_7.Add(self.NFO_Path, 1, wx.ALL|wx.EXPAND, 3)
        sizer_7.Add((1, 20), 0, 0, 0)
        sizer_7.Add(self.Save_Path, 1, wx.ALL|wx.EXPAND, 3)
        sizer_7.AddGrowableCol(1)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_5.AddGrowableCol(0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL|wx.EXPAND, 3)
        grid_sizer_2.Add((1, 20), 0, 0, 0)
        grid_sizer_2.Add(self.Device_Path, 1, wx.ALL|wx.EXPAND, 3)
        grid_sizer_2.Add((1, 20), 0, 0, 0)
        grid_sizer_2.Add(self.Save_Dir_On_Cart, 1, wx.ALL|wx.EXPAND, 3)
        grid_sizer_2.AddGrowableCol(1)
        sizer_4.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.ALL|wx.EXPAND, 3)
        sizer_2.AddGrowableCol(0)
        sizer_1_copy.Add(sizer_2, 1, wx.EXPAND, 0)
        self.NotebookPanel1.SetSizer(sizer_1_copy)
        grid_sizer_4.Add(self.Show_Splash, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.Use_Trimmed, 0, wx.ALL, 3)
        sizer_10_copy.Add(self.label_1_copy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_10_copy.Add(self.Safe_Trim, 0, wx.ALL, 3)
        grid_sizer_4.Add(sizer_10_copy, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.RealTime_Search, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.Filter_Use_Exact_Sizes, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.Parse_Subdirs, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.Swap_SS_and_Case, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.Find_Unknown, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.Confirm_Delete, 0, wx.ALL, 3)
        grid_sizer_4.Add(self.AutoCloseUpdate, 0, wx.ALL, 3)
        grid_sizer_10_copy.Add(self.label_6_copy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_10_copy.Add(self.Search_Method, 0, wx.ALL, 3)
        grid_sizer_4.Add(grid_sizer_10_copy, 1, wx.LEFT|wx.EXPAND, 2)
        grid_sizer_10.Add(self.label_6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_10.Add(self.Unknown_Name, 0, wx.ALL, 3)
        grid_sizer_4.Add(grid_sizer_10, 1, wx.LEFT|wx.EXPAND, 2)
        grid_sizer_18.Add(self.label_8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_18.Add(self.Alternate_Colour, 0, wx.ALL, 3)
        grid_sizer_4.Add(grid_sizer_18, 1, wx.EXPAND, 0)
        grid_sizer_18_copy.Add(self.label_8_copy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_18_copy.Add(self.Pending_Colour, 0, wx.ALL, 3)
        grid_sizer_4.Add(grid_sizer_18_copy, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.Search_Device_Subdirs, 0, wx.ALL, 3)
        grid_sizer_19.Add(self.label_9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_19.Add(self.Device_Dirs_to_Search, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_19.AddGrowableCol(1)
        grid_sizer_4.Add(grid_sizer_19, 1, wx.EXPAND, 0)
        self.NotebookPanel2.SetSizer(grid_sizer_4)
        grid_sizer_4.AddGrowableCol(0)
        sizer_10_copy_1.Add(self.label_1_copy_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_10_copy_1.Add(self.Save_Games_to_Keep, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(sizer_10_copy_1, 1, wx.EXPAND, 0)
        grid_sizer_4_copy.Add(self.Auto_Backup_Saved_Games, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(self.AutoCopySaves, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(self.Delete_Saves_with_ROM, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(self.Use_Original_Save_Time, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(self.UseShortSaveName, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(self.Convert_Imports, 0, wx.ALL, 3)
        grid_sizer_20.Add(self.label_10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_20.Add(self.Default_Device, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(grid_sizer_20, 1, wx.EXPAND, 0)
        grid_sizer_4_copy.Add(self.label_12, 0, wx.ALL, 3)
        grid_sizer_4_copy.Add(self.label_13, 0, wx.LEFT, 3)
        self.NotebookPanel3.SetSizer(grid_sizer_4_copy)
        grid_sizer_4_copy.AddGrowableCol(0)
        grid_sizer_11.Add(self.Use_Rename_Popup, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Use_Renaming, 0, wx.ALL, 3)
        grid_sizer_11_copy_1.Add(self.Rename_Label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_11_copy_1.Add(self.Rename_Mask, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_11_copy_1.AddGrowableCol(1)
        grid_sizer_11.Add(grid_sizer_11_copy_1, 1, wx.EXPAND, 0)
        grid_sizer_11.Add(self.Rename_Label2, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Rename_Label3, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Rename_Label4, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Rename_Label5, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Rename_Label6, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Rename_Label7, 0, wx.ALL, 3)
        grid_sizer_11.Add(self.Rename_Label8, 0, wx.ALL, 3)
        self.NotebookPanel4.SetSizer(grid_sizer_11)
        grid_sizer_11.AddGrowableCol(0)
        grid_sizer_6.Add(self.ROM_Columns, 1, wx.EXPAND, 0)
        sizer_11.Add(self.ROMColUP, 0, wx.ALL, 3)
        sizer_11.Add(self.ROMColDown, 0, wx.ALL|wx.ALIGN_BOTTOM, 3)
        grid_sizer_6.Add(sizer_11, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.label_11, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5)
        self.Notebook_pane_5.SetSizer(grid_sizer_6)
        grid_sizer_6.AddGrowableRow(0)
        grid_sizer_6.AddGrowableCol(0)
        grid_sizer_7.Add(self.Device_Columns, 1, wx.EXPAND, 0)
        sizer_12.Add(self.CartColUP, 0, wx.ALL, 3)
        sizer_12.Add(self.CartColDown, 0, wx.ALL|wx.ALIGN_BOTTOM, 3)
        grid_sizer_7.Add(sizer_12, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.label_11_copy, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5)
        self.Notebook_pane_6.SetSizer(grid_sizer_7)
        grid_sizer_7.AddGrowableRow(0)
        grid_sizer_7.AddGrowableCol(0)
        self.Notebook.AddPage(self.NotebookPanel1, _("Directories"))
        self.Notebook.AddPage(self.NotebookPanel2, _("Misc"))
        self.Notebook.AddPage(self.NotebookPanel3, _("Save Games"))
        self.Notebook.AddPage(self.NotebookPanel4, _("ROM to Device Renaming"))
        self.Notebook.AddPage(self.Notebook_pane_5, _("ROM List Columns"))
        self.Notebook.AddPage(self.Notebook_pane_6, _("Device List Columns"))
        Options_Sizer.Add(self.Notebook, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 3)
        OptionsButtonsSizer.Add((20, 20), 0, wx.EXPAND, 0)
        OptionsButtonsSizer.Add(self.OptionsOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        OptionsButtonsSizer.Add((20, 20), 0, wx.EXPAND, 0)
        OptionsButtonsSizer.Add(self.OptionsCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        OptionsButtonsSizer.Add((20, 20), 0, wx.EXPAND, 0)
        OptionsButtonsSizer.AddGrowableCol(0)
        OptionsButtonsSizer.AddGrowableCol(4)
        Options_Sizer.Add(OptionsButtonsSizer, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 5)
        self.SetSizer(Options_Sizer)
        Options_Sizer.AddGrowableRow(0)
        Options_Sizer.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade
        
        self.__LocalInit ()
        
    def __LocalInit ( self ):
        if sys.platform == "linux2":
            self.Fit()

        self.ColumnsChanged = False

        self.ROM_Path.SetLabel( _( "ROMs :" ) )
        self.ROM_Path.SetValue ( Config.Config ["ROM_Path"] )
        self.Image_Path.SetLabel( _( "Images :" ) )
        self.Image_Path.SetValue ( Config.Config ["Image_Path"] )
        self.NFO_Path.SetLabel( _( "NFO Files :" ) )
        self.NFO_Path.SetValue ( Config.Config ["NFO_Path"] )
        self.Orig_Device_Path = Config.Config ["Device_Path"]
        self.Device_Path.SetLabel( _( "ROMs :" ) )
        self.Device_Path.SetValue ( Config.Config ["Device_Path"] )
        self.Save_Path.SetLabel( _( "Save Games DB :" ) )
        self.Save_Path.SetValue ( Config.Config ["Save_Path"] )

        self.Save_Dir_On_Cart.SetLabel( _("Saves :") )
        self.Save_Dir_On_Cart.SetValue ( Config.Config ["Save_Dir_On_Cart"] )
        
        self.Save_Games_to_Keep.SetValue ( Config.Config ["Save_Games_to_Keep"] )
        self.Show_Splash.SetValue ( Config.Config ["Show_Splash"] )
        self.Use_Trimmed.SetValue ( Config.Config ["Use_Trimmed"] )
        self.RealTime_Search.SetValue ( Config.Config ["RealTime_Search"] )
        self.Parse_Subdirs.SetValue ( Config.Config ["Parse_Subdirs"] )
#        self.DLGfx.SetValue ( Config.Config ["DLGfx"] )
        self.Auto_Backup_Saved_Games.SetValue ( Config.Config ["Auto_Backup_Saved_Games"] )
        self.Swap_SS_and_Case.SetValue ( Config.Config ["Swap_SS_and_Case"] )
        self.Use_Original_Save_Time.SetValue ( Config.Config ["Use_Original_Save_Time"] )
        self.Find_Unknown.SetValue( Config.Config ["Find_Unknown"] )
        self.Safe_Trim.SetValue( Config.Config ["Safe_Trim"] )
        self.Search_Device_Subdirs.SetValue( Config.Config ["Search_Device_Subdirs"] )
#        self.UseCRCFiles.SetValue(Config.Config ["UseCRCFiles"])
        self.AutoCopySaves.SetValue(Config.Config ["AutoCopySaves"])
        self.Filter_Use_Exact_Sizes.SetValue( Config.Config ["Filter_Use_Exact_Sizes"] )
        self.UseShortSaveName.SetValue(Config.Config ["UseShortSaveName"])
        self.Confirm_Delete.SetValue(Config.Config ["Confirm_Delete"])
        self.Delete_Saves_with_ROM.SetValue(Config.Config ["Delete_Saves_with_ROM"])
#        self.SlowLookups.SetValue(Config.Config ["SlowLookups"])
        self.Convert_Imports.SetValue(Config.Config ["Convert_Imports"])
        self.AutoCloseUpdate.SetValue(Config.Config ["AutoCloseUpdate"])
        
        self.Use_Rename_Popup.SetValue(Config.Config ["Use_Rename_Popup"])
        self.Use_Renaming.SetValue(Config.Config ["Use_Renaming"])
        self.Rename_Mask.SetValue(Config.Config ["Rename_Mask"])
        
        self.Alternate_Colour.SetBackgroundColour( Config.Config ["Alternate_Colour"] )
        self.Pending_Colour.SetBackgroundColour(Config.Config ["Pending_Colour"])
        
        Str = ","
        self.Device_Dirs_to_Search.SetValue( Str.join ( Config.Config ["Device_Dirs_to_Search"] ) )

        self.On_Use_Renaming (None)

#        self.Unknown_Name.Append( _( "Archive File Name" ) )
#        self.Unknown_Name.Append( _( "ROM File Name" ) )
        
        if Config.Config ["Unknown_Name"] == "ARCHIVE":
            self.Unknown_Name.SetStringSelection( _( "Archive File Name" ) )
        elif Config.Config ["Unknown_Name"] == "FILENAME":
            self.Unknown_Name.SetStringSelection( _( "ROM File Name" ) )
            
        if Config.Config ["Search_Method"] == 1:
            self.Search_Method.SetStringSelection( _("Filename") )
        elif Config.Config ["Search_Method"] == 0:
            self.Search_Method.SetStringSelection( _("ROM Title") )
        else:
            self.Search_Method.SetStringSelection( _("Archive Filename"))
        
        self.ROM_Columns.InsertColumn ( 0, _( "Column Name" ) )
        self.ROM_Columns.InsertColumn ( 1, _( "Display Name" ) )
        
        index = self.ROM_Columns.InsertStringItem ( sys.maxint, "Icon" )
        self.ROM_Columns.SetStringItem ( index, 1, Config.Config ["ROMColumn_Titles"]["Icon"] )
        if "Icon" in Config.Config ["ROMColumns"]:
            self.ROM_Columns.CheckItem ( index )
            
        for Column in Config.Config ["ROMColumns"]:
            if Column == "Icon":
                continue
            index = self.ROM_Columns.InsertStringItem ( sys.maxint, Column )
            self.ROM_Columns.SetStringItem ( index, 1, Config.Config ["ROMColumn_Titles"][Column] )
            self.ROM_Columns.CheckItem ( index )
        for Column in Config.Config ["Columns"]:
            if Column == "Icon" or Column == "Save Date":
                continue
            if Column not in Config.Config ["ROMColumns"]:
                index = self.ROM_Columns.InsertStringItem ( sys.maxint, Column )
                self.ROM_Columns.SetStringItem ( index, 1, Config.Config ["ROMColumn_Titles"][Column] )  

        self.ROM_Columns.SetColumnWidth( 0, wx.LIST_AUTOSIZE )
        self.ROM_Columns.SetColumnWidth( 1, 200 )
        self.ROM_Columns.Select( 0, True )

        self.Device_Columns.InsertColumn ( 0, _( "Column Name" ) )
        self.Device_Columns.InsertColumn ( 1, _( "Display Name" ) )
        
        index = self.Device_Columns.InsertStringItem ( sys.maxint, "Icon" )
        self.Device_Columns.SetStringItem ( index, 1, Config.Config ["CartColumn_Titles"]["Icon"] )
        if "Icon" in Config.Config ["CartColumns"]:
            self.Device_Columns.CheckItem ( index )

        for Column in Config.Config ["CartColumns"]:
            if Column == "Icon" or Column == "ROM File (No Ext)":
                continue
            index = self.Device_Columns.InsertStringItem ( sys.maxint, Column )
            self.Device_Columns.SetStringItem ( index, 1, Config.Config ["CartColumn_Titles"][Column] )
            self.Device_Columns.CheckItem ( index )
        for Column in Config.Config ["Columns"]:
            if Column == "Icon" or Column == "ROM File (No Ext)":
                continue
            if Column not in Config.Config ["CartColumns"]:
                if Column != "Archive":
                    index = self.Device_Columns.InsertStringItem ( sys.maxint, Column )
                    self.Device_Columns.SetStringItem ( index, 1, Config.Config ["CartColumn_Titles"][Column] )  

        self.Device_Columns.SetColumnWidth( 0, wx.LIST_AUTOSIZE )
        self.Device_Columns.SetColumnWidth( 1, 200 )
        self.Device_Columns.Select( 0, True )
        
        self.Default_Device.Clear()
        for Device in Config.Config ["Devices"]:
            self.Default_Device.Append(Device[0])
            
        try:
            self.Default_Device.SetStringSelection(Config.Config ["Default_Device"])
        except:
            self.Default_Device.SetSelection(0)
            
        self.CartColUP.Disable()
        self.ROMColUP.Disable()
        self.CartColDown.Disable()
        self.ROMColDown.Disable()
        
        if self.GoToSaves:
            self.Notebook.ChangeSelection(2)

    def On_Alternate_Colour( self, event ): # wxGlade: cOptions.<event_handler>
        dlg = wx.ColourDialog( self )
        dlg.GetColourData().SetChooseFull( False )
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            self.Alternate_Colour.SetBackgroundColour( data.GetColour().Get() )

    def On_Pending_Colour(self, event): # wxGlade: cOptions.<event_handler>
        dlg = wx.ColourDialog( self )
        dlg.GetColourData().SetChooseFull( False )
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            self.Pending_Colour.SetBackgroundColour( data.GetColour().Get() )

    def OnColumnsListCtrlItemDeSelected( self, event ): # wxGlade: cOptions.<event_handler>
        if event.EventObject == self.ROM_Columns:
            Up = self.ROMColUP
            Down = self.ROMColDown
        else:
            Up = self.CartColUP
            Down = self.CartColDown

        if event.EventObject.GetSelectedItemCount() == 0:
            Up.Disable ()
            Down.Disable()

    def OnColumnsListCtrlItemSelected( self, event ): # wxGlade: cOptions.<event_handler>
        if event.EventObject == self.ROM_Columns:
            Up = self.ROMColUP
            Down = self.ROMColDown
        else:
            Up = self.CartColUP
            Down = self.CartColDown

        if event.EventObject.GetFirstSelected() > 1:
            Up.Enable()
        else:
            Down.Disable()
        if event.EventObject.GetFirstSelected() < event.EventObject.GetItemCount() - 1:
            Down.Enable()
        else:
            Down.Disable()
        if event.EventObject.GetFirstSelected() == 0:
            Up.Disable()
            Down.Disable()
        if event.EventObject.GetFirstSelected() == 1:
            Up.Disable()
        if event.EventObject.GetSelectedItemCount() == 0:
            Up.Disable ()
            Down.Disable()

    def On_Column_Up( self, event ): # wxGlade: cOptions.<event_handler>
        if event.EventObject == self.ROMColUP:
            Ctrl = self.ROM_Columns
        else:
            Ctrl = self.Device_Columns
            
        CurPos = Ctrl.GetFirstSelected()
        Item1 = Ctrl.GetItemText( CurPos )
        Item2 = Ctrl.GetItemText( CurPos - 1 )
        Item1C1 = Ctrl.GetItem( CurPos, 1 )
        Item2C1 = Ctrl.GetItem( CurPos - 1, 1 )
        Item1Checked = Ctrl.IsChecked( CurPos )
        Item2Checked = Ctrl.IsChecked( CurPos-1 )
        Ctrl.SetStringItem( CurPos, 0, Item2 )
        Ctrl.SetStringItem( CurPos - 1, 0, Item1 )
        Ctrl.SetStringItem( CurPos, 1, Item2C1.GetText() )
        Ctrl.SetStringItem( CurPos-1, 1, Item1C1.GetText() )
        Ctrl.CheckItem( CurPos, Item2Checked )
        Ctrl.CheckItem( CurPos-1, Item1Checked )
        Ctrl.SetItemState( CurPos-1, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED )


    def On_Column_Down( self, event ): # wxGlade: cOptions.<event_handler>
        if event.EventObject == self.ROMColDown:
            Ctrl = self.ROM_Columns
        else:
            Ctrl = self.Device_Columns
            
        CurPos = Ctrl.GetFirstSelected()
        Item1 = Ctrl.GetItemText( CurPos )
        Item2 = Ctrl.GetItemText( CurPos + 1 )
        Item1C1 = Ctrl.GetItem( CurPos, 1 )
        Item2C2 = Ctrl.GetItem( CurPos + 1, 1 )
        Item1Checked = Ctrl.IsChecked( CurPos )
        Item2Checked = Ctrl.IsChecked( CurPos+1 )
        Ctrl.SetStringItem( CurPos, 0, Item2 )
        Ctrl.SetStringItem( CurPos + 1, 0, Item1 )
        Ctrl.SetStringItem( CurPos, 1, Item2C2.GetText() )
        Ctrl.SetStringItem( CurPos+1, 1, Item1C1.GetText() )
        Ctrl.CheckItem( CurPos, Item2Checked )
        Ctrl.CheckItem( CurPos+1, Item1Checked )
        Ctrl.SetItemState( CurPos+1, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED )

    def ProcessOption ( self, Key, Value ):
        if Config.Config [Key] != Value:
            Config.Config [Key] = Value

    def On_OK( self, event ): # wxGlade: cOptions.<event_handler>
#_("Select ROMs Directory") + " : ")
#_("Select Images Directory") + " : ")
#_("Select NFO Directory") + " : ")
#_("Select Save Game Database Directory") + " : ")
#_("Select Device Directory") + " : ")
#_("Select Save Game Directory") + " : ")

        Msg = []
        if os.path.isdir(self.ROM_Path.GetValue()) == False:
            Msg.append (_("Invalid ROM Directory"))
        if os.path.isdir(self.Image_Path.GetValue()) == False:
            Msg.append (_("Invalid Images Directory"))
        if os.path.isdir(self.NFO_Path.GetValue()) == False:
            Msg.append (_("Invalid NFO Directory"))
        if os.path.isdir(self.Save_Path.GetValue()) == False:
            Msg.append (_("Invalid Save Database Directory"))
#        if os.path.isdir(self.Device_Path.GetValue()) == False:
#            Msg.append (_("Invalid Device Directory"))

        if sys.platform == "win32":
            if len (self.ROM_Path.GetValue()) < 3 or self.ROM_Path.GetValue()[2] != "\\":
                Msg.append (_("Invalid ROM Directory"))
            if len (self.Image_Path.GetValue()) < 3 or self.Image_Path.GetValue()[2] != "\\":
                Msg.append (_("Invalid Images Directory"))
            if len (self.NFO_Path.GetValue()) < 3 or self.NFO_Path.GetValue()[2] != "\\":
                Msg.append (_("Invalid NFO Directory"))
            if len (self.Save_Path.GetValue()) < 3 or self.Save_Path.GetValue()[2] != "\\":
                Msg.append (_("Invalid Save Database Directory"))
            if (len (self.Device_Path.GetValue()) < 3 or self.Device_Path.GetValue()[2] != "\\") and len (self.Device_Path.GetValue()) != 0:
                Msg.append (_("Invalid Device Directory"))
            if (len (self.Save_Dir_On_Cart.GetValue()) < 3 or self.Save_Dir_On_Cart.GetValue()[2] != "\\") and len (self.Device_Path.GetValue()) != 0:
                Msg.append (_("Invalid Save Directory on Device"))
            
        for m in Utils.unique (Msg):
            wx.MessageBox( m, _('Invalid Directory'), wx.OK| wx.ICON_EXCLAMATION )
        if Msg != []:
            return

        self.ProcessOption ( "ROM_Path", self.ROM_Path.GetValue() )
        self.ProcessOption ( "Image_Path", self.Image_Path.GetValue() )
        self.ProcessOption ( "NFO_Path", self.NFO_Path.GetValue() )
        self.ProcessOption ( "Device_Path", self.Device_Path.GetValue() )
        self.ProcessOption ( "Save_Path", self.Save_Path.GetValue() )
        self.ProcessOption ( "Save_Dir_On_Cart", self.Save_Dir_On_Cart.GetValue() )
        if Config.Config ["Save_Dir_On_Cart"] == "":
            Config.Config ["Save_Dir_On_Cart"] = Config.Config ["Device_Path"]
            
        self.ProcessOption ( "Save_Games_to_Keep", self.Save_Games_to_Keep.GetValue())
        self.ProcessOption ( "Show_Splash", self.Show_Splash.GetValue() )
        self.ProcessOption ( "Use_Trimmed", self.Use_Trimmed.GetValue() )
        self.ProcessOption ( "RealTime_Search", self.RealTime_Search.GetValue() )
        self.ProcessOption ( "Parse_Subdirs", self.Parse_Subdirs.GetValue() )
#        self.ProcessOption ( "DLGfx", self.DLGfx.GetValue(), None )
        self.ProcessOption ( "Auto_Backup_Saved_Games", self.Auto_Backup_Saved_Games.GetValue())
        self.ProcessOption ( "Swap_SS_and_Case", self.Swap_SS_and_Case.GetValue() )
        self.ProcessOption ( "Use_Original_Save_Time", self.Use_Original_Save_Time.GetValue())
        self.ProcessOption ( "Unknown_Name", self.Unknown_Name.GetStringSelection() )
        self.ProcessOption ( "Safe_Trim", self.Safe_Trim.GetValue() )
        self.ProcessOption ( "Search_Device_Subdirs", self.Search_Device_Subdirs.GetValue() )
#        self.ProcessOption ( "UseCRCFiles", self.UseCRCFiles.GetValue(), None )
        self.ProcessOption ( "AutoCopySaves", self.AutoCopySaves.GetValue() )
        self.ProcessOption ( "Filter_Use_Exact_Sizes", self.Filter_Use_Exact_Sizes.GetValue() )
        self.ProcessOption ( "UseShortSaveName", self.UseShortSaveName.GetValue())
        self.ProcessOption ( "Confirm_Delete", self.Confirm_Delete.GetValue() )
        self.ProcessOption ( "Delete_Saves_with_ROM", self.Delete_Saves_with_ROM.GetValue())
#        self.ProcessOption ( "SlowLookups", self.SlowLookups.GetValue(), "CART" )
        self.ProcessOption ( "Convert_Imports", self.Convert_Imports.GetValue())

        self.ProcessOption ( "Use_Rename_Popup", self.Use_Rename_Popup.GetValue() )
        self.ProcessOption ( "Use_Renaming", self.Use_Renaming.GetValue() )
        self.ProcessOption ( "Rename_Mask", self.Rename_Mask.GetValue() )
        self.ProcessOption ( "AutoCloseUpdate", self.AutoCloseUpdate.GetValue())
        
        self.ProcessOption ( "Alternate_Colour", self.Alternate_Colour.GetBackgroundColour() )
        self.ProcessOption ( "Pending_Colour", self.Pending_Colour.GetBackgroundColour() )
        
        self.ProcessOption ( "Default_Device", self.Default_Device.GetStringSelection())
        self.ProcessOption ( "Find_Unknown", self.Find_Unknown.GetValue())

        Str = self.Device_Dirs_to_Search.GetValue()
        Config.Config ["Device_Dirs_to_Search"] = Str.split ( "," )
#        Config.Config ["Device_Dirs_to_Search_Lower"] = []
#        for Item in Config.Config ["IncludeDirs"]:
#            Config.Config ["IncludeDirsLower"].append (Item.lower())
        
#        oldUnknownName = Config.Config ["Unknown_Name"]
        tmp = self.Unknown_Name.GetStringSelection()
        if tmp == _( "Archive File Name" ):
            Config.Config ["Unknown_Name"] = "ARCHIVE"
        elif tmp == _( "ROM File Name" ):
            Config.Config ["Unknown_Name"] = "FILENAME"
            
        tmp = self.Search_Method.GetStringSelection()
        if tmp == _( "Filename" ):
            Config.Config ["Search_Method"] = 1
        elif tmp == _( "ROM Title"):
            Config.Config ["Search_Method"] = 0
        else:
            Config.Config ["Search_Method"] = 2
            
#        if oldUnknownName != Config.Config ["UnknownName"]:
#            MyROMS.CloseUnknownShelve()
#            os.unlink ("Unknown.dat") 
#            MyROMS.OpenUnknownShelve()

        Orig_ROMColumns = copy.copy ( Config.Config ["ROMColumns"] )
        Orig_ROMColumn_Titles = copy.copy ( Config.Config ["ROMColumn_Titles"] )
        Orig_CartColumns = copy.copy ( Config.Config ["CartColumns"] )
        Orig_CartColumn_Titles = copy.copy ( Config.Config ["CartColumn_Titles"] )
        
        Config.Config ["ROMColumns"] = []
        for Count in range ( 0, self.ROM_Columns.GetItemCount() ):
            if self.ROM_Columns.IsChecked( Count ):
                Config.Config ["ROMColumns"].append( self.ROM_Columns.GetItemText ( Count ) )
            Config.Config ["ROMColumn_Titles"][self.ROM_Columns.GetItemText( Count )] = self.ROM_Columns.GetItem( Count, 1 ).GetText ()
    
        if Orig_ROMColumns == Config.Config ["ROMColumns"] and Orig_ROMColumn_Titles == Config.Config ["ROMColumn_Titles"]:
            pass
        else:
            self.ColumnsChanged = True

        Config.Config ["CartColumns"] = []
        for Count in range ( 0, self.Device_Columns.GetItemCount() ):
            if self.Device_Columns.IsChecked( Count ):
                Config.Config ["CartColumns"].append( self.Device_Columns.GetItemText ( Count ) )
            Config.Config ["CartColumn_Titles"][self.Device_Columns.GetItemText( Count )] = self.Device_Columns.GetItem( Count, 1 ).GetText ()
    
        if Orig_CartColumns == Config.Config ["CartColumns"] and Orig_CartColumn_Titles == Config.Config ["CartColumn_Titles"]:
            pass
        else:
            self.ColumnsChanged = True

        event.Skip()

    def On_Use_Renaming(self, event): # wxGlade: cOptions.<event_handler>
        if self.Use_Renaming.IsChecked():
            self.Rename_Mask.Enable(True)
            self.Rename_Label1.Enable(True)
            self.Rename_Label2.Enable(True)
            self.Rename_Label3.Enable(True)
            self.Rename_Label4.Enable(True)
            self.Rename_Label5.Enable(True)
            self.Rename_Label6.Enable(True)
            self.Rename_Label7.Enable(True)
            self.Rename_Label8.Enable(True)
        else:
            self.Rename_Mask.Enable(False)
            self.Rename_Label1.Enable(False)
            self.Rename_Label2.Enable(False)
            self.Rename_Label3.Enable(False)
            self.Rename_Label4.Enable(False)
            self.Rename_Label5.Enable(False)
            self.Rename_Label6.Enable(False)
            self.Rename_Label7.Enable(False)
            self.Rename_Label8.Enable(False)

    def dbbCallback( self, event ):
        TmpDir = event.GetString()
        
        if event.EventObject.Parent == self.Device_Path and self.Orig_Device_Path != TmpDir:
            self.Save_Dir_On_Cart.SetValue ( TmpDir )
            self.Orig_Device_Path = TmpDir

    def On_Device_Type_Change(self, event): # wxGlade: cOptions.<event_handler>
        if event.String == "SuperCard DS One (.sav)":
            self.UseShortSaveName.SetValue(True)
        else:
            self.UseShortSaveName.SetValue(False)

# end of class cOptions