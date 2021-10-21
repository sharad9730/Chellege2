
import boto3
from botocore.config import Config

CREDENTIALS_FILE = ""
credentials = {
    "client_id": "xyzzz",
    "secret": "abcccc"
}
class AwsUtils(object):
    """AWS utils class for all aws call"""

    def _init_(self, credentials=None, region="us-west-2"):

        self.boto_config = Config(retries=dict(max_attempts=15))
        self._session = boto3.Session(
            aws_access_key_id=credentials["client_id"],
            aws_secret_access_key=credentials["secret"])

        self._region = region
        self._ec2_resource = None

    @property
    def ec2_resource(self):
        if not self._ec2_resource:
            self._ec2_resource = self._session.resource(
                'ec2', region_name=self._region, config=self.boto_config)
        return self._ec2_resource

    def get_instance(self, instance_id):
        return self.ec2_resource.Instance(instance_id)

obj = AwsUtils(credentials=credentials)
obj.get_instance("id-intance_id_test")   
