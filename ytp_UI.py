# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.calendar
import wx.richtext
import wx.grid

m_mniExitId = 1000
m_mniAboutId = 1001

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"YTPMemo", pos = wx.DefaultPosition, size = wx.Size( 763,657 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetExtraStyle( wx.FRAME_EX_CONTEXTHELP )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menubar.Hide()
		
		self.m_mnFile = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_mnFile, wx.ID_ANY, u"Show Table", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_menuItem4 )
		
		self.m_ReadFile = wx.MenuItem( self.m_mnFile, wx.ID_ANY, u"ReadFile2DataBase", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_ReadFile )
		
		self.m_mnFile.AppendSeparator()
		
		self.m_mniExit = wx.MenuItem( self.m_mnFile, m_mniExitId, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniExit )
		self.m_mniExit.Enable( False )
		
		self.m_menubar.Append( self.m_mnFile, u"&File" ) 
		
		self.m_mnHelp = wx.Menu()
		self.m_mniAbout = wx.MenuItem( self.m_mnHelp, m_mniAboutId, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnHelp.AppendItem( self.m_mniAbout )
		
		self.m_menubar.Append( self.m_mnHelp, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"images/good.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer5.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Income", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_tcIncome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		gSizer3.Add( self.m_tcIncome, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Spend", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText1.Wrap( -1 )
		gSizer3.Add( self.m_staticText1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_tcSpend = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		gSizer3.Add( self.m_tcSpend, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( gSizer3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_calendar1 = wx.calendar.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.calendar.CAL_MONDAY_FIRST|wx.calendar.CAL_SHOW_HOLIDAYS )
		bSizer5.Add( self.m_calendar1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( bSizer5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.Add( bSizer4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_InputArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 750,300 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer41.Add( self.m_InputArea, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 750,300 ), wx.TE_PROCESS_TAB|wx.HSCROLL|wx.NO_BORDER|wx.TAB_TRAVERSAL|wx.VSCROLL|wx.WANTS_CHARS )
		bSizer41.Add( self.m_richText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_MemoTable = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 750,300 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_gridMemo = wx.grid.Grid( self.m_MemoTable, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,285 ), 0 )
		
		# Grid
		self.m_gridMemo.CreateGrid( 5, 4 )
		self.m_gridMemo.EnableEditing( True )
		self.m_gridMemo.EnableGridLines( True )
		self.m_gridMemo.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_gridMemo.EnableDragGridSize( False )
		self.m_gridMemo.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridMemo.SetColSize( 0, 40 )
		self.m_gridMemo.SetColSize( 1, 48 )
		self.m_gridMemo.SetColSize( 2, 45 )
		self.m_gridMemo.SetColSize( 3, 562 )
		self.m_gridMemo.EnableDragColMove( False )
		self.m_gridMemo.EnableDragColSize( True )
		self.m_gridMemo.SetColLabelSize( 30 )
		self.m_gridMemo.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridMemo.AutoSizeRows()
		self.m_gridMemo.EnableDragRowSize( True )
		self.m_gridMemo.SetRowLabelSize( 20 )
		self.m_gridMemo.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridMemo.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer10.Add( self.m_gridMemo, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.m_MemoTable.SetSizer( bSizer10 )
		self.m_MemoTable.Layout()
		bSizer41.Add( self.m_MemoTable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( bSizer41, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_hyperlink2 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"YuanThaiPavilion fb", u"https://www.facebook.com/YunThaiPavilion", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer3.Add( self.m_hyperlink2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_DeleteMemo = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"images/_del2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER|wx.TRANSPARENT_WINDOW )
		
		self.m_DeleteMemo.SetBitmapHover( wx.Bitmap( u"images/del2.png", wx.BITMAP_TYPE_ANY ) )
		self.m_DeleteMemo.SetExtraStyle( wx.WS_EX_TRANSIENT )
		self.m_DeleteMemo.SetToolTipString( u"Delete Select Date (F4)" )
		
		bSizer3.Add( self.m_DeleteMemo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 0, 0, 5 )
		
		self.m_Exit = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"images/_exit.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_Exit.SetBitmapHover( wx.Bitmap( u"images/exit.png", wx.BITMAP_TYPE_ANY ) )
		self.m_Exit.SetToolTipString( u"Exit program (Exit)" )
		
		bSizer3.Add( self.m_Exit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_mStatics = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"images/_statistics.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		
		self.m_mStatics.SetBitmapHover( wx.Bitmap( u"images/statistics.png", wx.BITMAP_TYPE_ANY ) )
		self.m_mStatics.SetDefault() 
		self.m_mStatics.SetExtraStyle( wx.WS_EX_TRANSIENT )
		self.m_mStatics.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_mStatics.SetToolTipString( u"Show Static (F3)" )
		
		bSizer3.Add( self.m_mStatics, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_btRun = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"images/_save.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_btRun.SetBitmapHover( wx.Bitmap( u"images/save.png", wx.BITMAP_TYPE_ANY ) )
		self.m_btRun.SetToolTipString( u"Save Money (F2)" )
		
		bSizer3.Add( self.m_btRun, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_showMemo = wx.CheckBox( self, wx.ID_ANY, u"Show All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_showMemo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer7, 0, 0, 5 )
		
		
		bSizer2.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.On_showTable, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.On_ReadFile2Database, id = self.m_ReadFile.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = self.m_mniExit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniAboutClick, id = self.m_mniAbout.GetId() )
		self.m_calendar1.Bind( wx.calendar.EVT_CALENDAR_DAY, self.on_CalDay )
		self.m_DeleteMemo.Bind( wx.EVT_BUTTON, self.On_DeleteMemo )
		self.m_Exit.Bind( wx.EVT_BUTTON, self.m_btExit )
		self.m_mStatics.Bind( wx.EVT_BUTTON, self.On_StaticClick )
		self.m_btRun.Bind( wx.EVT_BUTTON, self.m_btSave )
		self.m_showMemo.Bind( wx.EVT_CHECKBOX, self.On_showTable )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def On_showTable( self, event ):
		event.Skip()
	
	def On_ReadFile2Database( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	
	def m_mniAboutClick( self, event ):
		event.Skip()
	
	def on_CalDay( self, event ):
		event.Skip()
	
	def On_DeleteMemo( self, event ):
		event.Skip()
	
	def m_btExit( self, event ):
		event.Skip()
	
	def On_StaticClick( self, event ):
		event.Skip()
	
	def m_btSave( self, event ):
		event.Skip()
	
	

###########################################################################
## Class aboutDlg
###########################################################################

class aboutDlg ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer9.Add( self.m_staticText4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

