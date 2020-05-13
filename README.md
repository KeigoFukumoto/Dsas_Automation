# Dsas_Automation

System_Automationシートはパーツの型番をキー値としたデータベースとなっています。
ウェブスクレイピングで自動更新するスクリプトの作成は庄司さんにお願いしましたが
色々後々になってしまい統合テストはできていません。
テストがうまく動作する様であればウェブスクレイピングと合わせて本pythonスクリプトの実行で
SYstem_Automation.xlsxに保存されたパーツ情報を機器構成シートに転記します。



▼本レポジトリはDsasの機器構成シートの自動化の為のpythonコードです
実行の前提としてWindows10 PC上で動作を確認したので同様の条件で
pip3を含むpython3.x をインストールしてください。
インストールについては下記を参照。
https://vgkits.org/blog/pip3-windows-howto/

"write_composition_sheet.py"ファイルを実行するとSystemAutomation.xlsxの各列から機器構成シートを読み込みSample.xlsxへ転記します

実行にはいくつかの必要なライブラリがあります。

openpyxl
$ pip3 install openpyxl

pandas
$ pip3 install pandas

tkinterはpython3では必要ない筈

転記の実行は下記コマンドを実行
$ py write_composition_sheet.py
