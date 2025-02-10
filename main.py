import sqlite3
import speedtest
from datetime import datetime


def run_speed_test():
    """
    Run the speed test and return download/upload speeds in Mbps and ping in ms.
    
    Returns:
        tuple: (download_mbps (float), upload_mbps (float), ping (int))
    """
    try:
        s = speedtest.Speedtest()
        # Optionally, you can retrieve servers if you want to filter them:
        # s.get_servers([])
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()
        results = s.results.dict()

        download_mbps = round(results['download'] / (1024 * 1024), 2)
        upload_mbps = round(results['upload'] / (1024 * 1024), 2)
        ping = round(results['ping'], 0)

        return download_mbps, upload_mbps, ping

    except Exception as e:
        print(f"An error occurred during the speed test: {e}")
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
    now = datetime.now()
    date_str = now.strftime("%d %B %Y")
    time_str = now.strftime("%H:%M")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Speed (
        Date TEXT,
        Time TEXT,
        Download REAL,
        Upload REAL,
        Ping INTEGER
    )
    """
    insert_query = "INSERT INTO Speed (Date, Time, Download, Upload, Ping) VALUES (?, ?, ?, ?, ?)"

    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(create_table_query)
            conn.execute(insert_query, (date_str, time_str, download, upload, ping))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while storing results in the database: {e}")


def main():
    download, upload, ping = run_speed_test()
    if download is not None:
        store_results(download, upload, ping)
        print(f"Download: {download} Mbps")
        print(f"Upload: {upload} Mbps")
        print(f"Ping: {ping} ms")
    else:
        print("Speed test failed. Results not stored.")


if __name__ == "__main__":
    main()
