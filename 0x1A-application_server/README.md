## Application server

#### Task 0
Let’s serve what you built for AirBnB clone v2 - Web framework on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.
Requirements:
- Install the `net-tools` package on your server: `sudo apt install -y net-tools`
- Git clone your `AirBnB_clone_v2` on your `web-01` server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`.
- Your Flask application object must be named `app`

#### Task 1
Now that you have your development environment set up, let’s get your production application server set up with `Gunicorn` on `web-01`, port `5000`. You’ll need to install `Gunicorn` and any libraries required by your application. Your `Flask` application object will serve as a `WSGI` entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.
Requirements:
- Install `Gunicorn` and any other libraries required by your application.
- The Flask application object should be called `app`.
- You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a `Gunicorn` instance to localhost listening on port `5000` with your application object as the entry point.
- In order to check your code, the checker will bind a `Gunicorn` instance to port `6000`, so make sure nothing is listening on that port.

#### Task 2
Building on your work in the previous tasks, configure `Nginx` to serve your page from the route `/airbnb-onepage/`
Requirements:
- `Nginx` must serve this page both locally and on its public IP on port `80`.
- `Nginx` should proxy requests to the process listening on port `5000`.
- Include your `Nginx` config file as [2-app_server-nginx_config](2-app_server-nginx_config).

#### Task 3
Building on what you did in the previous tasks, let’s expand our web application by adding another service for `Gunicorn` to handle. In `AirBnB_clone_v2/web_flask/6-number_odd_or_even`, the route `/number_odd_or_even/<int:n>` should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure `Nginx` to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a `Gunicorn` instance listening on port 5001. The key to this exercise is getting `Nginx` configured to proxy requests to processes listening on two different ports.
Requirements:
- `Nginx` must serve this page both locally and on its public IP on port `80`.
- `Nginx` should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to the process listening on port `5001`.
- Include your `Nginx` config file as [3-app_server-nginx_config](3-app_server-nginx_config).

#### Task 4
Let’s serve what you built for AirBnB clone v3 - RESTful API on `web-01`.
Requirements:
- Git clone your `AirBnB_clone_v3`
- Setup `Nginx` so that the route /api/ points to a Gunicorn instance listening on port 5002
- `Nginx` must serve this page both locally and on its public IP on port 80
- To test your setup you should bind `Gunicorn` to `api/v1/app.py`
- Upload your `Nginx` config file as [4-app_server-nginx_config](4-app_server-nginx_config).
