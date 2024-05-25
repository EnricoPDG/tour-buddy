## Tour Buddy

Tour Buddy is a web application that connects tour guides with tourists, making it easier to discover and schedule personalized tours.

### Overview

Tour Buddy is a platform developed to help tourists find local tour guides in various cities. It allows users to search for guides based on their destination preferences, availability dates, and desired type of experience.

### Technologies Used

Tour Buddy is built using the following technologies:

- **Python**: For backend development.
- **FastAPI**: A fast web framework for APIs in Python.
- **SQLAlchemy**: An SQL library for Python.
- **HTML/CSS/JavaScript**: For frontend development.

### How to Run the Project

To run Tour Buddy locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local environment using the following command:

    ```bash
    git clone https://github.com/EnricoPDG/tour-buddy.git
    ```

2. **Set Up the Virtual Environment**: Navigate to the project directory and create a virtual environment:

    ```bash
    cd tour-buddy
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**: Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies**: Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up the Database**: Configure the PostgreSQL database according to the settings defined in the `.env` file.

6. **Run the Application**: Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

7. **Access the Application**: Open a web browser and go to `http://localhost:8000` to view the Tour Buddy application.

### Contribution

Contributions are welcome! Feel free to open issues and submit pull requests to improve the project.

### License

This project is licensed under the terms of the [MIT License](LICENSE).

