import os
import ast


def get_info():
    """Return a dictionary with information about the package."""
    return {
        "backend_name": "parallel",
        "project": "nx-parallel",
        "package": "nx_parallel",
        "url": "https://github.com/networkx/nx-parallel",
        "short_summary": "Parallel backend for NetworkX algorithms",
        "functions": {
            "number_of_isolates": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/isolate.py#L8",
                "additional_docs": "The parallel computation is implemented by dividing the list of isolated nodes into chunks and then finding the length of each chunk in parallel and then adding all the lengths at the end.",
                "additional_parameters": None,
            },
            "square_clustering": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/cluster.py#L10",
                "additional_docs": "The nodes are chunked into `node_chunks` and then the square clusterin coefficient for all `node_chunks` are computed in parallel over all available\nCPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes (or nbunch) as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "local_efficiency": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/efficiency_measures.py#L9",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and then computing and adding global efficiencies of all node in all chunks, in parallel, and then adding all these sums and dividing by the total number of nodes at the end.",
                "additional_parameters": None,
            },
            "closeness_vitality": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/vitality.py#L9",
                "additional_docs": "The parallel computation is implemented only when the node is not specified. The closeness vitality for each node is computed concurrently.",
                "additional_parameters": None,
            },
            "is_reachable": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/tournament.py#L10",
                "additional_docs": "The function parallelizes the calculation of two neighborhoods of vertices in `G` and checks closure conditions for each neighborhood subset in parallel.",
                "additional_parameters": None,
            },
            "tournament_is_strongly_connected": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/tournament.py#L54",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and then checking whether each node is reachable from each other node in parallel.",
                "additional_parameters": None,
            },
            "betweenness_centrality": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/centrality/betweenness.py#L16",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and computing betweenness centrality for each chunk concurrently.",
                "additional_parameters": None,
            },
            "node_redundancy": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/bipartite/redundancy.py#L11",
                "additional_docs": "In the parallel implementation we divide the nodes into chunks and compute the node redundancy coefficients for all `node_chunk` in parallel.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` (or `nodes`) into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_bellman_ford_path": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L16",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths for each node_chunk, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "johnson": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L59",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and computing the shortest paths using Johnson's Algorithm for each chunk in parallel.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            'chunks': {'url': 'https://github.com/networkx/nx-parallel/blob/main/nx_parallel/utils/chunk.py#L7', 'additional_docs': 'Divides an iterable into chunks of size n', 'additional_parameters': None}, 
            
            'cpu_count': {'url': 'https://github.com/networkx/nx-parallel/blob/main/nx_parallel/utils/chunk.py#L17', 'additional_docs': 'Returns the number of logical CPUs or cores', 'additional_parameters': None}
        },
    }


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
                        "additional_docs": par_docs,
                        "additional_parameters": par_params,
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
