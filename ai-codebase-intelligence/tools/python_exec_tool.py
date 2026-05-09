from langchain.tools import BaseTool

import subprocess
import tempfile


class PythonExecTool(BaseTool):
    name = "Python Execution Tool"
    description = "Executes Python code"

    def _run(self, code: str):

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False
        ) as file:

            file.write(code)
            file_path = file.name

        try:
            result = subprocess.check_output(
                ["python", file_path],
                stderr=subprocess.STDOUT,
                text=True,
            )

            return result

        except subprocess.CalledProcessError as error:
            return error.output