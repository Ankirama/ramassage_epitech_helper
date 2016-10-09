from . import router

class Project(router.Router):
    ROUTES = {
        'current': {
            'method': "get",
            'path': "/"
        },
        'create': {
            'method': "post",
            'path': "/"
        },
        'find': {
            'method': "get",
            'path': "/:id"
        },
        'patch': {
            'method': "patch",
            'path': "/:id",
        },
        'put': {
            'method': "put",
            'path': "/:id",
        },
        'find_by_slug': {
            'method': "get",
            'path': "/slug/:slug",
        },
        'find_by_token': {
            'method': "get",
            'path': "/token/:token",
        },
        'past': {
            'method': "get",
            'path': "/past",
        },
        'all': {
            'method': "get",
            'path': "/all",
        },
        'find_current_by_login': {
            'method': "get",
            'path': "/user/:login",
        },
        'find_all_by_login': {
            'method': "get",
            'path': "/all/user/:login",
        },
        'upload_grades': {
            'method': "post",
            'path': "/:id/notes",
        },
    }