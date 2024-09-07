# Flask Demo App Documentation

## Overview

The Flask Demo App is a simple web application built using Flask, showcasing fundamental features such as form handling, template rendering, and static file usage. The application allows users to input their name through a form and displays a personalized greeting based on the provided input.

## Project Structure

```
flask_demo/
├── static/
│   ├── style.css
├── templates/
│   ├── index.html
│   ├── hello.html
└── app.py
```

### Folder Descriptions

- `static/`: Contains static files such as CSS, JavaScript, and images used for styling the application.
- `templates/`: Contains HTML template files for rendering dynamic content.
- `app.py`: The main Python file that contains the Flask application code.

## Setup and Installation

1. **Install Flask**

   Ensure you have Flask installed. You can install it using pip:

   ```bash
   pip install Flask
   ```

2. **Project Setup**

   Clone or download the project files and navigate to the project directory:

   ```bash
   cd flask_demo
   ```

3. **Run the Application**

   Start the Flask development server by running:

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Application Functionality

### Home Page

- **URL:** `/`
- **Method:** GET
- **Description:** Displays a form where users can enter their name.
- **Form Fields:**
  - `name` (text input, required)

### Greeting Page

- **URL:** `/hello`
- **Method:** POST
- **Description:** Displays a personalized greeting message based on the name submitted through the form.
- **Form Data:**
  - `name` (text input)

## Templates

### `templates/index.html`

- **Description:** The home page template that includes a form for user input.
- **Features:**
  - Form submission to the `/hello` route.
  - Link to the static CSS file for styling.

### `templates/hello.html`

- **Description:** The greeting page template that displays a personalized message.
- **Features:**
  - Displays a dynamic greeting message using the `name` variable.
  - Provides a link to return to the home page.

## Static Files

### `static/style.css`

- **Description:** CSS file used for styling the application.
- **Styles:**
  - Basic styling for body, headers, form elements, and links.
