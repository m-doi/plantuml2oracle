# plantuml2oracle

## DESCRIPTION
PlantUMLのクラス図を使って書いたER図をOracleのSQLに変換するモジュールです。
こちらを参考にさせていただきました。THX！！

https://github.com/grafov/plantuml2mysql

## USAGE
python3系でないと動きません。

### INPUT
```
@startuml
hide circle

    class 社員 {
        ==
        #社員番号
        社員名
    }

    class 部門 {
        ==
        #部門番号
        部門名
    }

    class 所属 {
        ==
        #社員番号
        #部門番号
    }
@enduml

@starttmeta
  社員|employees
  部門|departments
  所属|belonging
@endtmeta

@startcmeta
  社員番号|e_id varchar(8) not null
  社員名|e_name varchar(24) not null
  部門番号|d_id varchar(3) not null
  部門名|d_name varchar(12) not null
@endcmeta
```
### EXEC
```
./plantuml2oracle.py sample.puml
```

### OUTPUT
```
CREATE TABLE employees (
	e_id varchar(8) not null,
	e_name varchar(24) not null,
	CONSTRAINT pk_employees PRIMARY KEY(e_id)
);

CREATE TABLE departments (
	d_id varchar(3) not null,
	d_name varchar(12) not null,
	CONSTRAINT pk_departments PRIMARY KEY(d_id)
);

CREATE TABLE belonging (
	e_id varchar(8) not null,
	d_id varchar(3) not null,
	CONSTRAINT pk_belonging PRIMARY KEY(e_id, d_id)
);
```

start.meta〜end.metaに囲まれた部分はテーブル、カラムの情報です。
ここに欠いている情報を元に論理名⇆物理名に変換します。

## LICENCE
This code is public domain. You can copy, modify, distribute and perform the work,
even for commercial purposes, all without asking permission.
