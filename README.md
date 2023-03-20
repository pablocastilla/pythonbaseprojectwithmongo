# Goal
python skeleton with repositories, dependency injection, tests and a model in a mongo db.

# Steps for setting up
- create venv with pipenv
- install pre-commit hooks with `pre-commit install`
- https://pre-commit.com/
- docker run -d -p 27017:27017 --name mongo -v mongo-data:/data/db mongo:latest
