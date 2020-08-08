import logging
import azure.functions as func
import pymongo
import ssl
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighborlydb:P1EMBiciV2pQn04yAl6k3WLGP7nlVIubRftgTkLDRUkA5QPnPMHL1DhnxXX2sB53XtzgG2GBOGDT96nggzgLqA==@neighborlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlydb@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url,  ssl_cert_reqs=ssl.CERT_NONE)
        database = client['neighborly']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except Exception as e:
        logging.info(e)
        return func.HttpResponse("Bad Request", status_code=400)