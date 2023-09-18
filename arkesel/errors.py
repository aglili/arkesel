class ArkeselErr(Exception):
    """
    API Key Cannot Be Found
    """


class MissingAPIKey(ArkeselErr):
    """
    API Key Not Found
    """