
# import webbrowser
import pandas as pd
import re
PR = pd.read_csv("output pr", sep='\t', header=None)
# PR.head()
f = open("inverted index out", "r", encoding='utf-8')
inverted_index = f.read()
# print(inverted_index)
f2 = open("input pr.txt", "r", encoding='utf-8')
links = f2.readlines()
import re
def search_engine(s_word, PR_f, i_index_f, links_f):
    urls = []
    flag = 1

    # work on inverted index file
    start = i_index_f.find(s_word)  # start of the word line
    if start == -1:
        flag = 0
    else:
        end = start + i_index_f[start:].find("\n")  # end of the word line
        line = i_index_f[start:end]  # extract the line of the word
        content = line.split()  # split the line to (word ,files numbers)
        num = [m.end() for m in re.finditer('file', content[1])]
        page_num = []
        for n in num:  # have the number of files(url)
            page_num.append(content[1][n: n + content[1][n:].find(":")])

        # work on page ranking file
        page_wight = {}
        for x in page_num:  # have the wights of pages from PR_f
            page_wight[x] = float(PR_f[PR_f[0] == int(x)][1])
        # sort the pages by it's wights
        page_wight_sorted = sorted(page_wight.items(), key=lambda x: x[1], reverse=True)
        the_pages = dict(page_wight_sorted)

        for z in the_pages.keys():
            s_link = links_f[int(z) + 1].find(' ') + 1
            e_link = links_f[int(z) + 1].find('\n')
            urls.append(links_f[int(z) + 1][s_link: e_link])
    return urls, flag

from tkinter import *
import webbrowser
root = Tk()
root.geometry("1000x1000")
root.title("search engine")
#Define a callback function
def callback(i):
   webbrowser.open_new_tab(i)
def Take_input():
    # to clear content of text each time print data
    # to take input words from search filed
    INPUT = inputtxt.get("1.0", "end-1c")
    inputtxt.delete("1.0", "end")  # to delete all in search input
    result, flage = search_engine(INPUT, PR, inverted_index, links)
    if INPUT == "":
        link2 = Label(root, text="\n ==>     have not input"+'\n')
        link2.pack()

    elif flage != 1:
        link4 = Label(root, text="\n ==>     result not found" + '\n')
        link4.pack()

    else:
        for i in result:
            link1 = Label(root, text=str(i), fg="blue", cursor="hand2", bd="5", font="40px", height="2")
            link1.pack()
            link1.bind("<Button-1>", lambda e: callback(i))

    link4 = Label(root, text="----------------------------------------------------------------------------------------------------")
    link4.pack()

l = Label(text="Searching")
inputtxt = Text(root, height=2,
                width=100,padx="50",pady="20",
                bg="LightBlue",
                relief="groove")

# Add a Scrollbar(horizontal)
v = Scrollbar(root, orient='vertical', bg="black")
v.pack(side=RIGHT, fill='y')
# Output = Text(root, height=250,
#               width=100,
#               bg="white",
#               yscrollcommand=v.set
#               )

Display = Button(root, height=2,
                 fg='black',
                 bg='black',
                 width=20,
                 text="search",
                 command=lambda: Take_input())

# Attach the scrollbar with the text widget
# v.config(command=Output.yview)
l.pack()
inputtxt.pack()
Display.pack()
# Output.pack()
mainloop()
