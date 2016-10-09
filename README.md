# ramassage_epitech_helper
Helper pacakge to use api.ramassage.epitech.eu
V1, It needs a lot of improvment

## How to use it

You must create a settings.json file like this one:
```json
{
  "UUID": "uuid",
  "SECRET": "secret"
}
```

Example:
```python
from ramassage.project import Project

print(Project().request('find_by_slug', {}, project_slug))
```

## More

I didn't read any api doc for api.ramassage.epitech.eu, if you have any problem please tell me.
You might need to contact [Steven MARTINS](https://github.com/steven-martins) to get your credentials (not sure)
