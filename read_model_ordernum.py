import xlrd
import pandas as pd
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import messagebox

def select_file():
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('○×プログラム','対象の構成表を選択してください')
    file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

    # 処理ファイル名の出力
    tkinter.messagebox.showinfo('○×プログラム',file)
    return file

def read_excel_column():
    file = select_file()
    #print("Sheet name?>")
    sheet_nm=input_sheet_name()
    df = pd.read_excel(file,sheet_name=sheet_nm,header=0,index_col=0)
    print(df)
    print('構成表excelファイルを読み込みました')
    return df

def input_sheet_name():
    root = tk.Tk()
    root.withdraw() #小さなウィンドウを表示させない

    inputdata = simpledialog.askstring("Input Box", "シート名を入力してください",)
    print("simpledialog",inputdata)
    return inputdata


def format_list():
    #print("シート名を入力>")
    #rSheet_name=input()
    df = read_excel_column()
    #column = df_use_skip.loc[:,["品番","品名","数量"]]
    #print(column)
    #column = df_use_skip.loc[:,["製品番号","製品名","数量"]]
    #print(column)
    #column = df_use_skip.loc[:,["メーカー型番","商品名","数量"]]
    #print(column)
    #column = df_use_skip.loc[:,["メーカー型番","商品名","受注数"]]
    #print(column)
    #column = df_use_skip.loc[:,["メーカー型番","品名","受注数"]]
    #print(column)
    #column = df_use_skip.loc[:,["製品番号","製品名","数量"]]
    #print(column)

    #column = df.loc[:,["製品番号","メーカー型番","品番","品名","商品名","製品名","受注数","数量"]]
    #column = df.loc[:,["Model ID","Product Name","Num"]]
    #print(column)
    return df

