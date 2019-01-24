# -* encoding: utf-8 *-
import logging

from django.db.backends.base import base as django_db_base

try:
    import pymysql
except ImportError:
    pymysql = None

log = logging.getLogger('django-db-reconnect')


def monkey_patch() -> None:
    _old_ensure_connection = django_db_base.BaseDatabaseWrapper.ensure_connection

    def ensure_connection_with_retries(self: django_db_base.BaseDatabaseWrapper) -> None:
        if self.connection:
            if self.autocommit:
                if pymysql and isinstance(self.connection, pymysql.connections.Connection):
                    self.connection.ping(reconnect=True)

        _old_ensure_connection(self)

    log.debug('monkey path django.db.backends.base.BaseDatabaseWrapper.ensure_connection')
    django_db_base.BaseDatabaseWrapper.ensure_connection = ensure_connection_with_retries


monkey_patch()
