
from django.core.management.base import BaseCommand, CommandError

import requests
import baslerbauer_main.models as models
import baslerbauer_main.openfarms as openfarms

class Command(BaseCommand):
    help = 'Synchronise farms and produces with openfarms'

    def sync_objects(self, object_urls, model):
        all_urls = list(map(lambda f: f['meta']['detail_url'], object_urls))

        for p in model.objects.all():
            if p.open_farms_url in all_urls: # already exists; we are ok
                all_urls.remove(p.open_farms_url) # remove so we dont add it later
            else: # the Produce does not exist anymore
                print("Warning, {} does not exist anymore".format(p.open_farms_url))

        # now, all farms that are still in all_farm_urls need to be created
        for urls in all_urls:
            print("Found new: {}".format(urls))
            p = model.objects.create(open_farms_url=urls)
            p.save()
        
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

