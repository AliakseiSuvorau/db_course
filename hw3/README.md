# CouchDB & PouchDB

One can install CouchDB following [this](https://docs.couchdb.org/en/stable/install/unix.html#enabling-the-apache-couchdb-package-repository) guide.

First, we'll start with creating a docker container with CouchDB using [this](https://docs.oldtimes.me/docker/samples/library/couchdb/index.html#persistent-data) guide.

```shell
docker run -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password -p 5984:5984 -d --name couchdb couchdb
```

![alt text](images/create_container.jpg)

Now that we have our container running, we can visit `http://127.0.0.1:5984/_utils/`. Here we should log in using login `admin` and password `password`.

![alt text](images/login.jpg)

To create a new database, press `Create Database` button and type the name of a database.

![alt text](images/create_db.jpg)

To add a new document, press `New Document` button and enter a json you want to add. Then press `Create Document`.

![alt text](images/new_doc.jpg)

To be able to connect to our database we need to make sure CORS are put correctly. For this time, we simply make the database accessible for all domains.

![alt text](images/CORS.jpg)

Now we can alter `hw3.html` file: we'll replace 25th line with

`Remote: new PouchDB('http://admin:password@localhost:5984/hw3_database')`

After that, we can open this page and press `Sync` button. Now the document from a database is displayed.

![alt text](images/sync.jpg)

Let's stop the CouchDB container and make sure that the document will still be displayed on the page.

![alt text](images/stop_container.jpg)

After reloading and pressing `Sync` button, we see that the document is still on the screen.

![alt text](images/reload_sync.jpg)

To delete stopped container, type:
```shell
docker container rm <container_id>
```

**Conclusion**: the data was synchronized between remote CouchDB and local PouchDB.

Result: [here](result.html).