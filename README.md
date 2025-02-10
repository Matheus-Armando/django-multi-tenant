# README.md

# Django Multi-Tenant Project

This project is a Django application designed to support multi-tenancy. It provides a structure for managing multiple tenants within a single application instance.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd django-multi-tenant
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your environment variables, such as:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage Guidelines

- The application supports multiple tenants, allowing you to manage tenant-specific data and configurations.
- Refer to the `tenants` app for tenant management and middleware for tenant resolution.
- Customize the `config/settings` files for different environments (local, production).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.