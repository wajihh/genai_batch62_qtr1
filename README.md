# Class 07 Basics of Markdown file in github 
    Explanation starts by Mr Qasim at 1 Hour 20 mins in video
Running a Jupyter Notebook with a "Hello World" Python example via a Dev Container using Docker involves several steps. Below is a guide to setting this up:

### 1. Install Docker and VS Code
Ensure you have Docker and Visual Studio Code (VS Code) installed on your machine. Install the "Dev Containers" extension in VS Code.

### 2. Create a Project Directory
Create a new directory for your project:

```bash
mkdir jupyter-dev-container
cd jupyter-dev-container
```

### 3. Create a Dockerfile
In your project directory, create a `Dockerfile` to define the environment for your Dev Container. The following `Dockerfile` sets up a Python environment with Jupyter installed:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /workspace

# Install Jupyter Notebook
RUN pip install jupyter

# Expose the port Jupyter Notebook will run on
EXPOSE 8888

# Run Jupyter Notebook on container startup
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
```

### 4. Create a Dev Container Configuration
In your project directory, create a `.devcontainer` directory with a `devcontainer.json` file to configure the Dev Container:

```bash
mkdir .devcontainer
cd .devcontainer
```

Create the `devcontainer.json` file:

```json
{
    "name": "Jupyter Dev Container",
    "dockerFile": "../Dockerfile",
    "context": "..",
    "appPort": [8888],
    "extensions": [
        "ms-python.python"
    ],
    "postCreateCommand": "pip install --upgrade pip"
}
```

### 5. Create a Simple "Hello World" Jupyter Notebook
Create a `notebooks` directory in your project and add a simple "Hello World" notebook:

```bash
mkdir ../notebooks
```

Create a file `hello_world.ipynb` inside the `notebooks` directory with the following content:

```json
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c62c25e",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Hello, World!\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

### 6. Open the Project in a Dev Container
1. Open VS Code in your project directory.
2. Press `Ctrl+Shift+P` and select "Dev Containers: Reopen in Container."
3. VS Code will build and start the container based on your `Dockerfile` and `devcontainer.json`.

### 7. Access the Jupyter Notebook
Once the container is running:

1. VS Code will forward port 8888, so Jupyter Notebook will be accessible from your browser.
2. Open the terminal in VS Code (inside the container) and run:

   ```bash
   jupyter notebook --ip=0.0.0.0 --no-browser --allow-root --notebook-dir=/workspace/notebooks
   ```

3. The terminal will display a URL with a token. Open this URL in your browser to access Jupyter Notebook.

4. You should see the `hello_world.ipynb` notebook in the Jupyter interface. Open it and run the cell to see "Hello, World!" printed.

### Summary
- **Dockerfile**: Sets up the Python environment with Jupyter.
- **devcontainer.json**: Configures VS Code to use the Docker container.
- **hello_world.ipynb**: Simple Jupyter notebook with a "Hello, World!" example.

This setup allows you to use a Docker-based environment to run Jupyter Notebooks inside a Dev Container in VS Code.


