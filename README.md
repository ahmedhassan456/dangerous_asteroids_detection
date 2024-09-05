# Dangerous Asteroids Detection

## Project Overview

This project implements a machine learning model to detect potentially hazardous asteroids using NASA's asteroid data. The model is deployed as a web service using FastAPI, allowing for real-time predictions on asteroid hazards.

## Dataset Description

The dataset contains information on 338,199 asteroids with the following features:

- **neo_id**: Unique identifier for each asteroid
- **name**: Name given by NASA
- **absolute_magnitude**: Describes intrinsic luminosity
- **estimated_diameter_min**: Minimum estimated diameter in kilometers
- **estimated_diameter_max**: Maximum estimated diameter in kilometers
- **orbiting_body**: Planet that the asteroid orbits
- **relative_velocity**: Velocity relative to Earth in km/h
- **miss_distance**: Distance missed in kilometers
- **is_hazardous**: Boolean feature indicating whether the asteroid is potentially hazardous

## Technologies Used

- Python
- Machine Learning libraries (RandomForestClassifier, SMOTE, e.c.)
- FastAPI for API development


## Usage

Once the server is running, you can access the API documentation at `http://localhost:8000/docs`. This Swagger UI allows you to test the API endpoints directly from your browser.

To make a prediction, send a POST request to the `/predict` endpoint with the asteroid data in JSON format.


## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NASA for providing the asteroid data
- The open-source community for the amazing tools and libraries used in this project
