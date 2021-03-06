# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.1 on Wed Nov 14 13:34:33 2007

import wx
import wx.gizmos as gizmos
import os
import glob
from stat import ST_SIZE
import sys
if sys.platform == "win32":
    import win32api #@UnresolvedImport
import shutil
import time

import Config
from ROMS import MyROMS
import Utils
import GFX
from cSaveGameConvert import cSaveGameConvert
from cOptions import cOptions

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class cSaveGameManager( wx.Dialog ):
    def __init__( self, *args, **kwds ):
        self.Save_Comments_Shelve = kwds["Save_Comments_Shelve"]
        del kwds["Save_Comments_Shelve"]
        self.Select = kwds["Select"]
        del kwds["Select"]
        # begin wxGlade: cSaveGameManager.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.THICK_FRAME
        wx.Dialog.__init__( self, *args, **kwds )
        self.SaveGameManager_Panel = wx.Panel( self, - 1 )
        self.Copy_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_Copy16"].getBitmap() ) )
        self.Edit_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_Edit16"].getBitmap() ) )
        self.Delete_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_Delete16"].getBitmap() ) )
        self.Duplicate_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_Duplicate16"].getBitmap() ) )
        self.Convert_Saves_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_Convert16"].getBitmap() ) )
        self.Find_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_Search16"].getBitmap() ) )
        self.Delete_All_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_SGM_DeleteAll16"].getBitmap() ) )
        self.Options_Button = wx.BitmapButton( self.SaveGameManager_Panel, - 1, ( GFX.catalog ["GFX_Icon_Options16"].getBitmap() ) )
        self.label_7 = wx.StaticText( self.SaveGameManager_Panel, - 1, _( "Default Device : " ) )
        self.Default_Device = wx.Choice( self.SaveGameManager_Panel, - 1, choices = [] )
        self.SGMTreeCtrl = gizmos.TreeListCtrl( self, - 1, style = wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT )

        self.__set_properties()
        self.__do_layout()

        self.Bind( wx.EVT_BUTTON, self.On_Copy, self.Copy_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Edit, self.Edit_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Delete, self.Delete_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Duplicate, self.Duplicate_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Convert_Saves, self.Convert_Saves_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Find_Button, self.Find_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Delete_All, self.Delete_All_Button )
        self.Bind( wx.EVT_BUTTON, self.On_Options, self.Options_Button )
        self.Bind( wx.EVT_CHOICE, self.On_Default_Device, self.Default_Device )
        # end wxGlade
        self.Bind( wx.EVT_FIND, self.On_Find )
        self.Bind( wx.EVT_FIND_NEXT, self.On_Find )
        self.Bind( wx.EVT_FIND_REPLACE, self.On_Find )
        self.Bind( wx.EVT_FIND_REPLACE_ALL, self.On_Find )
        self.Bind( wx.EVT_FIND_CLOSE, self.On_FindClose )

    def __set_properties( self ):
        # begin wxGlade: cSaveGameManager.__set_properties
        self.SetTitle( _( "Save Game Manager" ) )
        self.Copy_Button.SetToolTipString( _( "Copy Save to Device" ) )
        self.Copy_Button.SetSize( self.Copy_Button.GetBestSize() )
        self.Edit_Button.SetToolTipString( _( "Edit Save Comment" ) )
        self.Edit_Button.SetSize( self.Edit_Button.GetBestSize() )
        self.Delete_Button.SetToolTipString( _( "Delete Save Game" ) )
        self.Delete_Button.SetSize( self.Delete_Button.GetBestSize() )
        self.Duplicate_Button.SetToolTipString( _( "Duplicate Save Game" ) )
        self.Duplicate_Button.SetSize( self.Duplicate_Button.GetBestSize() )
        self.Convert_Saves_Button.SetToolTipString( _( "Convert Save Type" ) )
        self.Convert_Saves_Button.Hide()
        self.Convert_Saves_Button.SetSize( self.Convert_Saves_Button.GetBestSize() )
        self.Find_Button.SetToolTipString( _( "Search" ) )
        self.Find_Button.SetSize( self.Find_Button.GetBestSize() )
        self.Delete_All_Button.SetToolTipString( _( "Delete All Saves for Selected Game" ) )
        self.Delete_All_Button.SetSize( self.Delete_All_Button.GetBestSize() )
        self.Options_Button.SetToolTipString( _( "Options" ) )
        self.Options_Button.SetSize( self.Options_Button.GetBestSize() )
        self.Default_Device.SetMinSize( ( 150, 21 ) )
        self.SGMTreeCtrl.SetFocus()
        # end wxGlade

        ToolSize = Config.Config ["Toolbar_Size"]
        self.Copy_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_Copy" + ToolSize + "Bitmap" )() )
        self.Edit_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_Edit" + ToolSize + "Bitmap" )() )
        self.Delete_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_Delete" + ToolSize + "Bitmap" )() )
        self.Delete_All_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_DeleteAll" + ToolSize + "Bitmap" )() )
        self.Convert_Saves_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_Convert" + ToolSize + "Bitmap" )() )
        self.Duplicate_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_Duplicate" + ToolSize + "Bitmap" )() )
        self.Options_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_Options" + ToolSize + "Bitmap" )() )
        self.Find_Button.SetBitmapLabel( eval ( "GFX.getGFX_Icon_SGM_Search" + ToolSize + "Bitmap" )() )

    def __do_layout( self ):
