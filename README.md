# Image-Place-Holder-Service
## Summary

This service generates placeholder images in SVG format for use in websites and prototypes. To use it, specify the desired dimensions in the URL and optional query parameters for text, background color, and text color.

## About
This solution ensures you always have a working system, along with the code to run your own version if needed. Use our hosted service at [iph.lets.qa](https://iph.lets.qa) or deploy your own using the provided Docker image.

It's also a great self-contained Docker application and a base setup for FastAPI.

We welcome feedback and contributions! If you have ideas for improvements, feel free to contribute.

---

## Building and Running with Docker
This service is packaged as a Docker container for easy deployment. Follow the steps below to build and run the container:

### Prerequisites
- Install [Docker](https://www.docker.com/) on your system.

### Build the Docker Image
1. Navigate to the directory containing the `Dockerfile`.
2. Run the following command to build the Docker image:
   ```bash
   docker build -t image-placeholder-service .
   ```

### Run the Docker Container
Start the container using the following command:
```bash
docker run -d -p 8000:80 image-placeholder-service
```
- The `-d` flag runs the container in detached mode (in the background).
- The `-p 8000:80` flag maps port 8000 on your host to port 80 in the container.

### Access the Service
Open your browser and go to:
[http://localhost:8000/](http://localhost:8000/)

## Example Endpoints

### Generate a 300x100 placeholder:
```
http://localhost:8000/300x100
```

### Generate a square placeholder with custom text:
```
http://localhost:8000/400?text=Custom+Text
```

### Generate a placeholder with custom colors:
```
http://localhost:8000/600x200?text=Hello&bg=ff0000&color=ffffff
```

See more examples at: [https://iph.lets.qa](https://iph.lets.qa)

