from . import router

class Task(router.Router):
    ROUTES = {
      'all':{
        'method': "get",
        'path': "/"
      },
      'create':{
        'method': "post",
        'path': "/"
      },
      'find':{
        'method': "get",
        'path': "/:id"
      },
      'patch':{
        'method': "patch",
        'path': "/:id"
      },
      'put':{
        'method': "put",
        'path': "/:id"
      },
      'find_by_project':{
        'method': "get",
        'path': "/project/:project_id"
      },
    }