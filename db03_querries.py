import sys
import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
from loguru import logger

# Configure logger to show output in the terminal
logger.add(sys.stderr, level="INFO")

# ---------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------

def run_sql_file(connection: sqlite3.Connection, file_path: pathlib.Path) -> None:
    """
    Executes a SQL file (containing multiple SQL statements) using the given SQLite connection.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        with connection:
            connection.executescript(sql_script)
        logger.info(f"Executed SQL file: {file_path.name}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path.name}: {e}")
        raise

def run_sql_file_to_df(conn: sqlite3.Connection, file_path: pathlib.Path) -> pd.DataFrame:
    """
    Reads a SQL query from a file, executes it, and returns the result as a DataFrame.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_query = file.read()
        df = pd.read_sql_query(sql_query, conn)
        logger.info(f"Loaded DataFrame from SQL file: {file_path.name} ({len(df)} rows)")
        return df
    except Exception as e:
        logger.error(f"Failed to load DataFrame from {file_path.name}: {e}")
        raise

def run_to_df(conn: sqlite3.Connection, sql: str) -> pd.DataFrame:
    """
    Executes a SQL string and returns a DataFrame.
    """
    try:
        df = pd.read_sql_query(sql, conn)
        logger.info(f"Query returned {len(df)} rows.")
        return df
    except Exception as e:
        logger.error(f"Failed to execute SQL query: {e}")
        raise

def create_scatter_plot(conn: sqlite3.Connection, sql_file_path: pathlib.Path):
    """
    Creates a scatter plot using results from a SQL query stored in a file.
    The SQL must return columns 'age_when_published' and 'year_published'.
    """
    try:
        df = run_sql_file_to_df(conn, sql_file_path)

        if 'age_when_published' not in df.columns or 'year_published' not in df.columns:
            logger.warning(f"Expected columns not found in {sql_file_path.name}")
            return

        plt.figure(figsize=(12, 6))
        plt.scatter(df['age_when_published'], df['year_published'], color='teal', alpha=0.7)
        plt.xlabel('Age of Author When Published')
        plt.ylabel('Year Published')
        plt.title('Year Published vs Age of Author')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
        logger.info(f"Scatter plot created from {sql_file_path.name}")
    except Exception as e:
        logger.error(f"Failed to create scatter plot: {e}")
        raise

# ---------------------------------------------------------------------
# Main script logic
# ---------------------------------------------------------------------

def main():
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_QUERIES_FOLDER = ROOT_DIR.joinpath("sql_queries")
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath("books_authors.db")

    DATA_FOLDER.mkdir(exist_ok=True)
    logger.info("Starting query execution...")
    logger.info(f"Using database: {DB_PATH}")

    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        # Check available .sql files
        if SQL_QUERIES_FOLDER.exists():
            sql_files = list(SQL_QUERIES_FOLDER.glob("*.sql"))
            logger.info(f"Found {len(sql_files)} SQL files in {SQL_QUERIES_FOLDER}")
            for f in sql_files:
                logger.info(f" - {f.name}")
        else:
            logger.error(f"SQL folder does not exist: {SQL_QUERIES_FOLDER}")
            return

        # Execute queries
        run_sql_file(connection, SQL_QUERIES_FOLDER.joinpath('query_join.sql'))
        df_join = run_to_df(connection, "SELECT * FROM authors_books LIMIT 20")
        logger.info(f"authors_books table has {len(df_join)} rows shown")

        df_sorting = run_sql_file_to_df(connection, SQL_QUERIES_FOLDER.joinpath('query_sorting.sql'))
        logger.info(f"Sorting query returned {len(df_sorting)} rows")

        df_group_by = run_sql_file_to_df(connection, SQL_QUERIES_FOLDER.joinpath('query_group_by.sql'))
        logger.info(f"Group by query returned {len(df_group_by)} rows")

        df_aggregation = run_sql_file_to_df(connection, SQL_QUERIES_FOLDER.joinpath('query_aggregation.sql'))
        logger.info(f"Aggregation query returned {len(df_aggregation)} rows")

        # Create scatter plot
        create_scatter_plot(connection, SQL_QUERIES_FOLDER.joinpath('query_aggregation.sql'))

        logger.info("Database operations completed successfully.")
    except Exception as e:
        logger.error(f"Error during database operations: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")

# ---------------------------------------------------------------------

if __name__ == '__main__':
    main()
