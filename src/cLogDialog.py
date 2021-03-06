# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.1 on Mon Nov 05 10:01:05 2007

import wx
import os
import glob

import Utils
from ROMS import MyROMS
import Config

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class cLogDialog( wx.Dialog ):
    def __init__( self, *args, **kwds ):
        self.Auto_Close = kwds["Auto_Close"]
        self.Todo = kwds["Todo"]
        del kwds["Auto_Close"]
        del kwds["Todo"]

        if Config.Config ["AutoCloseUpdate"]:
            self.Auto_Close = True
        
        # begin wxGlade: cLogDialog.__init__
        kwds["style"] = wx.CAPTION | wx.RESIZE_BORDER | wx.THICK_FRAME
        wx.Dialog.__init__( self, *args, **kwds )
        self.Log = wx.TextCtrl( self, - 1, "", style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP )
        self.OK_Button = wx.Button( self, - 1, _( "OK" ) )

        self.__set_properties()
        self.__do_layout()

        self.Bind( wx.EVT_BUTTON, self.On_OK, self.OK_Button )
        # end wxGlade
        
        self.Bind( wx.EVT_SIZE, self.On_Window_Size )
        self.Bind( wx.EVT_MOVE, self.On_Window_Move )

        self.Aborted = False
        self.OK_Button.SetLabel( _( "Abort" ) )
        
        wx.FutureCall( 300, self.Run )

    def __set_properties( self ):
        # begin wxGlade: cLogDialog.__set_properties
        self.SetTitle( _( "Updating..." ) )
        self.SetSize( ( 500, 400 ) )
        self.SetFocus()
        # end wxGlade

    def __do_layout( self ):
        self.Freeze()
        # begin wxGlade: cLogDialog.__do_layout
        Log_Sizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        Log_Sizer.Add( self.Log, 0, wx.ALL | wx.EXPAND, 5 )
        Log_Sizer.Add( self.OK_Button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.SetSizer( Log_Sizer )
        Log_Sizer.AddGrowableRow( 0 )
        Log_Sizer.AddGrowableCol( 0 )
        self.Layout()
        self.Centre()
        # end wxGlade
        
        self.SetSize( Config.Config ["Log_Size"] )
        if Config.Config ["Log_Position"] [ 0 ] == - 1:
            self.CentreOnScreen ()
        else:
            self.SetPosition( Config.Config ["Log_Position"] )        

        self.Thaw()

    def On_Window_Size ( self, event ):
        Config.Config ["Log_Size"] = self.GetSize()
        event.Skip ()
    
    def On_Window_Move ( self, event ):
        Config.Config ["Log_Position"] = self.GetScreenPosition()
        event.Skip ()

    def On_OK( self, event ): # wxGlade: cLogDialog.<event_handler>
        if self.OK_Button.GetLabel() == _( "Abort" ):
            self.Aborted = True
            self.Todo.append ( "Failed" )
        else:
            self.Close()
        
    def Run ( self ):
        if "Master_List" in self.Todo and "Failed" not in self.Todo:
            self.Update_Master_List ()
        if "ROM_List" in self.Todo and "Failed" not in self.Todo:
            self.Update_ROM_List ()
        if "GFX" in self.Todo and "Failed" not in self.Todo:
            self.Update_GFX ()
            
        self.OK_Button.SetLabel ( _( "OK" ) )
        
        if self.Auto_Close:
            self.Close()

    def Update_Master_List ( self ):
        self.Log.AppendText( _( "Checking for Database Updates" ) + " ... " )
        wx.Yield()
        
        Version = Utils.Fetch_Master_List_Version()
        if Version > MyROMS.Master_List_XML_Version:
            self.Log.AppendText( _( "Updates Available" ) + "\n\n" )
            wx.Yield()
       
            self.Log.AppendText ( _( "Updating Database" ) + " ... " ) 
            wx.Yield()
            
            if Utils.Fetch_Master_List() == False:
                self.Log.AppendText( _( "Failed" ) + "\n\n" )
                self.Todo.append ( "Failed" )
                wx.Yield()
                return
            
            self.Log.AppendText( _( "Success" ) + "\n\n" + _( "Merging Updated Database" ) + " ... " )
            wx.Yield()
            if MyROMS.Load_Master_List ():
                self.Log.AppendText( _( "Success" ) + "\n\n" )
                self.Todo.append ( "ROM_List" )
                wx.Yield()
            else:
                self.Log.AppendText( _( "Failed" ) + "\n" )
                self.Todo.append ( "Failed" )
                wx.Yield()
        elif Version == - 1:
            self.Log.AppendText( _( "Internet Connection Error" ) + "\n\n" )
        else:
            self.Log.AppendText( _( "No Updates Available" ) + "\n\n" )
        wx.Yield()
        
    def Update_ROM_List ( self ):
        self.Log.AppendText( _( "Finalising Database" ) + " ... " )
        wx.Yield()

        MyROMS.Start_ROM_Find ()
        
        self.Log.AppendText ( _( "Completed" ) + "\n\n" )
        wx.Yield()
            
        self.Log.AppendText( _( "Finding New ROMs" ) + " ...\n\n" )
        wx.Yield()

        ROMS_Found = False
        if Config.Config ["Parse_Subdirs"] == False:
            SearchStr = os.path.join ( Config.Config ["ROM_Path"], "*" )
            DirList = glob.glob ( SearchStr )
            for Filename in DirList:
                Title = MyROMS.Process_ROM( Filename )
                if Title != []:
                    for a in Title:
                        if a != "":
                            self.Log.AppendText ( a + "\n" )
                            wx.Yield()
                    ROMS_Found = True
                wx.Yield()
                if self.Aborted:
                    break
        else:
            for root, dummy_dirs, files in os.walk( Config.Config ["ROM_Path"] ):
                for name in files:
                    Title = MyROMS.Process_ROM( os.path.join( root, name ) )
                    if Title != []:
                        for a in Title:
                            if a != "":
                                self.Log.AppendText ( a + "\n" )
                                wx.Yield()
                        ROMS_Found = True
                    wx.Yield()
                    if self.Aborted:
                        break
 
        MyROMS.Close_ROM_Find ()
                
        if self.Aborted:
            if ROMS_Found:
                self.Log.AppendText( "\n" + _( "Aborted Update" ) + ".\n\n" )
            else:
                self.Log.AppendText( _( "Aborted Update" ) + ".\n\n" )
            self.Todo.append ( "Failed" )
            wx.Yield()
            MyROMS.Load_Master_List ( AltName = True )
            MyROMS.Save_Master_List ()
        else:
            MyROMS.Sort_Current_List ()
            MyROMS.Populate_Current_List ()
            MyROMS.Save_Master_List ()
            if ROMS_Found:
                self.Log.AppendText( "\n" + _( "Completed" ) + ".\n\n" )
            else:
                self.Log.AppendText( _( "Completed" ) + ".\n\n" )
            wx.Yield()
        try:
            os.unlink ( "RToolDS_Master_List.dat.bak" )
        except:
            pass

    def Update_GFX ( self ):
        self.Log.AppendText( _( "Updating Image/NFO Database" ) + " ...\n\n" )
        wx.Yield()

        MyROMS.Process_All = True

        for ROM in MyROMS:
            if ROM.Comment [0].upper() != "U" and ROM.Found == True:
                ToDL = []
                self.Log.AppendText ( "%s ... " % ( ROM.Title ) )
                
                icoFilename = os.path.join ( Config.Config ["Image_Path"], "%04d.png" % ROM.Image_Number )
                im1Filename = os.path.join ( Config.Config ["Image_Path"], "%04da.png" % ROM.Image_Number )
                im2Filename = os.path.join ( Config.Config ["Image_Path"], "%04db.png" % ROM.Image_Number )
                nfoFilename = os.path.join ( Config.Config ["NFO_Path"], "%04d.nfo" % ROM.Image_Number )
                
                if not Utils.Check_CRC ( icoFilename, ROM.Ico_CRC ):
                    ToDL.append ( "ICO" )
                if not Utils.Check_CRC ( im1Filename, ROM.Im1_CRC ):
                    ToDL.append ( "IM1" )
                if not Utils.Check_CRC ( im2Filename, ROM.Im2_CRC ):
                    ToDL.append ( "IM2" )
                if not Utils.Check_CRC ( nfoFilename, ROM.Nfo_CRC ):
                    ToDL.append ( "NFO" )
                    
                if ToDL != []:
                    self.Log.AppendText( _( "Downloading ... " ) )
                    wx.Yield()
                
                    res = 0
                    if "ICO" in ToDL:
                        MyUrl = "%s%s/%04d.png" % ( Config.Config["icURL"], Utils.Directory_Range ( ROM.Image_Number ), ROM.Image_Number )
                        res += Utils.GetFromWeb ( MyUrl, icoFilename )
                    if "IM1" in ToDL:
                        MyUrl = "%s%s/%da.png" % ( Config.Config["imURL"], Utils.Directory_Range ( ROM.Image_Number ), ROM.Image_Number )
                        res += Utils.GetFromWeb ( MyUrl, im1Filename )
                    if "IM2" in ToDL:
                        MyUrl = "%s%s/%db.png" % ( Config.Config["imURL"], Utils.Directory_Range ( ROM.Image_Number ), ROM.Image_Number )
                        res += Utils.GetFromWeb ( MyUrl, im2Filename )
                    if "NFO" in ToDL:
                        MyUrl = "http://www.advanscene.com/offline/nfo/NDSnfo/%s/%04d.nfo" % ( Utils.Directory_Range ( ROM.Image_Number ), ROM.Image_Number )
                        res += Utils.GetFromWeb ( MyUrl, nfoFilename )
                    
                    if res == 0:
                        Display = _( "OK" )
                    else:
                        Display = _( "Failed" )
                            
                    self.Log.AppendText( Display + "\n" )
                    wx.Yield()
                else:
                    self.Log.AppendText( _( "OK" ) + "\n" )
                    wx.Yield()

            wx.Yield()
            if self.Aborted:
                break
                
        if self.Aborted:
            self.Log.AppendText( "\n" + _( "Aborted Update" ) + ".\n\n" )
            self.Todo.append ( "Failed" )
            wx.Yield()
        else:
            self.Log.AppendText( "\n" + _( "Completed" ) + ".\n\n" )
            wx.Yield()

        MyROMS.Process_All = False

# end of class cLogDialog
