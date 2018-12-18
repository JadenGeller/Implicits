# Implicits
Global state can be hard to reason about, but piping dependencies from function to function is a pain. With implicits, you _explicitly_ which function parameters are _implicit_ dependencies. When you call the function, no need to explicilty provide these parameters; instead, the parameters will be implicitly passed! All that's required is that there exists local variables in scope that match the names of the parameters you're calling.
```python3
@implicits("current_user")
def create_task(title, *, current_user):
    print(f"{current_user} created a task titled '{title}'")
    
current_user = "Jaden"
create_task("Hooray, a task!") # Jaden created a task titled 'Hooray, a task!'
create_task("Buy some trackpants") # Jaden created a task titled 'Buy some trackpants'
```

## Usage
1) Install via `pip install implicits`.
2) Import with `from implicits import implicits`.
3) Decorate using `@implicits("names", "of", "implicit", "parameters")`.

## Example
```python3
import logging
import boto3

from implicits import implicits

class Giraffe:
    @implicits("logger")
    def __init__(self, name, *, logger):
        self.name = name
        logger.info(f"Creating a Giraffe named {name}")
    
    @property
    @implicits("logger")
    def full_name(self, *, logger):
        logger.info(f"Getting {self.name}'s full name")
        return f"{self.name} the Giraffe"
    
    @property
    @implicits("food")
    def is_hungry(self, *, food):
        return "leaves" in food

@implicits("logger")
def main(*, logger):
    jeff = Giraffe("Jeff") # Creating a Giraffe named Jeff
    name = jeff.full_name  # Getting Jeff's full name
    food = ["rocks", "dirt"]
    logger.info(jeff.is_hungry) # False
    food.append("leaves")
    logger.info(jeff.is_hungry) # True
    
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

main()
```

## References

I didn't invent this idea! Quite a few other languages support implicit parameters. The most mainstream of these languages is Scala. [Check out how implicits work in Scala!](https://docs.scala-lang.org/tour/implicit-parameters.html)
