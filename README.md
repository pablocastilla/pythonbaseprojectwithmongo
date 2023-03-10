# create venv

# mongo data access
docker run -d -p 27017:27017 --name mongo -v mongo-data:/data/db mongo:latest



# ORM:
MongoEngine

# mongomock
http://docs.mongoengine.org/guide/mongomock.html