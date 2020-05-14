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

▼pipを念のためupgradeしといてください
$python -m pip install --upgrade pip


"write_composition_sheet.py"ファイルを実行するとSystemAutomation.xlsxの各列から機器構成シートを読み込みSample.xlsxへ転記します

実行にはいくつかの必要なライブラリがあります。

openpyxl
$ pip3 install openpyxl

pandas
$ pip3 install pandas

xrld
$ pip3 install xlrd

*tkinterも使ってますがpython3ではimportやインストールせずに実行できました

!!実行にあたって機器構成シートに機器構成(パーツ型番,パーツ名称）を機器構成シートに記載しておく必要があります
　　パーツの搭載位置は付属のマクロで記入してください
!!本コードは2020年１月頃の機器構シートのフォーマットを基本にしているのでもしフォーマットに変化があった場合は
　コードを書き直すメンテナンスが必要になる可能性があります。
 
!!当初は福本以外の人が使用する事はあまり想定していなかったので使いづらい部分は工夫して
　修正しバージョンを改良してください。Pythonの良いトレーニングになるでしょう
 
!!System_AUtomation.xlsxファイル上のFW情報が古い場合は機器構成シートに転記されるFWバージョン情報もそのまま古いものになってしまうので
　System_Automation.xlsxファイル上の情報を適宜更新してください。System_Automation.xlsxファイル上にないパーツやサーバーモデルの情報は
  転記されませんので、(現状は福本が手で更新してましたが)庄司さんのスクレイピングスクリプトでSYstem_Automation.xlsx上のファイルを自動更新してもらうようお願いします。

System_Automation.xlsx上の情報から転記の実行は下記コマンドを実行
$ py write_composition_sheet.py


実行したら書き込み対象の構成表を選択してくださいというプロンプトがでるので
OKを押して機器名称とパーツIDを記入済みの機器構成シートファイルをフォルダから指定してください。

