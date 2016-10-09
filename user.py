from . import router

class User(router.Router):
    ROUTES = {
      'all':{
        'method': "get",
        'path': "/"
      },
      'create':{
        'method': "post",
        'path': "/"
      },
      'delete':{
        'method': "delete",
        'path': "/:id"
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
    }