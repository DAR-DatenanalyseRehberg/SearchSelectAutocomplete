import pandas as pd
from tkinter import *

df = pd.read_excel('SearchAutofill.xlsm', sheet_name="Standards", engine='openpyxl', header=None)
df['ConcatTranslate'] = df[0] + str('---') + df[1]
languageTerms = df['ConcatTranslate'].to_numpy()

root = Tk() # to initialize Tkinter we must create a Tkinter root widget
root.title('Search and choose term')
root.geometry("600x400")

UserForm = Label(root, text="Search") #Define label widget where first parameter of the label method contains the parent widget root .A Tk label is a tkinter class (widget) which only will be displayed-no interaction possible
UserForm.pack(pady=10) # pack method used to embed label into existing widget. Use pady to give some space, otherwise overlapping
SearchText = Entry(root, font=("Arial", 20)) # create entry box where user can search, size of entry form
SearchText.pack() # already pady done by above UserForm label
ListBoxTerms = Listbox(root, width=50) # create a list box which displays English/German translations
ListBoxTerms.pack(pady=40)

def ListFill(data): #update the ListBoxTerms to user's input accordingly
	ListBoxTerms.delete(0, END) # list boxes are deleted from 0 to end
	for item in data: # Add German/English Translations to listbox
		ListBoxTerms.insert(END, item)
def ListBoxTermsDoubleClick(x):# update SearchText with what was clicked on ListBoxTerms
	SearchText.delete(0, END) # delete user`s input in SearchText
	SearchText.insert(0, ListBoxTerms.get(ANCHOR))
	print(ListBoxTerms.get(ANCHOR))
def ListFillFilter(x): # check SearchText vs ListBoxTerms; in other words: user`s input search string vs matching results in ListBoxTerms
	typed = SearchText.get() # get user`s input search string
	if typed == '': # if nothing entered, then display the complete list
		data = languageTerms
	else:
		data = []
		for item in languageTerms:
			if typed.lower() in item.lower():
				data.append(item)
	ListFill(data) # update ListBoxTerms with user's SearchText
ListFill(languageTerms) # update ListBoxTerms with user's SearchText
ListBoxTerms.bind("<Double-1>", ListBoxTermsDoubleClick)# Double click on any ListBoxTerms will be binded
SearchText.bind("<KeyRelease>", ListFillFilter)# after each key releasing in SearchText, this current string will be binded.
root.mainloop() # the label is not displayed until we apply the mainloop method to the root widget. The window created by our script remains in the event loop until we close the window.

