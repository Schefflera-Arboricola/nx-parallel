def get_info():
    """Return a dictionary with information about the package."""
    import os
    import ast

    def get_funcs_info():
        """Return a dictionary with information about all the functions."""
        funcs = {}

        nx_parallel_dir = os.path.join(os.getcwd(), "nx_parallel")
        for root, dirs, files in os.walk(nx_parallel_dir):
            for file in files:
                if (
                    file.endswith(".py")
                    and file != "__init__.py"
                    and not file.startswith("test_")
                ):
                    path = os.path.join(root, file)
                    d = extract_docstrings_from_file(path)
                    for func in d:
                        par_docs, par_params = extract_from_docs(d[func])
                        funcs[func] = {
                            "url": get_url(path, func),
                            "additional_docs": par_docs.replace("\n", " "),
                            "additional_parameters": par_params.replace("\n", " "),
                        }
        return funcs


    def extract_docstrings_from_file(file_path):
        """
        Extract docstrings from functions listed in the __all__ list of a Python file.

        Args:
        - file_path: The path to the Python file.

        Returns:
        - A dictionary mapping function names to their docstrings.
        """
        docstrings = {}
        with open(file_path, "r") as f:
            tree = ast.parse(f.read(), filename=file_path)
            all_list = None
            for node in tree.body:
                if isinstance(node, ast.Assign):
                    if (
                        isinstance(node.targets[0], ast.Name)
                        and node.targets[0].id == "__all__"
                    ):
                        all_list = [
                            expr.s for expr in node.value.elts if isinstance(expr, ast.Str)
                        ]
                elif isinstance(node, ast.FunctionDef):
                    if all_list and node.name in all_list:
                        docstring = ast.get_docstring(node) or "No docstring found."
                        docstrings[node.name] = docstring
        return docstrings


    def extract_from_docs(docstring):
        """Extract the parallel documentation and parallel parameter description from the given doctring."""
        try:
            # Extracting Parallel Computation description
            # Assuming that the first para in docstring is the function's PC desc
            # "par" is short for "parallel"
            par_docs_ = docstring.split("\n\n")[0]
            par_docs_ = par_docs_.split("\n")
            par_docs_ = [line.strip() for line in par_docs_ if line.strip()]
            par_docs = "\n".join(par_docs_)
        except IndexError:
            par_docs = None
        except Exception as e:
            print(e)
            par_docs = None

        try:
            # Extracting extra parameters
            # Assuming that the last para in docstring is the function's extra params
            par_params = {}
            par_params_ = docstring.split("------------\n")[1]

            par_params_ = par_params_.split("\n\n\n")
            for i in par_params_:
                j = i.split("\n")
                par_params[j[0]] = "\n".join(
                    [line.strip() for line in j[1:] if line.strip()]
                )
                if i == par_params_[-1]:
                    par_params[j[0]] = "\n".join(
                        [line.strip() for line in j[1:-1] if line.strip()]
                    )
        except IndexError:
            par_params = None
        except Exception as e:
            print(e)
            par_params = None
        return par_docs, par_params


    def get_url(file_path, function_name):
        """Return the URL to the given function in the given file."""
        file_url = (
            "https://github.com/networkx/nx-parallel/blob/main/nx_parallel"
            + file_path.split("nx_parallel")[-1]
            + "#L"
        )
        with open(file_path, "r") as f:
            tree = ast.parse(f.read(), filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    return file_url + str(node.lineno)
        return file_url

    return {
        "backend_name": "parallel",
        "project": "nx-parallel",
        "package": "nx_parallel",
        "url": "https://github.com/networkx/nx-parallel",
        "short_summary": "Parallel backend for NetworkX algorithms",
        "functions": get_funcs_info(),
    }
