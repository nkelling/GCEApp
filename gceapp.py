from datetime import datetime
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
import os


class GceApp:

    def __init__(self, projectname, keyname):
        self.projectname = projectname
        self.keyname = keyname
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys/' + self.keyname
        self.credentials = GoogleCredentials.get_application_default()
        self.service = build('compute', 'v1', credentials=self.credentials)
        self.instancelist = []

    def __del__(self):
        print "cleaning up {}".format(self.keyname)

    def list_instances(self):
        request = self.service.instances().aggregatedList(project=self.projectname)
        while request is not None:
            response = request.execute()

            for zonename, instances_scoped_list in response['items'].items():
                # TODO: Change code below to process each (name, instances_scoped_list) item:
                try:
                    for instance in instances_scoped_list['instances']:
                        print "{} - {} - {} - {}".format(datetime.now().time(),
                                                         zonename,
                                                         instance['name'],
                                                         instance['status'])
                        self.instancelist.append(instance)
                except KeyError:
                    # print(zonename, instances_scoped_list['warning'])
                    continue

            request = self.service.instances().aggregatedList_next(previous_request=request, previous_response=response)

    def start_instances(self):
        for instance in self.instancelist:
            zone = instance['zone'].rsplit('/', 1)
            if instance['status'] != 'RUNNING':
                request = self.service.instances().start(project=self.projectname,
                                                         zone=zone[1],
                                                         instance=instance['name'])
                response = request.execute()






