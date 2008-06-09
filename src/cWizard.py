# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.5 on Fri Aug 31 14:25:52 2007 from C:\Documents and Settings\Rich\workspace\WizardTest\WizardTest.wxg

import wx
import wx.wizard as wiz
import wx.lib.filebrowsebutton as filebrowse
import os
import sys

import Config
import GFX

# begin wxGlade: dependencies
# end wxGlade

class cWizard:
    def __init__( self, parent ):
        self.parent = parent
        
    def RunWizard ( self ):
        Wizard = wiz.Wizard( self.parent, -1, "RToolDS Setup Wizard", GFX.getGFX_WizardBitmap(), style=wx.DEFAULT_DIALOG_STYLE|wx.SYSTEM_MENU|wx.CLOSE_BOX )

        Page1 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 1/7" )
        Page2 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 2/7" )
        Page3 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 3/7" )
        Page4 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 4/7" )
        Page5 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 5/7" )
        Page6 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 6/7" )
        Page7 = TitledPage ( Wizard, _( "RToolDS Setup - Page" ) + " 7/7" )

# dialogTitle = _("Select Device Directory") + " : ", labelText = _("Device") + " : ")
        
        Page1.sizer.Add( wx.StaticText( Page1, -1, "Welcome to RToolDS Initial Configuration\n" ) )
        Page1.sizer.Add( wx.StaticText ( Page1, -1, _( "Please Select Your ROM Directory :" ) ) )
        self.ROM_Path = filebrowse.DirBrowseButton ( Page1, -1, labelText = "", dialogTitle = _("Select ROMs Directory") + " : ", newDirectory = True )
        Page1.sizer.Add ( self.ROM_Path, 0, wx.EXPAND|wx.TOP, 10 )
        Page1.sizer.Add ( wx.StaticText ( Page1, -1, "\n" + _( "RToolDS accepts Uncompressed, Zip, 7-Zip and RAR archived ROM files." ) ) )

        Page2.sizer.Add ( wx.StaticText ( Page2, -1, _( "Select a Default Save Game Database Directory :" ) ) )
        self.Save_Path = filebrowse.DirBrowseButton ( Page2, -1, labelText = "", newDirectory=True, dialogTitle = _("Select Save Game Database Directory") + " : " )
        self.Save_Path.SetValue( os.path.join ( os.getcwd(), "cache", "saves" ) )
        Page2.sizer.Add ( self.Save_Path, 0, wx.EXPAND|wx.TOP, 10 )
        Page2.sizer.Add ( wx.StaticText ( Page2, -1, "\n" + _("Note: Do not select a previous linker device save directory")))
        Page2.sizer.Add ( wx.StaticText ( Page2, -1, _("when choosing a location! Previous linker device saves will")))
        Page2.sizer.Add ( wx.StaticText ( Page2, -1, _("need to be imported within RToolDS before use, and any current")))
        Page2.sizer.Add ( wx.StaticText ( Page2, -1, _("saves within the chosen directory will not be automatically detected." ) ) )
        
        Page3.sizer.Add ( wx.StaticText ( Page3, -1, _( "Select a Default Image Directory :" ) ) )
