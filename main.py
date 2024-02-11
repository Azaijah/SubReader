import webbrowser
import re, sys
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog

class App:
  def __init__(self, root):
    self.counter = 0
    self.words = []
    self.new_lines = []
    self.file_name = None

    self.load_file_button = tk.Button(root, text="Load File", command=self.load_file)
    self.load_file_button.pack()

    root.title("undefined")
    # setting window size
    width = 1500
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    self.GButton_476 = tk.Button(root)
    self.GButton_476["bg"] = "#f0f0f0"
    self.GButton_476["cursor"] = "spider"
    ft = tkFont.Font(family='Times', size=10)
    self.GButton_476["font"] = ft
    self.GButton_476["fg"] = "#000000"
    self.GButton_476["justify"] = "center"
    self.GButton_476["text"] = "Next Line"
    self.GButton_476.place(x=470, y=100, width=70, height=25)
    self.GButton_476["command"] = self.NextLineCommand

    self.GButton_683 = tk.Button(root)
    self.GButton_683["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    self.GButton_683["font"] = ft
    self.GButton_683["fg"] = "#000000"
    self.GButton_683["justify"] = "center"
    self.GButton_683["text"] = "SpanishDict"
    self.GButton_683.place(x=470, y=160, width=70, height=25)
    self.GButton_683["command"] = self.OpenWordInSpanishDict

    self.GButton_946 = tk.Button(root)
    self.GButton_946["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    self.GButton_946["font"] = ft
    self.GButton_946["fg"] = "#000000"
    self.GButton_946["justify"] = "center"
    self.GButton_946["text"] = "DeepL"
    self.GButton_946.place(x=470, y=210, width=70, height=25)
    self.GButton_946["command"] = self.OpenInDeepLWord

    self.GButton_886 = tk.Button(root)
    self.GButton_886["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    self.GButton_886["font"] = ft
    self.GButton_886["fg"] = "#000000"
    self.GButton_886["justify"] = "center"
    self.GButton_886["text"] = "Back"
    self.GButton_886.place(x=390, y=100, width=70, height=25)
    self.GButton_886["command"] = self.PreviousLineCommand

    self.GLabel_954 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=10)
    self.GLabel_954["font"] = ft
    self.GLabel_954["fg"] = "#333333"
    self.GLabel_954["justify"] = "center"
    self.GLabel_954["text"] = "No file loaded"  # Default text
    self.GLabel_954.place(x=90, y=30, width=1400, height=52)

    self.GListBox_179 = tk.Listbox(root)
    self.GListBox_179["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    self.GListBox_179["font"] = ft
    self.GListBox_179["fg"] = "#333333"
    self.GListBox_179["justify"] = "center"
    self.GListBox_179["relief"] = "ridge"
    self.GListBox_179.place(x=100, y=170, width=235, height=300)
    self.GListBox_179["exportselection"] = "0"

    self.GLabel_828 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=10)
    self.GLabel_828["font"] = ft
    self.GLabel_828["fg"] = "#333333"
    self.GLabel_828["justify"] = "center"
    self.GLabel_828["text"] = str(self.counter) + "/" + str(len(self.new_lines))
    self.GLabel_828.place(x=20, y=20, width=70, height=25)

    self.GButton_136 = tk.Button(root)
    self.GButton_136["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    self.GButton_136["font"] = ft
    self.GButton_136["fg"] = "#000000"
    self.GButton_136["justify"] = "center"
    self.GButton_136["text"] = "DeepL Line"
    self.GButton_136.place(x=360, y=210, width=70, height=25)
    self.GButton_136["command"] = self.OpenInDeepLLine

  def load_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Subtitle files", "*.srt")])
    if file_path:
      self.file_name = file_path
      self.read_file()


  def update_ui(self):
    if self.new_lines:
      self.GLabel_954["text"] = self.new_lines[self.counter] if self.counter < len(self.new_lines) else "No content"
      self.GLabel_828["text"] = str(self.counter) + "/" + str(len(self.new_lines))

    else:
      self.GLabel_954["text"] = "No valid content found"
      self.GLabel_828["text"] = "0/0"

  def read_file(self):
    if self.file_name:
      file_encoding = 'utf-8'
      with open(self.file_name, encoding=file_encoding, errors='replace') as f:
        lines = f.readlines()
        self.new_lines = clean_up(lines)
      self.update_ui()

  def NextLineCommand(self):

    self.GListBox_179.delete(0, len(self.words))

    self.counter += 1
    self.GLabel_828["text"] = str(self.counter) + "/" + str(len(self.new_lines))
    self.GLabel_954['text'] = self.new_lines[self.counter]

    self.words = self.new_lines[self.counter].split()

    for n, word in enumerate(self.words):
      self.GListBox_179.insert(n, word)

  def PreviousLineCommand(self):

    self.GListBox_179.delete(0, len(self.words))

    self.counter -= 1
    self.GLabel_828["text"] = str(self.counter) + "/" + str(len(self.new_lines))
    self.GLabel_954['text'] = self.new_lines[self.counter]

    self.words = self.new_lines[self.counter].split()

    for n, word in enumerate(self.words):
      self.GListBox_179.insert(n, word)


  def OpenWordInSpanishDict(self):
    webbrowser.open('https://www.spanishdict.com/translate/'+self.words[self.GListBox_179.curselection()[0]])

  def OpenInDeepLWord(self):
    webbrowser.open('https://www.deepl.com/translator#es/en/'+self.words[self.GListBox_179.curselection()[0]])


  def OpenInDeepLLine(self):
    webbrowser.open('https://www.deepl.com/translator#es/en/' + self.new_lines[self.counter])

def is_time_stamp(l):
  if l[:2].isnumeric() and l[2] == ':':
    return True
  return False

def has_letters(line):
  if re.search('[a-zA-Z]', line):
    return True
  return False

def has_no_text(line):
  l = line.strip()
  if not len(l):
    return True
  if l.isnumeric():
    return True
  if is_time_stamp(l):
    return True
  if l[0] == '(' and l[-1] == ')':
    return True
  if not has_letters(line):
    return True
  return False

def is_lowercase_letter_or_comma(letter):
  if letter.isalpha() and letter.lower() == letter:
    return True
  if letter == ',':
    return True
  return False

def clean_up(lines):

  new_lines = []
  for line in lines[1:]:
    if has_no_text(line):
      continue
    elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
      new_lines[-1] = new_lines[-1].strip() + ' ' + line
    else:
      new_lines.append(line)
  return new_lines

def main():
  root = tk.Tk()
  App(root)
  root.mainloop()

if __name__ == '__main__':
  main()









