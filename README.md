## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Pasindu-Vishmika/Todo-List-App.git
    ```

2. Install the necessary dependencies, such as PIL (Python Imaging Library). You can install dependencies using pip:

    ```bash
    python -m pip install django
    python -m pip install djangorestframework
    python -m pip install django-cors-headers

    ```
3. Go to Project Dir 
    ```bash
    cd Todo-List-App
    ```

4. Use this Command to activate Server  

    ```bash
    python manage.py runserver
    ```
# Running Django Application with Docker

This guide provides instructions for running a Django application using Docker. Follow the steps below to get your application up and running in a Docker container.


## Prerequisites

- Ensure you have Docker installed on your system. You can download Docker from [here](https://www.docker.com/get-started).

## Instructions

### 1. Build the Docker Image

Navigate to the root directory of your Django project where the `Dockerfile` is located. Run the following command to build the Docker image. You can change name of your image name by replace **my-django-app** with the name you want to give your Docker image.

```bash
    docker build -t my-django-todo-app .
```


### 2. Run the Docker Container

After building the Docker image, run a Docker container using the image with the following command:

```bash
    docker run -p 8000:8000 my-django-todo-app
```
If you need give a name to the container you can do it by adding `--name` tag.Replace **my-todo-app** with the name you want to give your Docker container

```bash
    docker run --name my-todo-app -p 8000:8000 my-django-todo-app
```

This command maps port `8000` on your host machine to port `8000` in the Docker container. You can now access your Django application in your web browser at `http://localhost:8000`.

### 3. Additional Commands

If you need to run management commands such as migrations or creating a superuser, use the following commands:

- **Run Migrations:** Replace **my-django-app** with your own image name.


```bash
    docker run my-django-todo-app python manage.py migrate
```
- **Create a Superuser:** *(noted you must do migration command before creating superuser)*. Replace **my-django-app** with your own image name.

```bash
    docker run -it my-django-app python manage.py createsuperuser
```

### 4. Stop and Remove Containers

To stop the running container. Replace `container_id` with own container id

```bash
    docker stop <container_id>
```

To remove the stopped container. Replace `container_id` with own container id

```bash
    docker rm <container_id>
```