#        self.Freeze()
        # begin wxGlade: cSaveGameManager.__do_layout
        SaveGameManager_Sizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        SaveGameManager_Panel_Sizer = wx.FlexGridSizer( 1, 10, 0, 0 )
        SaveGameManager_Panel_Sizer.Add( self.Copy_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Edit_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Delete_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Duplicate_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Convert_Saves_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Find_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Delete_All_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Options_Button, 0, wx.TOP | wx.BOTTOM, 3 )
        SaveGameManager_Panel_Sizer.Add( self.label_7, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3 )
        SaveGameManager_Panel_Sizer.Add( self.Default_Device, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0 )
        self.SaveGameManager_Panel.SetSizer( SaveGameManager_Panel_Sizer )
        SaveGameManager_Panel_Sizer.AddGrowableCol( 9 )
        SaveGameManager_Sizer.Add( self.SaveGameManager_Panel, 1, wx.EXPAND, 0 )
        SaveGameManager_Sizer.Add( self.SGMTreeCtrl, 1, wx.EXPAND, 0 )
        self.SetSizer( SaveGameManager_Sizer )
        SaveGameManager_Sizer.Fit( self )
        SaveGameManager_Sizer.AddGrowableRow( 1 )
        SaveGameManager_Sizer.AddGrowableCol( 0 )
        self.Layout()
        # end wxGlade
        self.__LocalInit ()        
