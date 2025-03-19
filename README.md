# Image-Place-Holder-Service
This service generates placeholder images in SVG format for use in websites and prototypes. To use it, specify the desired dimensions in the URL and optional query parameters for text, background color, and text color.

# Why
Over the years, I’ve had to replace so many online placeholder image services that I finally hit my breaking point. First, I used placeholder.com. Then, when the main site was replaced, their via service kept working—until it didn't. Other alternatives came and went, each disappearing when I needed them most.

There’s nothing worse than prepping a demo for a client and realizing all your placeholder images are broken because yet another service vanished overnight. Instead of finding yet another temporary fix, I decided to solve the problem for good.

I built my own placeholder image service—one designed to be reliable, open, and permanent. Not only is it freely available as a running service, but I also packaged it as a fully functional Docker image so anyone can deploy their own version, extend it, or contribute back. No more sudden outages. No more searching for alternatives. Just a simple, self-hostable solution that will always be there when you need it.

Its also great as a self contained docker application amnd a base setup for FastAPI.

If you’ve ever been burned by broken placeholder images, check it out. Feedback and contributions are welcome!
