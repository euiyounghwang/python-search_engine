
### Python-Elasticsearch

I will use this project as a basic api for building and searching with Elasticsearch 
- Build Docker for creating an index with sample metrics and searching with Elasticsearch
- Also run local environment with this project
- Build Docker Instance for testing with pytest

#### Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

#### Using Python Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

#### Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies with basic library:
```bash
poetry config virtualenvs.in-project true
poetry init
poetry add fastapi
poetry add uvicorn
poetry add pytz
poetry add elasticsearch==7.9.0
poetry add numpy
poetry add pytest
poetry add python-dotenv
```

#### Install this proejct to make an environment using Poetry Dependency
```bash
source .venv/bin/activate
poetry install
```

#### Install Elasicsearch Cluster based on Docker
- Single Node ES with Kibana
```bash
docker run --name kibaba-run --network bridge -e "ELASTICSEARCH_URL=http://host.docker.internal:9209" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" -e "ELASTICSEARCH_HOSTS=http://host.docker.internal:9209" -p 5801:5601 docker.elastic.co/kibana/kibana:7.9.0
docker run --name es8-run --network bridge -p 9209:9200 -p 9114:9114 -p 9309:9300 -e "http.cors.enabled=true" -e "http.cors.allow-origin=\"*\"" -e "http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization" -e "http.cors.allow-credentials=true" -e "xpack.security.enabled=false" -e "discovery.type=single-node" -e "ES_JAVA_OPTS=-Xms2g -Xmx2g" docker.elastic.co/elasticsearch/elasticsearch:7.9.0
```
- Multiple Nodes ES with Kibana : Build & create instances using `./docker-compose.yml`


#### Run Local Environment
- It will be validate the status of elasticsearch cluster using `./wait_fo_es.sh` and `./DevOps_Shell/read_config.sh` for reading es host value automatically when running `./service_start.sh` script.
```bash
source .venv/bin/activate
(.venv) ➜  python-elasticsearch git:(master) ✗ ./service_start.sh
get_value_from_yaml ->  http://localhost:9209
ElasticSearch is up
INFO:     Will watch for changes in these directories: ['/Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch']
WARNING:  "workers" flag is ignored when reloading is enabled.
INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)
INFO:     Started reloader process [17469] using StatReload
[2023-12-09 20:36:18,420] [INFO] [injector] [read_config_yaml] {
  "app": {
    "es": {
      "es_host": "http://localhost:9209",
      "index": {
        "alias": "metrics_search"
      }
    }
  }
}
[2023-12-09 20:36:18,421] [INFO] [config] [__init__] @@self.hosts - http://localhost:9209
INFO:     Started server process [17471]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Pytest
```bash
(.venv) ➜  python-elasticsearch git:(master) ./pytest.sh 
============================================= test session starts ==============================================
platform darwin -- Python 3.9.7, pytest-7.4.3, pluggy-1.3.0 -- /Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch/tests
configfile: pytest.ini
plugins: cov-4.1.0, anyio-3.7.1
collected 7 items                                                                                              

tests/test_api.py::test_skip SKIPPED (no way of currently testing this)                                  [ 14%]
tests/test_api.py::test_api PASSED                                                                       [ 28%]
tests/test_api.py::test_CRUD_api PASSED                                                                  [ 42%]
tests/test_elasticsearch.py::test_elasticsearch PASSED                                                   [ 57%]
tests/test_elasticsearch.py::test_indics_analyzer_elasticsearch PASSED                                   [ 71%]
tests/test_elasticsearch.py::test_search_elasticsearch SKIPPED (no way of currently testing this)        [ 85%]
tests/test_elasticsearch.py::test_api_es_search SKIPPED (no way of currently testing this)               [100%]
```