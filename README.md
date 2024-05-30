# Automated ISP Speed Complaint Bot

## Description

This Python script utilizes Selenium to perform a speed test on your device, compare the results against the promised download and upload speeds from your ISP, and automatically tweet at your ISP's customer support if the speeds are lower than promised.

## Features

- **Speed Test**: Uses Selenium to run an internet speed test on your device.
- **Speed Comparison**: Compares the test results with the promised download and upload speeds from your ISP.
- **Automated Complaint**: If the measured speeds are lower than promised, the bot logs into your Twitter account and tweets at the ISP's customer support to report the issue.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Redchord520/ISP_tweet_bot.git
    cd ISP_tweet_bot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and place it in your PATH.

## Usage

1. Update the configuration file `config.json` with your:
    - Promised download and upload speeds
    - Twitter login credentials
    - ISP's Twitter handle

2. Run the script:
    ```bash
    python main.py
    ```

3. The script will:
    - Perform a speed test.
    - Compare the results with the promised speeds.
    - Log in to your Twitter account if the speeds are lower than promised.
    - Tweet at your ISP's customer support to report the issue.

## File Structure

- `main.py`: The main script to run the application.
- `speed_test.py`: Contains the logic for performing the speed test.
- `tweet_bot.py`: Contains the logic for logging into Twitter and sending a tweet.
- `config.json`: Configuration file for user settings and credentials.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

Special thanks to the contributors of the Selenium project and Angel Yu.

