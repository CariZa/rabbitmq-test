# rabbitmq-test

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