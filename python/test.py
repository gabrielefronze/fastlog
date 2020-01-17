#! /usr/bin/env python3

from fastlog import *

if __name__ == "__main__":
    print('\nLog level set to DEBUG')
    set_log_level(DEBUG)

    fastlog(UI, "This is a debug message with UI log level")
    fastlog(DEBUG, "This is a debug message with DEBUG log level")
    fastlog(INFO, "This is an info message with INFO log level")
    fastlog(WARNING, "This is an error message with WARNING log level")
    fastlog(ERROR, "This is an error message with ERROR log level")

    print('\nLog level set to INFO')
    set_log_level(INFO)

    fastlog(UI, "This is a debug message with UI log level")
    fastlog(DEBUG, "This is a debug message with DEBUG log level")
    fastlog(INFO, "This is an info message with INFO log level")
    fastlog(WARNING, "This is an error message with WARNING log level")
    fastlog(ERROR, "This is an error message with ERROR log level")

    print('\nLog level set to ERROR')
    set_log_level(ERROR)

    fastlog(UI, "This is a debug message with UI log level")
    fastlog(DEBUG, "This is a debug message with DEBUG log level")
    fastlog(INFO, "This is an info message with INFO log level")
    fastlog(WARNING, "This is an error message with WARNING log level")
    fastlog(ERROR, "This is an error message with ERROR log level")

    print('\nLog level set to SILENT')
    set_log_level(SILENT)

    fastlog(UI, "This is a debug message with UI log level")
    fastlog(DEBUG, "This is a debug message with DEBUG log level")
    fastlog(INFO, "This is an info message with INFO log level")
    fastlog(WARNING, "This is an error message with WARNING log level")
    fastlog(ERROR, "This is an error message with ERROR log level")