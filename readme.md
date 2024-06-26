# Mobile App Automation with Appium

This project demonstrates a simple automation script for logging into a demo mobile application using Appium with Python.

## Requirements

- Python 3.x installed on your system
- pip (Python package installer)
- uiautomator2
- Appium-Python-Client

## Project Structure

mini-case-appium-python-automation/
│
├── main.py
├── actions.py
├── config.py
├── requirements.txt
├── README.md

- `main.py`: The main script that runs the automation.
- `actions.py`: Contains reusable functions for interacting with web elements.
- `config.py`: Stores configuration variables like URL and element ID tokens.
- `requirements.txt`: Lists required Python packages.

## Setup

### Step 1: Clone the repository

Clone this repository to your local machine using:

```sh
git clone https://github.com/iqbalnur21/mini-case-appium-python-automation
cd mini-case-appium-python-automation
```

### Step 2: Install Dependencies

Install `uiautomator2` and `Appium-Python-Client` using pip:

```
pip install uiautomator2 Appium-Python-Client
```

Ensure you have Appium server running on your machine. You can download and install Appium Desktop from [here]().

### Step 3: **Install the Demo App**

Download the `DemoApp.apk` and install it on your emulator or device using the following adb command:

```
adb install path/to/DemoApp.apk
```

Replace `path/to/DemoApp.apk` with the actual path to the APK file.

### Step 4: Set up Android automation requirements

Make sure you have an Android emulator and fullfill [this](https://appium.io/docs/en/latest/quickstart/uiauto2-driver/) requirement

## Running the Script

run appium by using this command:

`appium`

Execute the main script using Python:

`python main.py`

Or if you use windows operating system just double click `main.py` file in your computer

## Customization

* To modify actions or add new ones, edit the `actions.py` file.
* To change configuration variables of desired_caps, edit the `config.py` file.
