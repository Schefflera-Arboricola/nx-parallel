from functools import partial
import nx_parallel as nxp
from joblib import Parallel, delayed
import networkx as nx

__all__ = ["closeness_vitality"]


def closeness_vitality(
    G, node=None, weight=None, wiener_index=None, get_chunks="chunks"
):
    """The parallel computation is implemented only when the node
    is not specified. The closeness vitality for each node is computed concurrently.

    Parameters
    ----------
    get_chunks : str, function (default = "chunks")
        A function that takes in a list of all the nodes as input and
        returns an iterable `node_chunks`. The default chunking is done by slicing the
        `nodes` into `n` chunks, where `n` is the total number of CPU cores.

    networkx.closeness_vitality : https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.vitality.closeness_vitality.html#closeness-vitality
    """

    def closeness_vitality_chunk_subset(chunk):
        return {v: vitality(v) for v in chunk}

    if hasattr(G, "graph_object"):
        G = G.graph_object

    if wiener_index is None:
        wiener_index = nx.wiener_index(G, weight=weight)

    if node is not None:
        after = nx.wiener_index(G.subgraph(set(G) - {node}), weight=weight)
        return wiener_index - after

    total_cores = nxp.cpu_count()

    if get_chunks == "chunks":
        num_in_chunk = max(len(G) // total_cores, 1)
        node_chunks = nxp.chunks(G.nodes, num_in_chunk)
    else:
        node_chunks = get_chunks(G.nodes)

    vitality = partial(
        nx.closeness_vitality, G, weight=weight, wiener_index=wiener_index
    )

    result = Parallel(n_jobs=total_cores)(
        delayed(closeness_vitality_chunk_subset)(chunk) for chunk in node_chunks
    )
    return {k: v for d in result for k, v in d.items()}
