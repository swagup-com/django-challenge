# django-challenge

Task1:


We have create, list and retrieve features but lack the ability to update. Introduce a new `PUT` endpoint at `/api/v1/accounts/{id}/` that receives a JSON body containing `phone`, `shipping_address1`, `shipping_address2`, `shipping_city`, `shipping_state`, `shipping_zip`,
`shipping_country`. The feature should update the existing record and return a JSON body representing the new state of the account item.


Solution:


Task2:


Also add a way to filter accounts by `shipping_country` in the admin interface


Solution:


Task3:


Besides write a view responding to a `GET` to path `/api/v1/fizz-buzz/?x=25` that will write the results of running FizzBuzz program for numbers from 1 to x. 
Looping them but for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. If the number is not divisible for three or five write the number.
As you can see x is a querystring param and by default this number should be 100. The response will be a json with the following format:

{"x": 100, "fizzbuzz": "here comes the result of your algorithm"}

Solution: