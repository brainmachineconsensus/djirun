# Djirun: Django Project Setup CLI


**Djirun: Simplify and Supercharge Your Django Setup!**

Djirun is a powerful, streamlined CLI tool that takes the hassle out of setting up Django projects. Whether you’re starting fresh or adding new configurations to an existing project, Djirun empowers developers by automating essential project setups with just a few commands.

Imagine setting up a Django project with a fully customizable structure, equipped with your preferred CSS framework, database support, single-page app capability, Docker configurations, and much more—all tailored to your needs in minutes. Djirun’s flexibility means you’re no longer limited by default configurations, giving you the freedom to structure your projects exactly as you envision.

## Why Choose Djirun?

- **Boost Your Workflow**: Get your Django project up and running faster than ever before.
- **Tailored Configurations**: Choose your CSS framework, database, static file setup, and even set up a REST API—all with simple options.
- **Seamless Docker Integration**: Bring Docker support effortlessly for modern, containerized deployments.
- **Focus on Development**: With setup taken care of, dive right into building features without the configuration fuss.

Start with Djirun today and turn project setups into a quick, efficient experience. Your perfect Django project is just a command away!

## Features

- **Static File Structure**: Option to create a structure for static files.
- **CSS Framework Integration**: Choose between Bootstrap, Tailwind, or none.
- **Single Page Application**: Easily set up a single-page application.
- **Database Support**: Use SQLite or PostgreSQL.
- **Authentication**: Enable user authentication from the start.
- **REST API**: Integrate Django REST framework to build APIs.
- **Docker Support**: Create a Docker configuration for containerization.

## Installation

**Clone the Repository**:

   ```bash
   git clone https://github.com/brainmachineconsensus/djirun.git
   cd djirun
   ```

   Install Dependencies:

   ```bash
   pip install click
   pip install rich
   ```

## Usage

You can use Djirun to create and configure a Django project from the command line. Here’s how to use the CLI tool:

   ```bash
   python cli.py <project_name> [OPTIONS]
   ```
## Options:

- **--css-framework**: Specify the CSS framework to use (options: bootstrap, tailwind, none).
- **--static-structure / --no-static-structure**: Create a structure for static files.
- **--single-page / --no-single-page**: Set up a single-page application.
- **--database**: Choose the database (options: sqlite, postgres).
- **--docker / --no-docker**: Add or skip Docker configuration.
- **--python-version**: Specify the Python version for Docker (e.g., 3.8).

## Create a Project

To create a Django project named "myproject" with Bootstrap, a static file structure, and Docker support:

   ```bash
   python cli.py myproject --css-framework bootstrap --static-structure --docker
   ```

## Start Developing

Navigate to Your Project Directory: Once Djirun completes setup, you can move into your new project’s directory.

Start the Django Server: Use Django’s development server to begin building your application:

   ```bash
   python manage.py runserver
   ```

Access Your Application: Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see your new Django project in action.

## Contribute

Feel free to contribute to Djirun by submitting issues or pull requests. Please follow standard GitHub contribution guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for details.