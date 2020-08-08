import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os
import ssl

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighborlydb:P1EMBiciV2pQn04yAl6k3WLGP7nlVIubRftgTkLDRUkA5QPnPMHL1DhnxXX2sB53XtzgG2GBOGDT96nggzgLqA==@neighborlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlydb@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url,  ssl_cert_reqs=ssl.CERT_NONE)
        database = client['neighborly']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

