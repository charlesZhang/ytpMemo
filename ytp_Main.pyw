# -*- coding: utf-8 -*- 

###########################################################################
## ytpMemo
## http://www.wxformbuilder.org/
##
## Charles Chang
###########################################################################

import sys, os
import time
import re
import wx
import calendar
import wx.lib.hyperlink as hyperlink
import logging
import sqlite3
from datetime import date
from datetime import datetime
import  wx.grid as gridlib
import random
import wx.richtext as rt
import pythoncom, pyHook 
import csv

            
import images
from wx.lib.embeddedimage import PyEmbeddedImage

import ytp_UI

logging.basicConfig(filename='YTPMLog.log',format='%(asctime)s:%(message)s',  level=logging.INFO)
execfile("config.ini")
    
###########################################################################
## Implementing MainFrameBase
###########################################################################

class ytp_Main( ytp_UI.MainFrameBase ):

            
    def __init__( self, parent ):
        ytp_UI.MainFrameBase.__init__( self, parent )
        self.addConfigItems()
        self.InCome =""
        self.Spend =""
        self.parent = parent

        self.m_InputArea.Show()
        self.m_MemoTable.Hide()
        self.m_richText1.Hide()

        self.conn = sqlite3.connect("ytp_Database.db")
        self.cursor = self.conn.cursor()

        img = PyEmbeddedImage(images._bye).GetBitmap()
        self.m_Exit.SetBitmapHover( img )

        img = PyEmbeddedImage(images._celebration).GetBitmap()
        self.m_bitmap1.SetBitmap( img )
        self.LoadDay()

        self.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
        self.m_richText1.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
        self.m_InputArea.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
        self.m_MemoTable.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
        self.m_tcIncome.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
        self.m_tcSpend.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
        self.m_calendar1.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)
 
    def onButtonKeyEvent(self, event):
        # HotKey event
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.m_btExit(event)
        if keycode == wx.WXK_F1:
            self.On_StaticClick(event)
        if keycode == wx.WXK_F2:
            self.m_btSave(event)
        if keycode == wx.WXK_F4:
            self.On_DeleteMemo(event)
        event.Skip()
        
    def addConfigItems( self ):
        box1_title = wx.StaticBox( self.m_InputArea, -1, u"Spends" )
        box2_title = wx.StaticBox( self.m_InputArea, -1, u"Incomes" )
        grid2 = wx.FlexGridSizer( 0, 2, 0, 0)
        grid1 = wx.FlexGridSizer( 0, 4, 0, 0)
        box1 = wx.StaticBoxSizer( box1_title, wx.VERTICAL)
        box2 = wx.StaticBoxSizer( box2_title, wx.VERTICAL)
        self.Spend_List = []
        self.Income_List = []

        lb ,tb = [], []
        for i in range(0, len(OutList)):
            lb.append(wx.StaticText(self.m_InputArea, -1, unicode(OutList[i],"utf8")))
            tb.append(wx.TextCtrl( self.m_InputArea, -1, "" ))
            self.Spend_List.append((lb[i], tb[i]))
                 
        for l, t in self.Spend_List:
            grid1.Add( l, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid1.Add( t, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            t.SetBackgroundColour((255,255,224))

            # Setup event handling and initial state for controls:
            self.Bind(wx.EVT_TEXT, self.OnSpend,t)
            self.Bind(wx.EVT_SET_FOCUS, self.OnSpend,t)
            self.Bind(wx.EVT_KILL_FOCUS, self.OnSpend,t)
            t.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)


        lb ,tb = [], []
        for i in range(0, len(InList)):
            lb.append(wx.StaticText(self.m_InputArea, -1, unicode(InList[i],"utf8")))
            tb.append(wx.TextCtrl( self.m_InputArea, -1, "" ))
            self.Income_List.append((lb[i], tb[i]))

        for l, t in self.Income_List:
            grid2.Add( l, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid2.Add( t, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            t.SetBackgroundColour((255,255,224))

            # Setup event handling and initial state for controls:
            self.Bind(wx.EVT_TEXT, self.OnIncome,t)
            self.Bind(wx.EVT_SET_FOCUS, self.OnIncome,t)
            self.Bind(wx.EVT_KILL_FOCUS, self.OnIncome,t)
            t.Bind(wx.EVT_KEY_DOWN, self.onButtonKeyEvent)

        box1.Add( grid1, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
        box2.Add( grid2, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )

        border = wx.BoxSizer(wx.HORIZONTAL)
        border.Add(box1, 0, wx.ALL, 10)
        border.Add(box2, 0, wx.ALL, 20)
        self.m_InputArea.SetSizer(border)
        self.m_InputArea.Layout()

#---------------------------------------------------------------------------------
# Handlers for MainFrameBase events.
#---------------------------------------------------------------------------------
    def On_showTable( self, event ):
        # Show all data in current month to grid.
        if self.m_MemoTable.IsShown():
            self.m_showMemo.SetValue(False)
            self.m_InputArea.Show()
            self.m_richText1.Hide()
            self.m_MemoTable.Hide()
            self.m_InputArea.Layout()
            return
        else:
            self.m_showMemo.SetValue(True)
            self.m_InputArea.Hide()
            self.m_richText1.Hide()
            self.m_MemoTable.Show()
            self.m_MemoTable.Layout()
            self.Layout()

        timeStr = str(self.m_calendar1.GetDate())
        dateList  = re.split('/| |\n', timeStr)
        lastDay = calendar.monthrange(int('20%s'%dateList[2]),int(dateList[0]))[1]

        start_date = '%s/01/%s'%(dateList[0], dateList[2])
        end_date = '%s/%s/%s'%(dateList[0], lastDay, dateList[2])
        
        sqlcmd = """
        SELECT * FROM ytpMemo WHERE 
            Date BETWEEN '%s' AND '%s'"""%(start_date, end_date)

        self.cursor.execute(sqlcmd)
        ret = self.cursor.fetchall()

        self.m_gridMemo.DeleteRows(0,31,False)
        self.m_gridMemo.SetColLabelValue(0, "Date")
        self.m_gridMemo.SetColLabelValue(1, "Income")
        self.m_gridMemo.SetColLabelValue(2, "Spend")
        self.m_gridMemo.SetColLabelValue(3, "Notes")
        self.m_gridMemo.AppendRows(lastDay)
        attr = gridlib.GridCellAttr()
        attr.SetAlignment(wx.ALIGN_RIGHT, wx.ALIGN_RIGHT)
        self.m_gridMemo.SetColAttr(1, attr)
        self.m_gridMemo.SetColAttr(2, attr)

        for idx in range(len(ret)):
            try:
                self.m_gridMemo.SetCellValue(idx, 0, ret[idx][0][0:5])
                self.m_gridMemo.SetCellValue(idx, 1, str(ret[idx][1]))
                self.m_gridMemo.SetCellValue(idx, 2, str(ret[idx][2]))
                self.m_gridMemo.SetCellValue(idx, 3, ret[idx][3])
            except:
                pass
        self.m_gridMemo.AutoSizeRows()
    
    def On_ReadFile2Database( self, event ):
        #Read data from file and commit to database
        #Each file contains single month data only. 

        timeStr = str(self.m_calendar1.GetDate())
        date  = timeStr.split(' ')[0]
        cMonth =date.split('/')[0]
        
        try:
            #Open csv file with file name is current month, ex 09.csv
            with open('.\..\data\%s.csv'%cMonth, 'rb') as csvfile:
    			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

   			for row in spamreader:
   				memoStr = ''
   				inCome = 0
   				Spend = 0
   				
   				if row[0]=='Date':
   					title = row
   				else:
                    # Replace day in date string '12/XX/13' with XX = 01 ~ 31
   					data =  [x if x != '' else '0' for x in row]
   					if len(data[0])==1: data[0] = '0' + data[0]
   					newDate =re.sub(r'/[0-9]*/','/'+data[0]+'/',date)
                       
   					inCome = int(data[1])
   					Spend = int(sum([int(eval(c)) for c in data[2:len(data)-1]]))
   					
   					idx = 2
   					for x in data[2:len(data)-1]:
   						if x != '0':
   							memoStr = memoStr + unicode(OutList[idx-2],"utf8")+": "+ x + "; "
   						idx = idx+1
   						
   				if inCome or Spend:
   					try:
   						self.cursor.execute("INSERT INTO ytpMemo VALUES ('%s', %d, %d, '%s')"%(newDate, Spend, inCome, memoStr))
   					except:
   						dlg = wx.MessageDialog(self,
   							"Data alredy exist!\n Do you really want to overwrite existing data?",
   							"Confirm", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
   						result = dlg.ShowModal()
   						dlg.Destroy()
   						if result == wx.ID_OK:
   							sqlcmd = """
   							UPDATE ytpMemo 
   							SET Income = '%d', Spend = '%d', Memo = '%s' 
   							WHERE Date = '%s'"""%(inCome, Spend, memoStr, newDate)
   							
   							self.cursor.execute(sqlcmd)
   					self.conn.commit()
   					str1 = u"\t%s : Spend: %s\tEarn: %s\tMemo: %s"%(newDate, inCome, Spend, memoStr)
   					logging.info(str1)

            print "Saving data from file to db...done!"
            dlg = wx.MessageDialog(self,
                'Saving data from file to db...Successfully!',
                "Saving Data", wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()
        except IOError:
            os.chdir('.\..\\data\\')
            dlg = wx.MessageDialog(self,
                'Oh dear! "%s\%s.csv" is not exist'%(os.getcwd(),cMonth),
                "Saving Data", wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()
        self.LoadDay()


    def m_mniExitClick( self, event ):
        self.Close()
    
    def m_mniAboutClick( self, event ):
        self.new = ytp_UI.aboutDlg( None )
        self.new.Show()
    
    def LoadDay( self ):

        timeStr = str(self.m_calendar1.GetDate())
        idate  = timeStr.split(' ')[0]

        if random.randint(0,2) == 0:
            img = PyEmbeddedImage(images._ok).GetBitmap()
        elif random.randint(0,2) == 1:
            img = PyEmbeddedImage(images._good).GetBitmap()
        else:
            img = PyEmbeddedImage(images._celebration).GetBitmap()
        self.m_bitmap1.SetBitmap( img )
        
        sqlcmd = """
        SELECT Income, Spend, Memo FROM ytpMemo WHERE 
            Date = '%s'"""%(idate)

        self.cursor.execute(sqlcmd)
        ret = self.cursor.fetchall()

        self.m_richText1.Clear()
        self.m_tcSpend.SetValue('')
        self.m_tcIncome.SetValue('')
        if len(ret):
            self.m_tcSpend.SetValue(str(ret[0][1]))
            self.m_tcIncome.SetValue(str(ret[0][0]))

            self.m_richText1.BeginFontSize(14)
            self.m_richText1.BeginTextColour((125, 125, 0))
            self.m_richText1.WriteText(ret[0][2])
            self.m_richText1.EndTextColour()

        self.Layout()
        
    def on_CalDay( self, event ):
        self.LoadDay()
    
    def m_btExit( self, event ):
        dlg = wx.MessageDialog(self,
            "Do you really want to close this application?",
            "Confirm", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Close()

    def On_DeleteMemo( self, event ):

        timeStr = str(self.m_calendar1.GetDate())
        date  = timeStr.split(' ')[0]

        try:
            dlg = wx.MessageDialog(self,
                "Do you really want to delete existing data?",
                "Confirm", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_OK:
                sqlcmd = """
                DELETE FROM ytpMemo 
                WHERE Date = '%s'"""%(date)

                cursor.execute(sqlcmd)
        except:
            pass
        self.conn.commit()
        self.LoadDay()

    def m_btSave( self, event ):

        timeStr = str(self.m_calendar1.GetDate())
        date  = timeStr.split(' ')[0]
        print date

        try:
            Spend = int(self.m_tcSpend.GetValue())
            inCome = int(self.m_tcIncome.GetValue())
            memo = self.Spend + "\n" + self.InCome
            str1 = u"\t%s : Spend: %s\tEarn: %s\tMemo: %s"%(date, Spend, inCome, memo)
            logging.info(str1)
        except:
            dlg = wx.MessageDialog(self,
                "Please input data first",
                "Saving Data", wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()
            return

        try:
            self.cursor.execute("INSERT INTO ytpMemo VALUES ('%s', %d, %d, '%s')"%(date, Spend, inCome, memo))
        except:
            dlg = wx.MessageDialog(self,
                "Data alredy exist!\n Do you really want to overwrite existing data?",
                "Confirm", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_OK:
                sqlcmd = """
                UPDATE ytpMemo 
                SET Income = '%d', Spend = '%d', Memo = '%s' 
                WHERE Date = '%s'"""%(inCome, Spend, memo, date)

                self.cursor.execute(sqlcmd)
        self.conn.commit()
        dlg = wx.MessageDialog(self,
            "Done",
            "Saving Data", wx.OK)
        result = dlg.ShowModal()
        dlg.Destroy()
        
        # Clear the text boxes.
        for cb, text in self.Income_List:
            text.SetValue("")
        for cb, text in self.Spend_List:
            text.SetValue("")
        self.LoadDay()


    def On_StaticClick( self, event ):
        if self.m_richText1.IsShown():
            self.m_InputArea.Show()
            self.m_MemoTable.Hide()
            self.m_richText1.Hide()
            self.m_richText1.Layout()
            self.Layout()
            return
        else:
            self.m_richText1.Show()
            self.m_MemoTable.Hide()
            self.m_InputArea.Hide()
            self.m_InputArea.Layout()
            
        timeStr = str(self.m_calendar1.GetDate())
        dateList  = re.split('/| |\n', timeStr)
        lastDay = calendar.monthrange(int('20%s'%dateList[2]),int(dateList[0]))[1]
        self.m_richText1.Clear()
        self.m_richText1.BeginFontSize(12)
        self.m_richText1.BeginTextColour((125, 125, 0))
        tmpS = "Month\t\tSpend\t\tEarn\t\tProfit\n"
        self.m_richText1.WriteText(tmpS)
        self.m_richText1.EndTextColour()
        for m in range(12):
            if m <9:
                month = "0%s"%(m + 1)
            else:
                month = "%s"%(m + 1)

            start_date = '%s/01/%s'%(month, dateList[2])
            end_date = '%s/%s/%s'%(month, lastDay, dateList[2])
            
            sqlcmd = """
            SELECT Income, Spend FROM ytpMemo WHERE 
                Date BETWEEN '%s' AND '%s'"""%(start_date, end_date)
    
            self.cursor.execute(sqlcmd)
            ret = self.cursor.fetchall()
    
            spend  =  0
            earn  =  0
            for i in range(len(ret)):
                earn += ret[i][0]
                spend += ret[i][1]

            self.m_richText1.BeginTextColour((0, 255, 255))
            self.m_richText1.WriteText("%s\t\t"%month)
            self.m_richText1.EndTextColour()
            self.m_richText1.BeginTextColour((255, 0, 0))
            self.m_richText1.WriteText("%8d\t\t"%spend)
            self.m_richText1.EndTextColour()
            self.m_richText1.BeginTextColour((0, 0, 255))
            self.m_richText1.WriteText("%8d\t\t"%earn)
            self.m_richText1.EndTextColour()
            self.m_richText1.BeginTextColour((0, 200, 0))
            self.m_richText1.WriteText("%8d\n"%(earn-spend))
            self.m_richText1.EndTextColour()
            
        self.m_richText1.EndFontSize()
        self.Layout()

    def OnSpend( self, event):
        i = 0
        mysum = 0
        self.Spend = ""
        memostr = "( "
        for cb, text in self.Spend_List:
            if text.GetValue():
                text.Enable(True)
                label = unicode(OutList[i],"utf8")
                mystr = text.GetValue()
                try:
                    mysum += eval(mystr)
                except:
                    pass
                
                memostr += label + " : " + mystr + " "
            i += 1
        memostr += ")"
        self.Spend += memostr

        self.m_richText1.Clear()
        self.m_richText1.BeginTextColour((0, 255, 0))
        self.m_richText1.WriteText(self.InCome)
        self.m_richText1.EndTextColour()
        self.m_richText1.Newline()
        self.m_richText1.BeginTextColour((255, 0, 0))
        self.m_richText1.WriteText(self.Spend)
        self.m_richText1.EndTextColour()
        self.m_tcSpend.SetValue(str(mysum))

    def OnIncome( self, event):
        i = 0
        mysum = 0
        self.InCome =""
        memostr = "( "
        for cb, text in self.Income_List:
            if text.GetValue():
                text.Enable(True)
                label = unicode(InList[i],"utf8")
                mystr = text.GetValue()
                try:
                    mysum += eval(mystr)
                except:
                    pass
                
                memostr += label + " : " + mystr + " "
            i += 1
        memostr += ")"
        self.InCome += memostr

        self.m_richText1.Clear()
        self.m_richText1.BeginTextColour((0, 255, 0))
        self.m_richText1.WriteText(self.InCome)
        self.m_richText1.EndTextColour()
        self.m_richText1.Newline()
        self.m_richText1.BeginTextColour((255, 0, 0))
        self.m_richText1.WriteText(self.Spend)
        self.m_richText1.EndTextColour()
        self.m_tcIncome.SetValue(str(mysum))


###########################################################################
## Launching App
###########################################################################

class YTPMemo(wx.App):

    def OnInit(self):
        self.m_frame = ytp_Main(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)

        return True


if __name__ == '__main__':
    app = YTPMemo(0)
    app.MainLoop()
    
