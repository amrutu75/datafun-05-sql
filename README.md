
# datafun-05-sql

In this module, we use sqlite3 from the Python Standard Library to interact with SQL data using Python. 

**Learning Outcome**
- To be able to create and manipulate database using Python and SQL
- To undeststand the basic file-based relational databases like SQLite and may get a bit of practice reading CSV files with pandas.
- Offer a lightweight starting point for assignment or self-study in data analysis.

**Project Description**
Use Python to create and manage the overall database. 
Use SQL to interact with the relational data and tables. 
Our DBMS is SQLite, a lightweight, file-based database widely used in browsers, mobile devices, and more. 
Use several packages from the  Python Standard Library:
csv - optional - preferably using pandas as the code is a bit cleaner
pathlib
sqlite3
uuid - optional - utility for creating unique ids (helpful with databases)
Add an external dependency (e.g. pandas), so we'll need to create a project-specific virtual environment using venv and pip. 
pandas to read from csv with cleaner code

**Contents**
- `requirements.txt` — packages and setup instructions for a virtual environment.
- `README.md` — this file with project overview and usage instructions.

**Initial set up**

```git clone repo: https://github.com/amrutu75/datafun-05-sql
 ```
 
**Getting started**
---------------

1. Create and activate a Python virtual environment in the project root:

	 - Windows PowerShell:

		 ```powershell
		 py -m venv .venv
		 .\.venv\Scripts\Activate
		 ```

	 - macOS / Linux:

		 ```bash
		 python3 -m venv .venv
		 source .venv/bin/activate
		 ```

2. Upgrade packaging tools and install dependencies:

	 - Windows PowerShell:

		 ```powershell
		 py -m pip install --upgrade pip setuptools wheel
		 py -m pip install --upgrade -r requirements.txt --timeout 100
		 ```

	 - macOS / Linux:

		 ```bash
		 python3 -m pip install --upgrade pip setuptools wheel
		 python3 -m pip install --upgrade -r requirements.txt --timeout 100
		 ```

Usage
-----

Inspect or run SQL files using SQL engine. If the repository includes examples .sql files or Python script , follow the instructions

# datafun-05-sql

This project partially completes the requirements for [datafun-05-spec](https://github.com/denisecase/datafun-05-spec).

## Python Standard Library

The project uses these packages from the Python Standard Library:

- pathlib - to work with folders and files
- sqlite3 - to work with a Sqlite file-based database

If you want to avoid using a project virtual environment, it is possible to use the csv module from the Python Standard Library to read csv files. 

## External Packages & Project Virtual Environment

To work with csv files using a bit cleaner code, we choose to use pandas, an external library, not part of the Python Standard Library. 
Therefore, this project requires a project virtual environment, which we recommend creating in the .venv folder. 

## Organization

This project organizes SQL scripts and Python scripts into separate folders to ensure a structured and maintainable workflow for database management.

- data/ – Stores the SQLite database (db.sqlite).
- sql_create/ – Contains SQL scripts for database setup:
  - 01_drop_tables.sql – Drops any existing tables
  - 02_create_tables.sql – Creates tables
  - 03_insert_records.sql – Inserts initial data
- sql_features/ – Contains SQL scripts for feature engineering and schema modifications.
- sql_analytics/ – Contains SQL scripts for analytics queries and aggregations.

## Run Scripts

First: Create a virtual environment, activate it, and install requirements.txt (see requirements.txt for commands). 

1. Activate the .venv
2. Run the Python file 

Windows Example
```powershell
.\.venv\Scripts\activate
py db01_setup.py
```


Mac/Linux Example
```shell
source .venv/bin/activate
python3 db01_setup.py
```



