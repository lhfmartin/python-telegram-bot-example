if __name__ == "__main__":
    import logging
    import sys

    LOG_FORMAT = "%(asctime)s %(filename)s [%(levelname)s] %(message)s"
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logging.basicConfig(
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=[handler],
    )

    from application import application

    application.run_polling()
