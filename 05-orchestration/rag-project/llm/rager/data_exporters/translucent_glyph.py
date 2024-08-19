if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

from elasticsearch import Elasticsearch
from mage_ai.data_preparation.variable_manager import get_global_variable

search_query = {
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": "When is the next cohort?",
                    "fields": ["question", "text"],
                    "type": "best_fields"
                }
            }
        }
    }
}

@data_exporter
def export_data(data, *args, **kwargs):
    es_client = Elasticsearch('http://rag-project-elasticsearch-1:9200') 
    index_name = get_global_variable('numinous_eon', 'index_name')
    response = es_client.search(index=index_name, body=search_query)
    result_docs = []
    
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
        print(hit['_score'])

    print(result_docs)
    return result_docs

