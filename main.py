import sqlite3
import speedtest
from datetime import datetime
import os


def run_speed_test():
    """
    Run the speed test and return download/upload speeds in Mbps and ping in ms.
    
    Returns:
        tuple: (download_mbps (float), upload_mbps (float), ping (int))
    """
    try:
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        results = s.results.dict()

        download_mbps = round(results['download'] / (1024 * 1024), 2)
        upload_mbps = round(results['upload'] / (1024 * 1024), 2)
        ping = round(results['ping'])

        return download_mbps, upload_mbps, ping

    except Exception as e:
        print(f"Speed test error: {e}")
        return None, None, None


def store_results(download, upload, ping, db_path="SpeedTest.db"):
    """
    Store the speed test results in a SQLite database.
    
    Args:
        download (float): Download speed in Mbps.
        upload (float): Upload speed in Mbps.
        ping (int): Ping in ms.
        db_path (str): Path to the SQLite database file.
    """
    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")

    # Ensure database directory exists
    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS SpeedTestResults (
        timestamp TEXT PRIMARY KEY,
        download REAL,
        upload REAL,
        ping INTEGER
    )
    """
    insert_query = """
    INSERT INTO SpeedTestResults (timestamp, download, upload, ping)
    VALUES (?, ?, ?, ?)
    """

    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(create_table_query)
            conn.execute(insert_query, (timestamp, download, upload, ping))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")


def main():
    print("Running speed test...")
    results = run_speed_test()
    if results != (None, None, None):
        download, upload, ping = results
        store_results(download, upload, ping)
        print(f"Results:\nDownload: {download} Mbps\nUpload: {upload} Mbps\nPing: {ping} ms")
    else:
        print("Speed test failed. Results not stored.")


if __name__ == "__main__":
    main()
