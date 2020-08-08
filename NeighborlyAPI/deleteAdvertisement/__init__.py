import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import ssl


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborlydb:P1EMBiciV2pQn04yAl6k3WLGP7nlVIubRftgTkLDRUkA5QPnPMHL1DhnxXX2sB53XtzgG2GBOGDT96nggzgLqA==@neighborlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlydb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url,  ssl_cert_reqs=ssl.CERT_NONE)
            database = client['neighborly']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
