from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

class MyJsonEncoder(DjangoJSONEncoder):
    """
    shell 에서의 사용방법
    from tutorial.my_json_encoder import MyJsonEncoder
    from django.contrib.auth.models import User
    import json
    data = User.objects.all()
    json.dumps(data, cls=MyJsonEncoder, ensure_ascii=False)
    '[{"id": 1}]'
    """
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, User):
            return {'id': obj.id}
        return super().default(obj)