#        Page3.sizer.Add ( wx.StaticText ( Page3, -1, _( "(It is Safe to Keep the Default)" ) ) )
        self.Image_Path = filebrowse.DirBrowseButton ( Page3, -1, labelText = "", newDirectory=True, dialogTitle = _("Select Images Directory") + " : " )
        self.Image_Path.SetValue( os.path.join ( os.getcwd(), "cache", "img" ) )
        Page3.sizer.Add ( self.Image_Path, 0, wx.EXPAND|wx.TOP, 10 )
        Page3.sizer.Add ( wx.StaticText ( Page3, -1, "\n" + _("Select a Default NFO Directory :" ) ) )
        self.NFO_Path = filebrowse.DirBrowseButton ( Page3, -1, labelText = "", newDirectory=True, dialogTitle = _("Select NFO Directory") + " : " )
        self.NFO_Path.SetValue( os.path.join ( os.getcwd(), "cache", "nfo" ) )
        Page3.sizer.Add ( self.NFO_Path, 0, wx.EXPAND|wx.TOP, 10 )
        Page3.sizer.Add ( wx.StaticText ( Page3, -1, "\n" + _( "Note: Keeping the default directories is recommended.")))
        Page3.sizer.Add ( wx.StaticText ( Page3, -1, _( "Directories will contain ROM images and NFO files,")))
        Page3.sizer.Add ( wx.StaticText ( Page3, -1, _( "downloaded during the update process, which are associated")))
        Page3.sizer.Add ( wx.StaticText ( Page3, -1, _( "with your ROM collection." ) ) )

        self.Use_Trimmed = wx.RadioBox ( Page4, -1, _( 'Enable ROM Trimming by default?' ), choices = [ _( 'No' ), _( 'Yes' ) ] )
        self.Use_Trimmed.SetStringSelection( _( "Yes" ) )
        Page4.sizer.Add ( self.Use_Trimmed )
        Page4.sizer.Add ( wx.StaticText( Page4, -1, "\n" + _( "Enabling this option saves memory, as all ROM files are" ) ) )
        Page4.sizer.Add ( wx.StaticText( Page4, -1, _( "compressed before being copied to the device." ) ) )

        self.DLGFX = wx.RadioBox ( Page5, -1, _( 'Update Image and NFO Database upon initial start-up?' ), choices = [ _( 'No' ), _( 'Yes' ) ] )
        self.DLGFX.SetStringSelection( _( "No" ) )
        Page5.sizer.Add ( self.DLGFX )
        Page5.sizer.Add ( wx.StaticText( Page5, -1, "\n" + _( "Warning: This process will take a long time and requires")))
        Page5.sizer.Add ( wx.StaticText( Page5, -1, _("an Internet connection! This process includes updating Images and")))
        Page5.sizer.Add ( wx.StaticText( Page5, -1, _("NFO files associated with your ROM collection." ) ) )

        self.Find_Unknown = wx.RadioBox ( Page6, -1, _( 'Enable Unknown/Homebrew ROM File Detection?' ), choices = [ _( 'No' ), _( 'Yes' ) ] )
        self.Find_Unknown.SetStringSelection( _( "Yes" ) )
        Page6.sizer.Add ( self.Find_Unknown )
        Page6.sizer.Add ( wx.StaticText( Page6, -1, "\n" + _( "Enabling this option allows RToolDS to detect ROMs which are not")))
        Page6.sizer.Add ( wx.StaticText( Page6, -1, _("categorised in our database. This option is recommended and is required")))
        Page6.sizer.Add ( wx.StaticText( Page6, -1, _("to detect newly released ROMs and uncategorised homebrew files." ) ) )

        Page7.sizer.Add ( wx.StaticText ( Page7, -1, _( "Select Your Linker Device Drive :" ) ))
        self.Device_Path = filebrowse.DirBrowseButton ( Page7, -1, labelText = "", dialogTitle = _("Select Device Directory") + " : ", newDirectory = True )
        Page7.sizer.Add ( self.Device_Path, 0, wx.EXPAND|wx.TOP, 10 )
        Page7.sizer.Add ( wx.StaticText (Page7, -1, "\n" + _("Select Your Linker Device Type :")))
        self.Default_Device = wx.Choice ( Page7, -1, choices = [] )
        for Device in Config.Config ["Devices"]:
            if Device[2] != "":
                self.Default_Device.Append (Device[2])
        Page7.sizer.Add ( self.Default_Device, 0, wx.EXPAND|wx.TOP|wx.LEFT, 10 )
        Page7.sizer.Add ( wx.StaticText( Page7, -1, "\n" + _( "Note: You can leave these options blank and select them at a")))
        Page7.sizer.Add ( wx.StaticText( Page7, -1, _("later time from the options menu. Completing these selections enables")))
        Page7.sizer.Add ( wx.StaticText( Page7, -1, _("enhanced RToolDS integration with your linker device." ) ) )

        Wizard.FitToPage( Page1 )
        
        wiz.WizardPageSimple_Chain( Page1, Page2 )
        wiz.WizardPageSimple_Chain( Page2, Page3 )
        wiz.WizardPageSimple_Chain( Page3, Page4 )
        wiz.WizardPageSimple_Chain( Page4, Page5 )
        wiz.WizardPageSimple_Chain( Page5, Page6 )
        wiz.WizardPageSimple_Chain( Page6, Page7 )

        Wizard.GetPageAreaSizer().Add( Page1 )
        
        Wizard.Fit()
        Wizard.Layout()
        
        self.Wizard = Wizard
        self.Page1 = Page1
        self.Page2 = Page2
        self.Page3 = Page3
        self.Page4 = Page4
        self.Page5 = Page5
        self.Page6 = Page6
        self.Page7 = Page7

        Wizard.Bind(wiz.EVT_WIZARD_PAGE_CHANGING, self.OnWizPageChanging)

        Result = Wizard.RunWizard( Page1 )

        del ( Wizard )
        
        return Result
        
    def GetResult( self, Value ):
            if Value == "ROM_Path":
                return self.ROM_Path.GetValue()
            elif Value == "Save_Path":
                return self.Save_Path.GetValue()
            elif Value == "Image_Path":
                return self.Image_Path.GetValue()
            elif Value == "NFO_Path":
                return self.NFO_Path.GetValue()
            elif Value == "Use_Trimmed":
                if self.Use_Trimmed.GetStringSelection() == _( "Yes" ):
                    return True
                else:
                    return False
            elif Value == "DLGFX":
                if self.DLGFX.GetStringSelection() == _( "Yes" ):
                    return True
                else:
                    return False
            elif Value == "Find_Unknown":
                if self.Find_Unknown.GetStringSelection() == _( "Yes" ):
                    return True
                else:
                    return False
            elif Value == "Device_Path":
                return self.Device_Path.GetValue()
            elif Value == "Default_Device":
                if self.Default_Device.GetSelection() == wx.NOT_FOUND:
                    return Config.Config ["Devices"][0]
                else:
                    a = self.Default_Device.GetStringSelection()
                    for Device in Config.Config ["Devices"]:
                        if Device[2] == a:
                            return Device[0]
                return Config.Config ["Devices"][0]

    def OnWizPageChanging (self, event):
        if event.Page == self.Page1:
            if os.path.isdir (self.ROM_Path.GetValue()) == False or len (self.ROM_Path.GetValue()) < 3 or (sys.platform == "win32" and (self.ROM_Path.GetValue()[2] != "\\") and (self.ROM_Path.GetValue()[0] != "\\" and self.ROM_Path.GetValue()[1] != "\\")):
                wx.MessageBox( _('ROM Path is Invalid.\n\nPlease Select a Valid Directory.'), _('Error'), wx.OK| wx.ICON_ERROR )
                event.Veto()

        if event.Page == self.Page2:
            if os.path.isdir (self.Save_Path.GetValue()) == False or len (self.Save_Path.GetValue()) < 3 or (sys.platform == "win32" and (self.Save_Path.GetValue()[2] != "\\") and (self.Save_Path.GetValue()[0] != "\\" and self.Save_Path.GetValue()[1] != "\\")):
                wx.MessageBox( _('Save Path is Invalid.\n\nPlease Select a Valid Directory.'), _('Error'), wx.OK| wx.ICON_ERROR )
                event.Veto()

        if event.Page == self.Page3:
            if os.path.isdir (self.Image_Path.GetValue()) == False or len (self.Image_Path.GetValue()) < 3 or (sys.platform == "win32" and (self.Image_Path.GetValue()[2] != "\\") and (self.Image_Path.GetValue()[0] != "\\" and self.Image_Path.GetValue()[1] != "\\")):
                wx.MessageBox( _('Image Path is Invalid.\n\nPlease Select a Valid Directory.'), _('Error'), wx.OK| wx.ICON_ERROR )
                event.Veto()
            if os.path.isdir (self.NFO_Path.GetValue()) == False or len (self.NFO_Path.GetValue()) < 3 or (sys.platform == "win32" and (self.NFO_Path.GetValue()[2] != "\\") and (self.NFO_Path.GetValue()[0] != "\\" and self.NFO_Path.GetValue()[1] != "\\")):
                wx.MessageBox( _('NFO Path is Invalid.\n\nPlease Select a Valid Directory.'), _('Error'), wx.OK| wx.ICON_ERROR )
                event.Veto()

def makePageTitle( wizPg, title ):
        sizer = wx.BoxSizer( wx.VERTICAL )
        wizPg.SetSizer( sizer )
        title = wx.StaticText( wizPg, -1, title )
        title.SetFont( wx.Font( 18, wx.SWISS, wx.NORMAL, wx.BOLD ) )
        sizer.Add( title, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
        sizer.Add( wx.StaticLine( wizPg, -1 ), 0, wx.EXPAND|wx.ALL, 5 )
        return sizer
    
class TitledPage( wiz.WizardPageSimple ):
    def __init__( self, parent, title ):
        wiz.WizardPageSimple.__init__( self, parent )
        self.sizer = makePageTitle( self, title )
        self.Layout()

