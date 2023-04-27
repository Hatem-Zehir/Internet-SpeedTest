# Internet-SpeedTest

This Python script measures the speed of your internet connection using the Speedtest.net API and saves the results in a SQLite database. The script uses the speedtest and sqlite3 libraries to perform the test and store the data, respectively.

# Prerequisites
To run this project, you must have the following libraries installed:
- speedtest
- sqlite3

You can install them by running the following command in your terminal:

```
pip install speedtest sqlite3
```

# Database
The script creates a SQLite database named SpeedTest.db in the project directory, if it does not exist already. It creates a table named Speed with the following columns:

- Date (text)
- Time (text)
- Download (real)
- Upload (real)
- Ping (integer)

The script inserts a new row into the Speed table each time it is run, with the current date and time, download speed, upload speed, and ping time.
