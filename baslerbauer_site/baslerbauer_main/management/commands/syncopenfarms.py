
from django.core.management.base import BaseCommand, CommandError

import requests
import baslerbauer_main.models as models
import baslerbauer_main.openfarms as openfarms

class Command(BaseCommand):
    help = 'Synchronise farms and produces with openfarms'

    def sync_objects(self, json_objects, model):
        object_map = { f['id']: f for f in json_objects }

        new_objects = []

        for p in model.objects.all():
            if p.openfarms_id in object_map: # already exists; we are ok
                del(object_map[p.openfarms_id]) # remove so we dont add it later
            else: # the Produce does not exist anymore
                print("Warning, {} with openfarms-id {} does not exist anymore".format(model.__name__, p.openfarms_id))

        # now, all farms that are still in all_farm_urls need to be created
        for data in object_map.values():
            new_objects.append(model.from_openfarms(data))

        # Bulk create all objects
        print("Found {} new {}.".format(len(new_objects), model.__name__))
        model.objects.bulk_create(new_objects)
        
    def handle(self, *args, **options):
        try:
            openfarms_farms = openfarms.list_farms()
            openfarms_produce = openfarms.list_produce()
        except requests.exceptions.Timeout:
            raise CommandError("A timeout occured while contacting openfarms")
        except requests.exceptions.TooManyRedirects:
            raise CommandError("Too many redirects while contacting openfarms")
        except requests.exceptions.RequestException as e:
            raise CommandError("Request exception {} while contacting openfarms".format(e))

        self.sync_objects(openfarms_farms, models.Producer)
        self.sync_objects(openfarms_produce, models.Product)