#        self.Thaw()
        
    def __LocalInit ( self ):
        self.ColumnsChanged = False
        self.Result = wx.ID_CANCEL
        
        self.SetSize( Config.Config ["SGM_Size"] )
        
        if Config.Config ["SGM_Position"] [ 0 ] == - 1:
            self.CentreOnScreen ()
        else:
            self.SetPosition( Config.Config ["SGM_Position"] )
            
        self.Bind( wx.EVT_SIZE, self.On_Window_Size )
        self.Bind( wx.EVT_MOVE, self.On_Window_Move )
        self.Bind ( wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChanged, self.SGMTreeCtrl )
        self.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnTreeRightClick, self.SGMTreeCtrl )
        self.Bind( wx.EVT_LIST_COL_END_DRAG, self.OnTreeColResized, self.SGMTreeCtrl )

        ImageSize = ( 16, 16 )
        self.ImageList = wx.ImageList( ImageSize[0], ImageSize[1] )
        self.fldridx = self.ImageList.Add( GFX.catalog ["GFX_Icon_Folder"].getBitmap() )
        self.fldropenidx = self.ImageList.Add( GFX.catalog ["GFX_Icon_FolderOpen"].getBitmap() )
        self.fileidx = self.ImageList.Add( GFX.catalog ["GFX_Icon_SaveFile"].getBitmap() )

        self.SGMTreeCtrl.SetImageList( self.ImageList )

        self.SGMTreeCtrl.AddColumn( _( "Rel No / Title" ) )
        self.SGMTreeCtrl.AddColumn( _( "No" ) )
        self.SGMTreeCtrl.AddColumn( _( "Date / Time" ) )
        self.SGMTreeCtrl.AddColumn( _( "Save Type / Size" ) )
        self.SGMTreeCtrl.SetMainColumn( 0 )
        self.SGMTreeCtrl.SetColumnWidth( 0, Config.Config ["SGM_Col_Sizes"][0] )
        self.SGMTreeCtrl.SetColumnWidth( 1, Config.Config ["SGM_Col_Sizes"][1] )
        self.SGMTreeCtrl.SetColumnWidth( 2, Config.Config ["SGM_Col_Sizes"][2] )
        self.SGMTreeCtrl.SetColumnWidth( 3, Config.Config ["SGM_Col_Sizes"][3] )
        
        self.Populate()

        self.Default_Device.Clear()
        for Device in Config.Config ["Devices"]:
            self.Default_Device.Append( Device[0] )
            
        try:
            self.Default_Device.SetStringSelection( Config.Config ["Default_Device"] )
        except:
            self.Default_Device.SetSelection( 0 )

    def On_Window_Size ( self, event ):
        Config.Config ["SGM_Size"] = self.GetSize()
        event.Skip ()
    
    def On_Window_Move ( self, event ):
        Config.Config ["SGM_Position"] = self.GetScreenPosition()
        event.Skip ()

    def OnTreeRightClick ( self, event ):
        item = event.GetItem()
        self.m_SelItem = item
        self.m_SelItemText = self.SGMTreeCtrl.GetItemText( item )
        if item and self.SGMTreeCtrl.GetItemText( item )[:5] == "Save ":
            if not hasattr( self, "popupSaveTree1" ):
                self.popupSaveTree1 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.On_Copy, id = self.popupSaveTree1 )
                self.popupSaveTree2 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.On_Edit, id = self.popupSaveTree2 )
                self.popupSaveTree3 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.On_Delete, id = self.popupSaveTree3 )
                self.popupSaveTree4 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.On_Convert_Saves, id = self.popupSaveTree4 )
                self.popupSaveTree5 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.On_Duplicate, id = self.popupSaveTree5 )
            menu = wx.Menu()
            if self.Parent.Device_List.IsEnabled() and os.path.isdir ( Config.Config["Save_Dir_On_Cart"] ):
                item = wx.MenuItem( menu, self.popupSaveTree1, _( "Copy to Device" ) )
                menu.AppendItem( item )
            item = wx.MenuItem( menu, self.popupSaveTree2, _( "Edit Save Comment" ) )
            menu.AppendItem( item )
            item = wx.MenuItem( menu, self.popupSaveTree5, _( "Duplicate Save" ) )
            menu.AppendItem( item )
