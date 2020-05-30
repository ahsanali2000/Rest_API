import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO

from local.api.serializers import StatusSerializer
from local.models import Status

obj = Status.objects.first()
serializer = StatusSerializer(obj)
jsondata = JSONRenderer().render(serializer.data)
print(jsondata)

stream = BytesIO(jsondata)
data = JSONParser.parse(stream)
print(data)

# same work as BytesIO do
print(json.loads(jsondata))

qs = Status.objects.all()
serializer2 = StatusSerializer(obj, many=True)
jsondata2 = JSONRenderer().render(serializer2.data)
print(jsondata2)

stream2 = BytesIO(jsondata2)
data2 = JSONParser.parse(stream2)
print(data2)

# same work as BytesIO do
print(json.loads(jsondata2))

# create data
data = {'content': 'new addition of data','user':1}
serializer = StatusSerializer(data=data)
serializer.is_valid()

if serializer.is_valid():
    serializer.save()

# update data
obj = Status.objects.first()
data = {'content': 'data is updated','user':1}
update_serializer = StatusSerializer(obj, data)
update_serializer.is_valid()
if update_serializer.is_valid():
    update_serializer.save()

#delete data
obj=Status.objects.last()
obj.delete()