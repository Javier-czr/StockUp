"""
Este módulo contiene la configuración de desarrollo para la aplicación.
"""
import os


class DevelopmentConfig:
    """Configuración de desarrollo para la aplicación."""
    DEBUG = True
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "stock")
    MYSQL_DB = os.getenv("MYSQL_DB", "stockup")


config = {"development": DevelopmentConfig}