#            item = wx.MenuItem( menu, self.popupSaveTree4, _("Convert Save Game") )
#            menu.AppendItem( item )
            item = wx.MenuItem( menu, self.popupSaveTree3, _( "Delete Save Game" ) )
            menu.AppendItem( item )
            self.PopupMenu( menu )
            menu.Destroy()
        elif item and self.SGMTreeCtrl.GetItemText( item )[:5] != "Saves":
            if not hasattr( self, "popupSaveTree11" ):
                self.popupSaveTree11 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.On_Delete_All, id = self.popupSaveTree11 )
            menu = wx.Menu()
            item = wx.MenuItem( menu, self.popupSaveTree11, _( "Delete All Saves for this Game" ) )
            menu.AppendItem( item )
            self.PopupMenu( menu )
            menu.Destroy()
        elif item and self.SGMTreeCtrl.GetItemText( item )[:5] == "Saves":
            if not hasattr( self, "popupSaveTree21" ):
                self.popupSaveTree21 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.OnExpandAll, id = self.popupSaveTree21 )
                self.popupSaveTree22 = wx.NewId()
                self.Bind( wx.EVT_MENU, self.OnCollapseAll, id = self.popupSaveTree22 )
            menu = wx.Menu()
            item = wx.MenuItem( menu, self.popupSaveTree21, _( "Expand All" ) )
            menu.AppendItem( item )
            item = wx.MenuItem( menu, self.popupSaveTree22, _( "Collapse All" ) )
            menu.AppendItem( item )
            self.PopupMenu( menu )
            menu.Destroy()

        event.Skip()
    
    def OnTreeColResized ( self, event ):
        ColNum = event.Column
        Config.Config ["SGM_Col_Sizes"][ ColNum ] = self.SGMTreeCtrl.GetColumnWidth( ColNum )
        event.Skip()
        
    def OnTreeSelChanged ( self, event ):
        item = event.GetItem()
        self.m_SelItem = item
        self.m_SelItemText = self.SGMTreeCtrl.GetItemText( item )
        if item and self.SGMTreeCtrl.GetItemText( item )[:5] == "Save ":
            if self.Parent.Device_List.IsEnabled() and os.path.isdir ( Config.Config["Save_Dir_On_Cart"] ):
                self.Copy_Button.Enable( True )
            else:
                self.Copy_Button.Enable( False )
            self.Edit_Button.Enable( True )
            self.Duplicate_Button.Enable( True )
            self.Delete_Button.Enable( True )
            self.Delete_All_Button.Enable( False )
            self.Convert_Saves_Button.Enable( True )
        elif item and self.SGMTreeCtrl.GetItemText( item )[:5] != "Saves":
            self.Copy_Button.Enable( False )
            self.Edit_Button.Enable( False )
            self.Duplicate_Button.Enable( False )
            self.Delete_Button.Enable( False )
            self.Delete_All_Button.Enable( True )
            self.Convert_Saves_Button.Enable( False )
        elif item:
            self.Copy_Button.Enable( False )
            self.Edit_Button.Enable( False )
            self.Duplicate_Button.Enable( False )
            self.Delete_Button.Enable( False )
            self.Delete_All_Button.Enable( False )
            self.Convert_Saves_Button.Enable( False )
    
        event.Skip()

    def Populate( self ):
        self.SGMTreeCtrl.DeleteAllItems()
#        Config ["Save_Extensions"] = [ ".sav", ".duc", ".dss", ".0", ".dat" ]
#        DirList = []
#        for Extension in Config.Config["Save_Extensions"]:
        SearchStr = os.path.join ( Config.Config ["Save_Path"], "*" + ".sav" + ".[0-9][0-9][0-9]" )
        DirList = glob.glob ( SearchStr )

        self.root = self.SGMTreeCtrl.AddRoot( "Saves" )
        self.SGMTreeCtrl.SetItemImage( self.root, self.fldridx, which = wx.TreeItemIcon_Normal )
        self.SGMTreeCtrl.SetItemImage( self.root, self.fldropenidx, which = wx.TreeItemIcon_Expanded )
        self.SGMTreeCtrl.SetItemImage( self.root, self.fldridx, which = wx.TreeItemIcon_Selected )
        self.SGMTreeCtrl.SetItemImage( self.root, self.fldropenidx, which = wx.TreeItemIcon_SelectedExpanded )

        child = None
        Count = 0
        Hilight = None
        
        for File in sorted ( DirList ):
            if os.path.isdir( File ):
                pass
            else:
                CRC = os.path.split ( File )[1]
                CRC = os.path.splitext ( CRC )[0]
                CRC = os.path.splitext ( CRC )[0]
                
                try:
                    ROM = MyROMS.Lookup_ROM_CRC ( CRC )
                except:
                    continue
                
                DisplayName = "%s - %s" % ( ROM.Comment, ROM.Title )
                
                Ext = os.path.splitext( File )[1]
                SaveNum = Ext[1:]
                
                if SaveNum == "001":
                    if child != None:
                        self.SGMTreeCtrl.SetItemText ( child, "%d" % ( Count - 1 ) , 1 )
                    child = self.SGMTreeCtrl.AppendItem( self.root, DisplayName )
                    self.SGMTreeCtrl.SetItemText( child, "0", 1 )
                    self.SGMTreeCtrl.SetItemText( child, "", 2 )
                    self.SGMTreeCtrl.SetItemText( child, ROM.Save_Type, 3 )
                    self.SGMTreeCtrl.SetItemImage( child, self.fldridx, which = wx.TreeItemIcon_Normal )
                    self.SGMTreeCtrl.SetItemImage( child, self.fldropenidx, which = wx.TreeItemIcon_Expanded )
                    self.SGMTreeCtrl.SetItemImage( child, self.fldridx, which = wx.TreeItemIcon_Selected )
                    self.SGMTreeCtrl.SetItemImage( child, self.fldropenidx, which = wx.TreeItemIcon_SelectedExpanded )
                    self.SGMTreeCtrl.SetItemPyData( child, CRC )
                    if self.Select == DisplayName:
                        Hilight = child
                    Count = 1

                Comment = ""
                Date = _( "Unknown" )
                if Count > 0:
                    if self.Save_Comments_Shelve.has_key( str ( CRC + "%03d" % ( Count ) ) ):
                        Comment = self.Save_Comments_Shelve[ str ( CRC + "%03d" % ( Count ) )]
                    else:
                        Comment = ""
                    Count += 1
                    try:
