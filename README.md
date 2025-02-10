# **Internet-SpeedTest**  
🚀 A Python script to measure internet speed using the Speedtest.net API and store results in an SQLite database.  

## **License**  
This project is licensed under the **GPL-3.0 License**.  

## **Overview**  
This script tests your internet speed and logs the results for future reference. It utilizes:  
- **speedtest** for measuring download, upload, and ping speeds.  
- **sqlite3** for storing test results in a local database.  

## **Prerequisites**  
Ensure you have the required dependencies installed:  

```sh
pip install speedtest-cli

## **Database Details**  
The script creates a **SQLite database** named `SpeedTest.db` in the project directory (if it doesn’t already exist).  

### **Table Structure (Speed Table)**  
| Column   | Data Type |
|----------|-----------|
| Date     | TEXT      |
| Time     | TEXT      |
| Download | REAL      |
| Upload   | REAL      |
| Ping     | INTEGER   |

Each test run **inserts a new row** into the `Speed` table, storing:  
📅 **Date** | ⏰ **Time** | 📥 **Download Speed (Mbps)** | 📤 **Upload Speed (Mbps)** | 📶 **Ping (ms)**  

## **Usage**  
Run the script using:  
```sh
python speedtest_script.py
