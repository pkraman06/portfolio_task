import os


class FileLoader:
    @staticmethod
    def load_files(directory, extensions=None):
        extensions = extensions or [".py"]

        files = []

        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if any(filename.endswith(ext) for ext in extensions):
                    files.append(os.path.join(root, filename))

        return files