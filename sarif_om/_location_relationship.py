# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class LocationRelationship(object):
    """Information about the relation of one location to another."""
    target = attr.ib()
    description = attr.ib(default=None)
    kinds = attr.ib(default=['relevant'])
    properties = attr.ib(default=None)