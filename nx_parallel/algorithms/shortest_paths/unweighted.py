"""
Shortest path parallel algorithms for unweighted graphs.
"""

from joblib import Parallel, delayed
import nx_parallel as nxp
from networkx.algorithms.shortest_paths.unweighted import (
    single_source_shortest_path_length,
    single_source_shortest_path,
)

__all__ = [
    "all_pairs_shortest_path",
    "all_pairs_shortest_path_length",
]


def all_pairs_shortest_path_length(G, cutoff=None, get_chunks="chunks"):
    """The parallel computation is implemented by computing the
    shortest paths lengths for each node in `G` concurrently.

    networkx.single_source_shortest_path_length : https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.unweighted.all_pairs_shortest_path_length.html#all-pairs-shortest-path-length"""

    def _process_node_chunk(node_chunk):
        return [
            (node, single_source_shortest_path_length(G, node, cutoff=cutoff))
            for node in node_chunk
        ]

    if hasattr(G, "graph_object"):
        G = G.graph_object

    nodes = G.nodes
    total_cores = nxp.cpu_count()

    if get_chunks == "chunks":
        node_chunks = get_chunks(nodes)
    else:
        num_in_chunk = max(len(nodes) // total_cores, 1)
        node_chunks = nxp.chunks(nodes, num_in_chunk)

    path_lengths_chunk_generator = (
        delayed(_process_node_chunk)(node_chunk) for node_chunk in node_chunks
    )

    for path_length_chunk in Parallel(n_jobs=nxp.cpu_count())(
        path_lengths_chunk_generator
    ):
        for path_length in path_length_chunk:
            yield path_length


def all_pairs_shortest_path(G, cutoff=None, get_chunks="chunks"):
    """The parallel computation is implemented by computing the
    shortest paths for each node in `G` concurrently.

    networkx.single_source_shortest_path : https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.unweighted.all_pairs_shortest_path.html#all-pairs-shortest-path"""

    def _process_node_chunk(node_chunk):
        return [
            (node, single_source_shortest_path(G, node, cutoff=cutoff))
            for node in node_chunk
        ]

    if hasattr(G, "graph_object"):
        G = G.graph_object

    nodes = G.nodes
    total_cores = nxp.cpu_count()

    if get_chunks == "chunks":
        node_chunks = get_chunks(nodes)
    else:
        num_in_chunk = max(len(nodes) // total_cores, 1)
        node_chunks = nxp.chunks(nodes, num_in_chunk)

    paths_chunk_generator = (
        delayed(_process_node_chunk)(node_chunk) for node_chunk in node_chunks
    )

    for path_chunk in Parallel(n_jobs=nxp.cpu_count())(paths_chunk_generator):
        for path in path_chunk:
            yield path
