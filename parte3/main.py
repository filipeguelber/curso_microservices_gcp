# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request
from google.cloud import datastore


def create_client(project_id):
    return datastore.Client(project_id)


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    username = request.args.get('username')
    password = request.args.get('password')
    saveUser(username,password)

    return 'Criando user= '+username+' pass='+password

def saveUser(username,password):
    print "deveria salvar",username," : ",password

def publishUser(username,password):
    # Instantiates a publisher client
    publisher = pubsub_v1.PublisherClient()

    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = subscriber.topic_path(project_id, topic_name)

    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    # Create the topic.
    topic = publisher.create_topic(topic_path)
    print('\nTopic created: {}'.format(topic.name))

    # Create a subscription.
    subscription = subscriber.create_subscription(
        subscription_path, topic_path)
    print('\nSubscription created: {}\n'.format(subscription.name))

    # Publish messages.
    data = {
        	'username': username,
        	'password': password
        }
    # Data must be a bytestring
    data = str(data).encode('utf-8')
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)
    print('Published {} of message ID {}.'.format(data, future.result()))





if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
