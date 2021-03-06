# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.1 on Fri Nov 16 10:36:38 2007

import sys
import wx

from ColumnListCtrlMixin import SGCListCtrlMixin

import Config

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class cSaveGameComments( wx.Dialog ):
    def __init__( self, *args, **kwds ):
        # begin wxGlade: cSaveGameComments.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__( self, *args, **kwds )
        self.Label_Text = wx.StaticText( self, - 1, _( "Enter You Notes in the Comments Column Below :" ) )
        self.SGCList = SGCListCtrlMixin( self, - 1 )
        self.OK_Button = wx.Button( self, wx.ID_OK, _( "&OK" ) )

        self.__set_properties()
        self.__do_layout()

        self.Bind( wx.EVT_BUTTON, self.On_OK, id = wx.ID_OK )
        # end wxGlade

    def __set_properties( self ):
        # begin wxGlade: cSaveGameComments.__set_properties
        self.SetTitle( _( "Save Game Comments" ) )
        # end wxGlade

    def __do_layout( self ):
        self.Freeze()
        # begin wxGlade: cSaveGameComments.__do_layout
        SGCSizer = wx.FlexGridSizer( 3, 1, 0, 0 )
        SGCSizer.Add( self.Label_Text, 0, wx.ALL, 3 )
        SGCSizer.Add( self.SGCList, 1, wx.EXPAND, 0 )
        SGCSizer.Add( self.OK_Button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.SetSizer( SGCSizer )
        SGCSizer.Fit( self )
        SGCSizer.AddGrowableRow( 1 )
        SGCSizer.AddGrowableCol( 0 )
        self.Layout()
        # end wxGlade
        
        self.__Local_Init ()
        
        self.Thaw()
        
    def __Local_Init ( self ):
        self.SGCList.ColumnsToSkip = [0, 1]
        self.SetSize( Config.Config ["SC_Size"] )
        
        if Config.Config ["SC_Position"] [ 0 ] == - 1:
            self.CentreOnScreen ()
        else:
            self.SetPosition( Config.Config ["SC_Position"] )
            
        self.SGCList.InsertColumn ( 0, _( "ROM Name" ) )
        self.SGCList.InsertColumn ( 1, _( "Filename" ) )
        self.SGCList.InsertColumn ( 2, _( "Comment" ) )
        
        self.Bind( wx.EVT_SIZE, self.On_Window_Size )
        self.Bind( wx.EVT_MOVE, self.On_Window_Move )
        self.Bind( wx.EVT_LIST_COL_END_DRAG, self.OnColResized, self.SGCList )

    def On_Window_Size ( self, event ):
        Config.Config ["SC_Size"] = self.GetSize()
        event.Skip ()
    
    def On_Window_Move ( self, event ):
        Config.Config ["SC_Position"] = self.GetScreenPosition()
        event.Skip ()

    def OnColResized ( self, event ):
        ColNum = event.Column
        Config.Config ["SC_Col_Sizes"][ ColNum ] = self.SGCList.GetColumnWidth( ColNum )
        event.Skip()

    def Populate ( self, ROMS, SaveGameShelve ):
        self.ROMS = ROMS
        self.ROMS.reverse()
        self.SaveGameShelve = SaveGameShelve
        Count = 0
        for ROM in self.ROMS:
            index = self.SGCList.InsertStringItem ( sys.maxint, ROM.ROM_File )
            try:
                self.SGCList.SetStringItem ( index, 1, ROM.Name_On_Device )
            except:
                pass
            self.SGCList.SetStringItem ( index, 2, "" )
            self.SGCList.SetItemData( index, Count )
            Count += 1

        self.SGCList.SetColumnWidth( 0, wx.LIST_AUTOSIZE )
        self.SGCList.SetColumnWidth( 1, wx.LIST_AUTOSIZE )
        self.SGCList.SetColumnWidth( 2, 10 )
        self.SGCList.SetColumnWidth ( 0, self.SGCList.GetColumnWidth( 0 ) + 5 )
        
        self.SGCList.SetFocus()
        self.SGCList.Focus( 0 )
        self.SGCList.SetItemState( 0, wx.LIST_STATE_FOCUSED | wx.LIST_STATE_SELECTED, wx.LIST_STATE_FOCUSED | wx.LIST_STATE_SELECTED )

        self.SGCList.Bind ( wx.EVT_CHAR, self.On_List_KeyDown )
        
    def On_List_KeyDown( self, event ):
        if event.GetUnicodeKey() == 13: # Return
            self.SGCList.col_locs = [0]
            loc = 0
            for n in range( self.SGCList.GetColumnCount() ):
                loc = loc + self.SGCList.GetColumnWidth( n )
                self.SGCList.col_locs.append( loc )

            self.SGCList.OpenEditor( 2, self.SGCList.GetFirstSelected() )
        else:
            event.Skip ()

    def On_OK( self, event ): # wxGlade: cSaveGameComments.<event_handler>
        Count = 0
        Dups = []
        while Count < self.SGCList.GetItemCount():
            KeyCount = 1
            MyKey = str ( self.ROMS[self.SGCList.GetItemData( Count )].ROM_CRC )
            MyKey = MyKey + "%03d" % KeyCount
            while MyKey in Dups:
                KeyCount += 1
                MyKey = str ( self.ROMS[self.SGCList.GetItemData( Count )].ROM_CRC )
                MyKey = MyKey + "%03d" % KeyCount
            Dups.append( MyKey )
                
            Comment = self.SGCList.GetItem( Count, 2 ).Text
            
            if Comment != "":
                self.SaveGameShelve [ MyKey ] = Comment
            else:
                try:
                    del ( self.SaveGameShelve [ MyKey ] )
                except:
                    pass
            self.SaveGameShelve.sync ()
            Count += 1
            
        self.Close ()

# end of class cSaveGameComments
