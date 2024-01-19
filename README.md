# StudyBuddy-App

## quering data

queryset = ModelName.objects.all()
queryItem = ModelName.objects.exclude(attribute='value')

## Filtering

queryset = ModelName.objects.filter(attribute='value')
queryset = ModelName.objects.filter(attribute\_\_startswith='value')
queryset = ModelName.objects.filter(attribute\_\_contains='value')
queryset = ModelName.objects.filter(attribute\_\_icontains='value')
queryset = ModelName.objects.filter(attribute\_\_gt='value')
queryset = ModelName.objects.filter(attribute\_\_gte='value')
queryset = ModelName.objects.filter(attribute\_\_lt='value')
queryset = ModelName.objects.filter(attribute\_\_lte='value')
queryItem = Project.objects.filter(attribute='value').order_by('value1', 'value2')
queryItem = Project.objects.filter(attribute='value').order_by('-value1', '-value2')

## Creating

queryItem = ModelName.objects.create(attribute='value')

## updating

item = ModelName.objects.get(attribute='value')
item.title = 'New Value'
item.save()

## deleting

item = ModelName.objects.get(attribute='value')
item.delete()
item = ModelName.objects.last()
item.delete()

## Query Models Children

item = ModelName.objects.first()
item.childmodel_set.all()

3:08:00
