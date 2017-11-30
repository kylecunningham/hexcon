#imports
import wx
import function

#set up the window
class window(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(window, self).__init__(*args, **kwargs)
		self.OnErrorDlg = wx.MessageDialog(self, "Your text is empty!", "error")
		p = wx.Panel(self)
		s = wx.BoxSizer(wx.VERTICAL)
		s1 = wx.BoxSizer(wx.HORIZONTAL)
		s1.Add(wx.StaticText(p, label='&text to convert'), 0, wx.GROW)
		self.convertText = wx.TextCtrl(p, style=wx.TE_MULTILINE)
		s1.Add(self.convertText, 1, wx.GROW)
		s.Add(s1, 0, wx.GROW)
		s2 = wx.BoxSizer(wx.HORIZONTAL)
		self.ConvertToBtn = wx.Button(p, label='Convert text to &hex')
		s2.Add(self.ConvertToBtn, 0, wx.GROW)
		self.ConvertFromBtn = wx.Button(p, label='&Convert text from hex')
		s2.Add(self.ConvertFromBtn, 1, wx.GROW)
		s.Add(s2, 0, wx.GROW)
		p.SetSizerAndFit(s)
		self.ConvertToBtn.Bind(wx.EVT_BUTTON, self.ConvertTo)
		self.ConvertFromBtn.Bind(wx.EVT_BUTTON, self.ConvertFrom)

	#define our functions
	def ConvertTo(self, event):
		string = self.convertText.GetValue()
		if string == "":
			self.OnErrorDlg.ShowModal()
			return
		hexrep = function.toHex(string)
		self.convertText.SetValue(hexrep)
		self.convertText.SetFocus()

	def ConvertFrom(self, event):
		hexrep = self.convertText.GetValue()
		if hexrep == "":
			self.OnErrorDlg.ShowModal()
			return
		string = function.toStr(hexrep)
		self.convertText.SetValue(string)
		self.convertText.SetFocus()

#initialize the app and set it running
app = wx.App(redirect=False)
w = window(None, title='HexCon', style=wx.MAXIMIZE|wx.SYSTEM_MENU)
w.Show(True)
app.MainLoop()