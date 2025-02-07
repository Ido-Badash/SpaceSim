
# Solar System Simulator

A Python-based solar system simulator that allows users to zoom in and out and explore real-life data of the planets. The project utilizes real astronomical data to create a realistic, interactive experience for users to visualize our solar system.

## Features

- **Zoom in and Zoom out**: Users can zoom in and out to explore the planets and other celestial bodies in the solar system.
- **Real-Life Data**: The simulator uses real-world data for each planet (e.g., diameter, mass, distance from the Sun, etc.).

## Installation

To run the Solar System Simulator, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/SolarSim.git
```

### 2. Install dependencies

Make sure you have Python 3.8+ installed. Then, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the simulator

After installing the dependencies, run the project using the following command:

```bash
python main.py
```

## Technologies Used

- **Python**: The core language used for simulation and interaction.
- **Pygame**: Used to create the interactive user interface and simulate movement within the solar system.


### Notes:
- The `src` folder contains all the primary source code, broken down into manageable components such as drawing, testing, updaters, and utility functions.
- `assets` includes visual elements like images for planets and UI logos, which are used to display the simulation in a graphical format.
- `data` holds configuration files like planetary alignment, which can be used for simulation purposes.
