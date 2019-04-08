# bills-of-materials

Example of a bills of materials, I will asume that you have a correct installation of python3 in your machine. This project was created on Manjaro 18.0.4, but It should works rigth on any machine with python.

## Project Setup

1. Install all the required software(git, pip, virtualenv):

    ```sh
    $ sudo pacman -S git
    $ sudo pacman -S python3-pip
    $ sudo pip install virtualenv
    ```

2. Clone the project on your machine:

    ```sh
    $ git clonegit@github.com:labrank/bills-of-materials.git
    ```
3. Create a virtualenv and install required dependencies:
    ```sh
    $ cd bills-of-materials
    $ virtualenv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    ```
4. Run your project:
    ```sh
    python -m flask run
    ```
4. have fun.

## API Usage

Here is a list of available calls, but is prefered to install and use **postman**, here is a simple documetation of the API on postman:
 ```
https://documenter.getpostman.com/view/3248743/S1EKzfYj
 ```
 Or, you can import to your own installation using this url:
 ```
 https://www.getpostman.com/collections/d016f0f569da671dd278
  ```
