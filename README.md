# Dsas_Automation


Dsasの機器構成シートの自動化の為のpythonコードです
前提としてpip3を含むpython3.x をインストールしてください
https://vgkits.org/blog/pip3-windows-howto/

下記のファイルを実行するとSystemAutomation.xlsxの各列から機器構成シートを読み込みSample.xlsxへ転記します

実行にはいくつかの必要なライブラリがあります。

openpyxl
$ pip3 install openpyxl

pandas
$ pip3 install pandas

tkinterはpython3では必要ない筈

転記の実行は下記コマンドを実行
$ py write_composition_sheet.py
