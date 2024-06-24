# This file was automatically generated by update_get_info.py


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
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the isolated nodes as input and returns an iterable `isolate_chunks`. The default chunking is done by slicing the `isolates` into `n` chunks, where `n` is the total number of CPU cores available."
                },
            },
            "square_clustering": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/cluster.py#L10",
                "additional_docs": "The nodes are chunked into `node_chunks` and then the square clustering coefficient for all `node_chunks` are computed in parallel over all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes (or nbunch) as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "local_efficiency": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/efficiency_measures.py#L9",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and then computing and adding global efficiencies of all node in all chunks, in parallel, and then adding all these sums and dividing by the total number of nodes at the end.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the total number of CPU cores available."
                },
            },
            "closeness_vitality": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/vitality.py#L9",
                "additional_docs": "The parallel computation is implemented only when the node is not specified. The closeness vitality for each node is computed concurrently.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the total number of CPU cores."
                },
            },
            "is_reachable": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/tournament.py#L12",
                "additional_docs": "The function parallelizes the calculation of two neighborhoods of vertices in `G` and checks closure conditions for each neighborhood subset in parallel.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the total number of CPU cores available."
                },
            },
            "tournament_is_strongly_connected": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/tournament.py#L59",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and then checking whether each node is reachable from each other node in parallel.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the total number of CPU cores available."
                },
            },
            "all_pairs_node_connectivity": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/connectivity/connectivity.py#L17",
                "additional_docs": "The parallel implementation first divides a list of all permutation (in case of directed graphs) and combinations (in case of undirected graphs) of `nbunch` into chunks and then creates a generator to lazily compute the local node connectivities for each chunk, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores. At the end, the results are aggregated into a single dictionary and returned.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in `list(iter_func(nbunch, 2))` as input and returns an iterable `pairs_chunks`, here `iter_func` is `permutations` in case of directed graphs and `combinations` in case of undirected graphs. The default is to create chunks by slicing the list into `n` chunks, where `n` is the number of CPU cores, such that size of each chunk is atmost 10, and at least 1."
                },
            },
            "approximate_all_pairs_node_connectivity": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/approximation/connectivity.py#L12",
                "additional_docs": "The parallel implementation first divides the a list of all permutation (in case of directed graphs) and combinations (in case of undirected graphs) of `nbunch` into chunks and then creates a generator to lazily compute the local node connectivities for each chunk, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores. At the end, the results are aggregated into a single dictionary and returned.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in `list(iter_func(nbunch, 2))` as input and returns an iterable `pairs_chunks`, here `iter_func` is `permutations` in case of directed graphs and `combinations` in case of undirected graphs. The default is to create chunks by slicing the list into `n` chunks, where `n` is the number of CPU cores, such that size of each chunk is atmost 10, and at least 1."
                },
            },
            "betweenness_centrality": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/centrality/betweenness.py#L19",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and computing betweenness centrality for each chunk concurrently.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "edge_betweenness_centrality": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/centrality/betweenness.py#L94",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and computing edge betweenness centrality for each chunk concurrently.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in a list of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "node_redundancy": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/bipartite/redundancy.py#L11",
                "additional_docs": "In the parallel implementation we divide the nodes into chunks and compute the node redundancy coefficients for all `node_chunk` in parallel.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` (or `nodes`) into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_dijkstra": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L28",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths and lengths for each `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_dijkstra_path_length": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L71",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths lengths for each node in `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_dijkstra_path": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L121",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths for each `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_bellman_ford_path_length": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L164",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths lengths for each node in `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_bellman_ford_path": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L209",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths for each node_chunk, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "johnson": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/weighted.py#L252",
                "additional_docs": "The parallel computation is implemented by dividing the nodes into chunks and computing the shortest paths using Johnson's Algorithm for each chunk in parallel.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_all_shortest_paths": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/generic.py#L10",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute all shortest paths between all nodes for each node in `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_shortest_path_length": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/unweighted.py#L18",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths lengths for each node in `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "all_pairs_shortest_path": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/algorithms/shortest_paths/unweighted.py#L63",
                "additional_docs": "The parallel implementation first divides the nodes into chunks and then creates a generator to lazily compute shortest paths for each `node_chunk`, and then employs joblib's `Parallel` function to execute these computations in parallel across all available CPU cores.",
                "additional_parameters": {
                    'get_chunks : str, function (default = "chunks")': "A function that takes in an iterable of all the nodes as input and returns an iterable `node_chunks`. The default chunking is done by slicing the `G.nodes` into `n` chunks, where `n` is the number of CPU cores."
                },
            },
            "chunks": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/utils/chunk.py#L8",
                "additional_docs": "Divides an iterable into chunks of size n",
                "additional_parameters": None,
            },
            "cpu_count": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/utils/chunk.py#L18",
                "additional_docs": "Returns the number of logical CPUs or cores",
                "additional_parameters": None,
            },
            "create_iterables": {
                "url": "https://github.com/networkx/nx-parallel/blob/main/nx_parallel/utils/chunk.py#L26",
                "additional_docs": "Creates an iterable of function inputs for parallel computation based on the provided iterator type.",
                "additional_parameters": {
                    "G : NetworkX graph": "iterator : str Type of iterator. Valid values are 'node', 'edge', 'isolate'",
                    "iterable : Iterable": "An iterable of function inputs.",
                },
            },
        },
    }
