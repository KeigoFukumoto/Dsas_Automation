# Dsas_Automation


Dsasの機器構成シートの自動化の為のpythonコードです

下記のファイルを実行するとSystemAutomation.xlsxの各列から機器構成シートを読み込みSample.xlsxへ転記します

実行にはいくつかの必要なライブラリがあります。

openpyxl
$ pip3 install openpyxl

pandas
$ pip3 install pandas

tkinter

転記の実行は下記コマンドを実行
$ py write_composition_sheet.py
