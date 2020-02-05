# django-challenge
Django Coding Challenge for API developer candidates

Hello, and welcome to the Django coding challenge! You'll find a set of instructions below that you must attempt to complete within 3 days. Clone this repository to start the challenge, and good luck! When completed, push your solution to a new repository, and send us a link.

Within this repository, you will find a simple application with the ability to create and list accounts.

Here are some things we need help with:

We have create and list features but lack the ability to update. Introduce a new PUT endpoint at /accounts/{id} that receives a JSON body containing phone, shipping_address1, shipping_address2, shipping_city, shipping_state, shipping_zip,
shipping_country. The feature should update the existing record and return a JSON body representing the new state of the account item.

You may notice the lack of tests in the repo, maybe set a good example and add tests to your method if you have time. That way the other devs can copy-paste from your good example. Once done, go ahead and open a pull request again the repo.

Good luck again.
