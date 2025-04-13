# ISS Tracker

A Python application that tracks the International Space Station (ISS) in real-time, displays its current location on a world map, and provides information about astronauts currently on board.

## Features

- Displays the ISS's real-time location on a world map
- Shows the number of astronauts currently on board the ISS
- Lists the names of all astronauts on the ISS
- Displays your current geographical location
- Updates the ISS position every 3 seconds

## Requirements

- Python 3.x
- Internet connection
- Required Python packages:
  - `turtle`
  - `json`
  - `urllib`
  - `webbrowser`
  - `geocoder`
  - `time`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/username/iss-tracker.git
   cd iss-tracker
   ```

2. Install required packages:
   ```
   pip install geocoder
   ```

3. Download the required image files:
   - `map.gif` - A world map image
   - `iss.gif` - An ISS icon image

## Usage

Run the script:
```
python iss_tracker.py
```

The application will:
1. Create a file `iss.txt` with information about the astronauts on the ISS
2. Open this file in your default web browser
3. Display a world map with the current location of the ISS
4. Update the ISS location every 3 seconds

Press Enter when prompted with "stop" to exit the application.

## How It Works

This application uses two APIs from [Open Notify](http://open-notify.org/):
- `http://api.open-notify.org/astros.json` - Provides data about astronauts in space
- `http://api.open-notify.org/iss-now.json` - Provides the current location of the ISS

The application also uses:
- `geocoder` - To determine your current location
- `turtle` - To display the world map and the ISS
- `webbrowser` - To open the generated text file

## Customization

- Replace `map.gif` with a different world map image
- Replace `iss.gif` with a different ISS icon
- Modify the update frequency by changing the `time.sleep()` value

## Credits

- [Open Notify API](http://open-notify.org/) for ISS data
- Based on tutorial: [YouTube - ISS Tracker Tutorial](https://www.youtube.com/watch?v=5UWeOfdESZE)
