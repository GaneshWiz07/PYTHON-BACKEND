# Simple Blog CRUD Application with Flask

![Flask](https://img.shields.io/badge/Flask-2.2.5-000000?style=flat&logo=flask)

A basic blog application demonstrating CRUD (Create, Read, Update, Delete) operations using Python Flask.

## Features
- Create new blog posts
- Read existing posts
- Update existing content
- Delete posts
- Responsive web interface

## Installation
1. **Prerequisites**
   - Python 3.8+
   - pip package manager

2. **Clone Repository**
   ```bash
   git clone https://github.com/GaneshWiz07/PYTHON-BACKEND.git
   cd PYTHON-BACKEND/SIMPLE\ BLOG\ POST\ -\ \(CRUD\)/
   ```

3. **Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

4. **Install Dependencies**
   ```bash
   pip install Flask
   ```

## Project Structure
```
SIMPLE BLOG POST - (CRUD)/
├── app.py                # Main application entry point
├── templates/            # HTML templates
│   ├── index.html        # Main blog listing
│   ├── create.html       # Post creation form
│   ├── edit.html         # Post editing form
│   └── post.html         # Individual post view
├── static/               # Static assets
│   └── css/
│       └── style.css     # Custom styles
└── .hintrc              # Code quality configuration
```

## Usage
1. **Run Application**
   ```bash
   python app.py
   ```

2. **Access in Browser**
   Visit [http://localhost:5000](http://localhost:5000)

## Dependencies
- Flask 2.2.5

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License
[ISC License](https://opensource.org/licenses/ISC)