#                        Stat = os.stat( File )
#                        Date = datetime.datetime.fromtimestamp( Stat[ST_MTIME] )
                        Date = "%s %s" % ( win32api.GetDateFormat ( win32api.GetSystemDefaultLCID(), 0, time.localtime( os.path.getmtime ( os.path.join ( Config.Config ["Save_Path"], File ) ) ) ).lower(), win32api.GetTimeFormat ( win32api.GetSystemDefaultLCID(), 0, time.localtime( os.path.getmtime ( os.path.join ( Config.Config ["Save_Path"], File ) ) ) ) )
                    except:
                        Date = _( "Unknown" )
                try:
                    childchild = self.SGMTreeCtrl.AppendItem( child, "Save %s - %s" % ( SaveNum, Comment ) )
                    self.SGMTreeCtrl.SetItemImage( childchild, self.fileidx, which = wx.TreeItemIcon_Normal )
                    self.SGMTreeCtrl.SetItemImage( childchild, self.fileidx, which = wx.TreeItemIcon_Selected )
                    self.SGMTreeCtrl.SetItemText( childchild, str( Date ), 2 )
                    Size = os.stat( os.path.join ( Config.Config ["Save_Path"], File ) )[ST_SIZE]
                    self.SGMTreeCtrl.SetItemText( childchild, Utils.Format_ROM_Size( Size ), 3 )
                    self.SGMTreeCtrl.SetItemPyData( childchild, CRC )
                except:
                    pass
    
        if child != None:
            self.SGMTreeCtrl.SetItemText ( child, "%d" % ( Count - 1 ) , 1 )

        self.SGMTreeCtrl.Expand( self.root )
        self.SGMTreeCtrl.SortChildren( self.root )
        
        self.SGMTreeCtrl.SetFocus()
        if Hilight:
#            print Hilight
            self.SGMTreeCtrl.Expand( Hilight )
#            self.SGMTreeCtrl.UnselectAll()
#            self.SGMTreeCtrl.SelectItem( Hilight )
#            self.SGMTreeCtrl.ScrollTo( Hilight )
            self.SGMTreeCtrl.EnsureVisible( Hilight )
