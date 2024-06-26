# Stock Market Data

## Description

This repository contains the source code for the Janata WiFi Task backend project. It is built using Django and is designed to perform CRUD operation on stocks data.

## Features

- CRUD operations for managing stocks
- Pagination

## Installation

1. Clone the repository: `git clone https://github.com/SelimRejabd/Stock-Market-Data`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Usage

1. Access the application at `http://localhost:8000/`
2. Get stocks data from Json file `api/stocks/`
3. Get stocks data from database `api/stocks-data/`
4. Get single stock data from database `api/stocks-data/<int:pk>/`
4. Add new stock data `api/stocks-data/add/`
5. Edit stock data `api/stocks-data/update/<int:pk>/`
6. Delete stock data `api/stocks-data/delete/<int:pk>/`


## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
