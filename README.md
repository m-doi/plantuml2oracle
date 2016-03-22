# plantuml2oracle

## DESCRIPTION
PlantUMLのクラス図を使って書いたER図をOracleのSQLに変換するモジュールです。
こちらを参考にさせていただきました。THX！！

https://github.com/grafov/plantuml2mysql

## USAGE
python3系でないと動きません。
```
./plantuml2oracle.py sample.puml
```
start.meta〜end.metaに囲まれた部分はテーブル、カラムの情報です。
ここに欠いている情報を元に論理名⇆物理名に変換します。

## LICENCE
This code is public domain. You can copy, modify, distribute and perform the work,
even for commercial purposes, all without asking permission.
