# Chatnels

Chatnels is a real-time chat server built using Django and the Channels library. This project demonstrates how to create a scalable and efficient chat application with WebSocket support.

## Features

- Real-time messaging with WebSockets
- User authentication and authorization
- Chat rooms for group conversations
- Persistent message storage

## Requirements

- Python 3.8+
- Django 3.2+
- Channels 3.0+
- Redis (for channel layers)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatnels.git
    cd chatnels
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your browser and go to `http://127.0.0.1:8000/`.
2. Register a new user or log in with an existing account.
3. Create or join a chat room and start messaging in real-time.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Channels](https://channels.readthedocs.io/en/stable/)
- [Redis](https://redis.io/)
