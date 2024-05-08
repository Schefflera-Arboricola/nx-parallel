"""Provides functions for computing the efficiency of nodes and graphs."""
import networkx as nx
from joblib import Parallel, delayed
import nx_parallel as nxp

__all__ = ["local_efficiency"]


def local_efficiency(G, get_chunks="chunks"):
    """The parallel computation is implemented by dividing the
    nodes into chunks and then computing and adding global efficiencies of all node
    in all chunks, in parallel, and then adding all these sums and dividing by the
    total number of nodes at the end.

    Parameters
    ----------
    get_chunks : str, function (default = "chunks")
        A function that takes in a list of all the nodes as input and returns an
        iterable `node_chunks`. The default chunking is done by slicing the `nodes`
        into `n` chunks, where `n` is the total number of CPU cores available.

    networkx.local_efficiency : https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.efficiency_measures.local_efficiency.html#local-efficiency
    """

    def _local_efficiency_node_subset(G, chunk):
        return sum(nx.global_efficiency(G.subgraph(G[v])) for v in chunk)

    if hasattr(G, "graph_object"):
        G = G.graph_object

    total_cores = nxp.cpu_count()

    if get_chunks == "chunks":
        num_in_chunk = max(len(G.nodes) // total_cores, 1)
        node_chunks = list(nxp.chunks(G.nodes, num_in_chunk))
    else:
        node_chunks = get_chunks(G.nodes)

    efficiencies = Parallel(n_jobs=total_cores)(
        delayed(_local_efficiency_node_subset)(G, chunk) for chunk in node_chunks
    )
    return sum(efficiencies) / len(G)
