class AppErrors(object):
    NO_ERRORS = 0
    UNKNOWN_ERROR = 1
    POST_DOES_NOT_EXIST = 2
    COMMENT_DOES_NOT_EXIST = 3
    # This is a pretty fatal error, tbh...
    USER_DOES_NOT_EXIST = 4
    # Unable to insert into the datastore...this is bad.
    UNABLE_TO_PERSIST = 5
    UNABLE_TO_RETRIEVE = 6
    ID_ALREADY_EXISTS = 7
    # Used for when information that a function needs is missing.
    MISSING_INFORMATION = 8
