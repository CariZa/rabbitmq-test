# rabbitmq-test


## Setup rabbitmq

Run a rabbitmq docker container:

    $ docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 -p 5672:5672 -p 5671:5671 rabbitmq:3-management

Note the port 5672 is what is used in udemy-example1.py & udemy-example2.py

View Dashboard:

    http://localhost:8080


## Setup python environment with virtualenv

Setup environment env

    $ virtualenv env

Activate virtualenv

    $ source env/bin/activate

Install requirements

    $ pip install -r requirements.txt

## Run python code using pika library

Currently the working examples are in the "working-examples" folder

Run these two together:

#### Subscribe/Consumer script

    $ python working-examples/udemy/udemy-example1.py

You will see:

     [*] Waiting for message. Press CTRL + C to exit.

#### Publish script

    $ python working-examples/udemy/udemy-example2.py

You won't see feedback in this console, you'll see the feedback in the above consumer's console:

    [x] Received 'Message number 1'
    [x] Received 'Message number 2'
    [x] Received 'Message number 3'
    [x] Received 'Message number 4'
    [x] Received 'Message number 5'
    [x] Received 'Message number 6'
    [x] Received 'Message number 7'
    [x] Received 'Message number 8'
    [x] Received 'Message number 9'
    [x] Received 'Message number 10'
    [x] Received 'Message number 11'
    [x] Received 'Message number 12'
    [x] Received 'Message number 13'
    [x] Received 'Message number 14'
    [x] Received 'Message number 15'