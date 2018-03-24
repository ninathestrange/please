#This is where the ElasticSearch code live.

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Integer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class LeadIndex(DocType):
    author = Text()
    project = Text()
    posted_date = Date()
    business_website = Text()
    first_name = Text()
    second_name = Text()
    corporate_email = Text()
    industry = Text()
    corporate_phone_number = Integer()
    company_size = Text()
    state = Text()
    country = Text()

    class Meta:
        index = 'lead-index'

def bulk_indexing():
    LeadIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.LeadPost.objects.all().iterator()))
