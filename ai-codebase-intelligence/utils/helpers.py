import textwrap


class Helpers:
    @staticmethod
    def chunk_text(text, chunk_size=500):
        return textwrap.wrap(text, chunk_size)