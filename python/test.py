#! /usr/bin/env python3

from fastlog import *

if __name__ == "__main__":
    print('\nLog level set to DEBUG')
    set_log_level(DEBUG)

    fastlog(DEBUG, "This is a debug message with DEBUG log level")
    fastlog(INFO, "This is an info message with DEBUG log level")
    fastlog(ERROR, "This is an error message with DEBUG log level")

    print('\nLog level set to INFO')
    set_log_level(INFO)

    fastlog(DEBUG, "This is a debug message with INFO log level")
    fastlog(INFO, "This is an info message with INFO log level")
    fastlog(ERROR, "This is an error message with INFO log level")

    print('\nLog level set to ERROR')
    set_log_level(ERROR)

    fastlog(DEBUG, "This is a debug message with ERROR log level")
    fastlog(INFO, "This is an info message with ERROR log level")
    fastlog(ERROR, "This is an error message with ERROR log level")