#            print self.SGMTreeCtrl.IsVisible(Hilight)

    def On_Copy( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        CRC = self.SGMTreeCtrl.GetItemPyData( self.m_SelItem )
        ROM = MyROMS.Lookup_ROM_CRC ( CRC )
        
        if self.Parent.Device_List.Get_CRC_List().count ( CRC ) == 1:
            Files = []
            ROMS = []
            for a in self.Parent.Device_List.ROM_List:
                if a.ROM_CRC == CRC:
                    Files.append ( a.Name_On_Device )
                    ROMS.append ( a )
            ROM = ROMS [0]

        if self.Parent.Device_List.Get_CRC_List().count ( CRC ) > 1:
            Files = []
            ROMS = []
            for a in self.Parent.Device_List.ROM_List:
                if a.ROM_CRC == CRC:
                    Files.append ( a.Name_On_Device )
                    ROMS.append ( a )
            dlg = wx.SingleChoiceDialog( 
                    self, 'Select a File to Copy Save to:', 'Multiple ROMs Exist',
                    Files,
                    wx.CHOICEDLG_STYLE
                    )
    
            if dlg.ShowModal() == wx.ID_OK:
                ROM = ROMS [dlg.GetSelection()]
            else:
                return
            
        SaveName = ""
        if CRC not in self.Parent.Device_List.Get_CRC_List():
            Res = wx.MessageBox( _( 'ROM is not on the Device\n\nDo You Wish to Copy it Anyway?' ), _( 'ROM Not Found' ), wx.YES_NO | wx.ICON_QUESTION )
            if Res != wx.YES:
                return
            SaveName = os.path.splitext ( Utils.Get_Name_on_Device ( ROM ) )[0] + Utils.Get_Save_Extension()
        
        Text = self.SGMTreeCtrl.GetItemText( self.m_SelItem )
        SaveNum = Text[5:Text.find( " - " )]
        OriginalSaveName = os.path.join ( Config.Config ["Save_Path"], "%s.sav.%s" % ( CRC, SaveNum ) )

        self.SetCursor( wx.StockCursor( wx.CURSOR_WAIT ) )

        try:
#            SaveFileIn  = open ( OriginalSaveName, "rb" )
##            SaveFileOut = open ( Utils.Get_Savename_on_Device ( ROM ), "wb" )
#            if SaveName == Utils.Get_Save_Extension():
#                raise RuntimeError
#            if SaveName == "":
#                SaveName = os.path.splitext (ROM.Name_On_Device)[0] + Utils.Get_Save_Extension()
#            SaveFileOut = open (SaveName, "wb")
#            SaveFileOut.write ( SaveFileIn.read() )
#            SaveFileOut.close()
#            SaveFileIn.close()

            SaveFileIn = open ( OriginalSaveName, "rb" )
            Data = SaveFileIn.read ()
            SaveFileIn.close()
#            SaveFileOut = open ( Utils.Get_Savename_on_Device ( ROM ), "wb" )

#            if SaveName == Utils.Get_Save_Extension():
#                raise RuntimeError

            if SaveName == "":
                SaveName = os.path.splitext ( ROM.Name_On_Device )[0] + Utils.Get_Save_Extension()

            SaveName = os.path.join( Config.Config["Save_Dir_On_Cart"], os.path.split ( SaveName )[1] )
            Utils.Write_Save( ROM, Data, SaveName )

            self.SetCursor( wx.StockCursor( wx.CURSOR_ARROW ) )
            
            wx.MessageBox( _( "Save Game Successfully Copied" ), _( 'Success' ), wx.OK | wx.ICON_INFORMATION )
        except:
            self.SetCursor( wx.StockCursor( wx.CURSOR_ARROW ) )
            
            wx.MessageBox( _( "Save Game Has Not Been Copied" ), _( 'Failed' ), wx.OK | wx.ICON_ERROR )

    def On_Edit( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        CRC = self.SGMTreeCtrl.GetItemPyData( self.m_SelItem )
        Text = self.SGMTreeCtrl.GetItemText( self.m_SelItem )
        SaveNum = Text[5:Text.find( " - " )]
        if self.Save_Comments_Shelve.has_key( str ( CRC + SaveNum ) ):
            Comment = self.Save_Comments_Shelve[ str ( CRC + SaveNum )]
        else:
            Comment = ""

        dlg = wx.TextEntryDialog( 
                self, _( 'Enter a New Comment for this Save Game' ),
                _( 'Edit Save Game Comment' ), 'Python' )

        dlg.SetValue( Comment )

        if dlg.ShowModal() == wx.ID_OK:
            Comment = dlg.GetValue()
            self.Save_Comments_Shelve[ str ( CRC + SaveNum )] = Comment
            self.Save_Comments_Shelve.sync ()
            self.SGMTreeCtrl.SetItemText ( self.m_SelItem, "Save " + SaveNum + " - " + Comment, 0 )

        dlg.Destroy()

    def On_Delete( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        CRC = self.SGMTreeCtrl.GetItemPyData( self.m_SelItem )
        ROM = MyROMS.Lookup_ROM_CRC ( CRC )
        
        Text = self.SGMTreeCtrl.GetItemText( self.m_SelItem )
        SaveNum = int ( Text[5:Text.find( " - " )] )
        
        AnyMoves = False
        for Count in range ( SaveNum + 1, Config.Config ["Save_Games_to_Keep"] + 1 ):
            if os.path.isfile ( os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( Count ) ):
                shutil.move( os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( Count ), os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( Count - 1 ) )
                AnyMoves = True
                if self.Save_Comments_Shelve.has_key( str ( CRC + "%03d" % ( Count ) ) ):
                    self.Save_Comments_Shelve [str ( CRC + "%03d" % ( Count - 1 ) )] = self.Save_Comments_Shelve [str ( CRC + "%03d" % ( Count ) )]
                    self.Save_Comments_Shelve.sync ()
            else:
                if self.Save_Comments_Shelve.has_key( str ( CRC + "%03d" % ( Count ) ) ):
                    del self.Save_Comments_Shelve [str ( CRC + "%03d" % ( Count ) )]
                    self.Save_Comments_Shelve.sync ()
                    
        if AnyMoves == False:
            try:
                os.unlink ( os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( SaveNum ) )
                if self.Save_Comments_Shelve.has_key( str ( CRC + "%03d" % ( SaveNum ) ) ):
                    del self.Save_Comments_Shelve [str ( CRC + "%03d" % ( SaveNum ) )]
                    self.Save_Comments_Shelve.sync ()
            except:
                pass

        OldSelect = self.Select
        self.Select = "%s - %s" % ( ROM.Comment, ROM.Title )
        
        self.Populate()

        self.Select = OldSelect

    def On_Duplicate( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        CRC = self.SGMTreeCtrl.GetItemPyData( self.m_SelItem )
        ROM = MyROMS.Lookup_ROM_CRC ( CRC )
        
        Text = self.SGMTreeCtrl.GetItemText( self.m_SelItem )
        SaveNum = int ( Text[5:Text.find( " - " )] )
        OriginalSaveName = os.path.join ( Config.Config ["Save_Path"], "%s.sav.%03d" % ( CRC, SaveNum ) )
        
        if SaveNum == Config.Config ["Save_Games_to_Keep"]:
            wx.MessageBox( _( 'Save Game will Exceed Maximum Number to Keep.' ), _( 'Error' ), wx.OK | wx.ICON_EXCLAMATION )
            return

        for Count in range ( Config.Config ["Save_Games_to_Keep"] - 1, SaveNum, - 1 ):
            if os.path.isfile ( os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( Count ) ):
                shutil.move( os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( Count ), os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( Count + 1 ) )
                if self.Save_Comments_Shelve.has_key( str ( CRC + "%03d" % ( Count ) ) ):
                    self.Save_Comments_Shelve [str ( CRC + "%03d" % ( Count + 1 ) )] = self.Save_Comments_Shelve [str ( CRC + "%03d" % ( Count ) )]
                    self.Save_Comments_Shelve.sync ()
        shutil.copy2 ( OriginalSaveName, os.path.join ( Config.Config ["Save_Path"], CRC ) + ".sav.%03d" % ( SaveNum + 1 ) )
        if self.Save_Comments_Shelve.has_key( str ( CRC + "%03d" % SaveNum ) ):
            self.Save_Comments_Shelve [str ( CRC + "%03d" % ( SaveNum + 1 ) )] = "Copy of " + self.Save_Comments_Shelve [str ( CRC + "%03d" % ( SaveNum ) )]
            self.Save_Comments_Shelve.sync ()
        else:
            self.Save_Comments_Shelve [str ( CRC + "%03d" % ( SaveNum + 1 ) )] = "Copy of Slot %d" % ( SaveNum ) 
            self.Save_Comments_Shelve.sync ()

        OldSelect = self.Select
        self.Select = "%s - %s" % ( ROM.Comment, ROM.Title )
        
        self.Populate()

        self.Select = OldSelect

    def On_Convert_Saves( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        CRC = self.SGMTreeCtrl.GetItemPyData( self.m_SelItem )
        ROM = MyROMS.Lookup_ROM_CRC ( CRC )

        Text = self.SGMTreeCtrl.GetItemText( self.m_SelItem )
        SaveNum = int ( Text[5:Text.find( " - " )] )
        OriginalSaveName = os.path.join ( Config.Config ["Save_Path"], "%s.sav.%03d" % ( CRC, SaveNum ) )

        dlg = cSaveGameConvert ( self, Save_File = OriginalSaveName, ROM = ROM, InSGM = True )
        dummy_Result = dlg.ShowModal()
        dlg.Destroy()

        OldSelect = self.Select
        self.Select = "%s - %s" % ( ROM.Comment, ROM.Title )
        
        self.Populate()

        self.Select = OldSelect

    def On_Delete_All( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        CRC = self.SGMTreeCtrl.GetItemPyData( self.m_SelItem )
        SearchStr = os.path.join ( Config.Config ["Save_Path"], CRC + ".sav.*" )

        DirList = glob.glob ( SearchStr )

        for File in sorted ( DirList ):
            if os.path.isdir( File ):
                pass
            else:
                try:
                    os.unlink( File )
                except:
                    pass
        for Count in range ( 1, Config.Config["Save_Games_to_Keep"] ):
            try:
                del ( self.Save_Comments_Shelve [str ( CRC + "%03d" % Count )] )
            except:
                pass

        self.SGMTreeCtrl.DeleteChildren( self.m_SelItem )
        self.SGMTreeCtrl.Delete( self.m_SelItem )
        wx.MessageBox( _( 'Save Games have been Deleted' ), _( 'Complete' ), wx.OK | wx.ICON_INFORMATION )

    def OnExpandAll ( self, event ):
        self.SGMTreeCtrl.ExpandAll( self.root )

    def OnCollapseAll ( self, event ):
        nc = self.SGMTreeCtrl.GetChildrenCount( self.root, False )
        
        cookie = 1
        for dummy in range( nc ):
            if dummy == 0:
                child, cookie = self.SGMTreeCtrl.GetFirstChild( self.root )
            else:
                child, cookie = self.SGMTreeCtrl.GetNextChild( self.root, cookie )
            self.SGMTreeCtrl.Collapse( child )

    def On_Options( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        dlg = cOptions ( self, GoToSaves = True )
        
        self.Result = dlg.ShowModal ()
        self.ColumnsChanged = dlg.ColumnsChanged
        
        dlg.Destroy ()

    def On_Default_Device( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        if event.String == "SuperCard DS One (.sav)":
            Config.Config ["UseShortSaveName"] = True
        else:
            Config.Config ["UseShortSaveName"] = False
        Config.Config ["Default_Device"] = event.String

    
    def On_Find_Button( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        self.Find_Button.Disable()
        self.Find_Position = - 1
        data = wx.FindReplaceData()
        dlg = wx.FindReplaceDialog( self, data, "Find Save", wx.FR_NOUPDOWN | wx.FR_NOMATCHCASE | wx.FR_NOWHOLEWORD )
        dlg.data = data  # save a reference to it...
        dlg.Show( True )
        
    def On_Find( self, event ): # wxGlade: cSaveGameManager.<event_handler>
        Find_Text = event.GetFindString()
        self.Enable( False )
        event.Dialog.Enable ( False )

        nc = self.SGMTreeCtrl.GetChildrenCount( self.root, False )
        cookie = 1
        Found = False
        for dummy in range( nc ):
            if dummy == 0:
                child, cookie = self.SGMTreeCtrl.GetFirstChild( self.root )
            else:
                child, cookie = self.SGMTreeCtrl.GetNextChild( self.root, cookie )
            if dummy > self.Find_Position:
                if self.SGMTreeCtrl.GetItemText( child ).upper ().find ( Find_Text.upper() ) != - 1:
                    Found = True
                    self.Find_Position = dummy
#                    self.SGMTreeCtrl.Expand( Hilight )
                    self.SGMTreeCtrl.SelectItem( child )
#                    self.SGMTreeCtrl.ScrollTo( Hilight )
                    self.SGMTreeCtrl.EnsureVisible( child )
                    break
        if Found == False:
            wx.MessageBox( _( 'Save Game Not Found' ), _( 'Not Found' ), wx.OK | wx.ICON_INFORMATION )
            self.Find_Position = - 1
        event.Dialog.Enable ( True )

    def On_FindClose( self, evt ):
        evt.GetDialog().Destroy()
        self.Find_Button.Enable()
        self.Enable( True )
        
# end of class cSaveGameManager