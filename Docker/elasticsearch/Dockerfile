FROM docker.elastic.co/elasticsearch/elasticsearch:7.10.0

RUN elasticsearch-plugin install analysis-icu
RUN elasticsearch-plugin install analysis-phonetic
RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-nori
RUN elasticsearch-plugin install -b https://github.com/vvanholl/elasticsearch-prometheus-exporter/releases/download/7.10.0.0/prometheus-exporter-7.10.0.0.zip

# COPY elasticsearch_config ./config