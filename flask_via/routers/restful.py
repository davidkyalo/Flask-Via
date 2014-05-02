# -*- coding: utf-8 -*-

"""
flask_via.routers.restful
=========================

Routers for the Flask-Restful framework.
"""

from flask_via.routers import BaseRouter


class Resource(BaseRouter):
    """ The Resource router allows you to define Flask-Restful routes and have
    those API resources added to the application automatically. For this to
    work you must at ``init_app`` time pass a optional keyword argument
    ``restful_api`` to ``init_app`` with its value being the restful api
    extension instance.

    Example
    -------
    .. sourcecode:: python

        app = Flask(__name__)
        api = restful.Api(app)

        class FooResource(restful.Resource):

            def get(self):
                return {'hello': 'world'}

        routes = [
            Resource('/foo', FooResource)
        ]

        via = Via()
        via.init_app(
            app,
            routes_module='flask_via.examples.restful',
            restful_api=api)

        if __name__ == '__main__':
            app.run(debug=True)

    """

    def __init__(self, url, resource):
        """ Constructor for flask restful resource router.

        Arguments
        ---------
        url : str
            The url to use for the route
        resource
            A flask ``restful.Resource`` resource class
        """

        self.url = url
        self.resource = resource

    def add_to_app(self, app, restful_api=None):
        """ Adds the restul api resource route to the application.

        Arguments
        ---------
        app : flask.app.Flask
            Flask application instance

        Keyword Arguments
        -----------------
        restful_api : str
            Instantiated restful API instace, used to add the route.

        Raises
        ------
        NotImplementedError
            If ``restful_api`` is not provided
        """

        if not restful_api:
            raise NotImplementedError('restful_api not passed to add_to_app')

        restful_api.add_resource(self.resource, self.url)
