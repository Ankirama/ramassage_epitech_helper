from . import router

class Template(router.Router):
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
      'find_by_slug':{
        'method': "get",
        'path': "/slug/:slug_id"
      },
    }