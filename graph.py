import networkx as nx  # Import library NetworkX untuk manipulasi graf
import matplotlib.pyplot as plt  # Import library Matplotlib untuk visualisasi

class Graf:
    def __init__(self):
        """
        Inisialisasi objek Graf dengan graf kosong.
        """
        self.graph = nx.Graph()  # Membuat objek graf kosong menggunakan NetworkX

    def add_node(self, node):
        """
        Menambahkan node ke graf.

        Args:
            node: Node yang ingin ditambahkan.
        """
        self.graph.add_node(node)  # Menambahkan node ke graf

    def add_edge(self, u, v, weight=None):
        """
        Menambahkan sisi antara node u dan v, dengan bobot opsional.

        Args:
            u: Node pertama.
            v: Node kedua.
            weight: Bobot sisi (opsional).
        """
        if weight is None:
            self.graph.add_edge(u, v)  # Menambahkan sisi tanpa bobot
        else:
            self.graph.add_edge(u, v, weight=weight)  # Menambahkan sisi dengan bobot

    def visualize_graph(self):
        """
        Menampilkan visualisasi graf.
        """
        pos = nx.spring_layout(self.graph)  # Menentukan posisi node menggunakan layout spring
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')  # Menggambar graf
        labels = nx.get_edge_attributes(self.graph, 'weight')  # Mengambil atribut bobot dari sisi
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)  # Menambahkan label bobot pada sisi
        plt.title("Visualisasi Graf")  # Menambahkan judul pada plot
        plt.show()  # Menampilkan plot

    def shortest_path(self, start_node, end_node):
        """
        Menghitung jalur terpendek antara dua node menggunakan algoritma Dijkstra.

        Args:
            start_node: Node awal.
            end_node: Node tujuan.

        Returns:
            List yang berisi urutan node pada jalur terpendek, atau pesan error jika jalur tidak ditemukan.
        """
        try:
            # Menghitung jalur terpendek dengan bobot sebagai parameter menggunakan algoritma Dijkstra
            path = nx.shortest_path(self.graph, source=start_node, target=end_node, weight='weight')
            return path  # Mengembalikan jalur terpendek
        except nx.NetworkXNoPath:
            return f"Tidak ada jalur antara node {start_node} dan {end_node}"  # Mengembalikan pesan error jika tidak ada jalur
        except nx.NodeNotFound as e:
            return f"Node tidak ditemukan dalam graf: {e}"  # Mengembalikan pesan error jika node tidak ditemukan

    def visual_shortest_path(self, start_node, end_node):
        """
        Menampilkan visualisasi graf dengan jalur terpendek yang disorot.

        Args:
            start_node: Node awal.
            end_node: Node tujuan.
        """
        try:
            # Menghitung jalur terpendek dengan bobot sebagai parameter menggunakan algoritma Dijkstra
            path = nx.shortest_path(self.graph, source=start_node, target=end_node, weight='weight')
            pos = nx.spring_layout(self.graph)  # Menentukan posisi node menggunakan layout spring
            nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')  # Menggambar graf
            labels = nx.get_edge_attributes(self.graph, 'weight')  # Mengambil atribut bobot dari sisi
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)  # Menambahkan label bobot pada sisi

            # Menyorot node dan sisi pada jalur terpendek
            path_edges = list(zip(path, path[1:]))  # Membuat list pasangan node yang membentuk sisi pada jalur terpendek
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='red')  # Mewarnai node pada jalur terpendek dengan warna merah
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=3)  # Mewarnai sisi pada jalur terpendek dengan warna merah dan tebal

            plt.title(f"Jalur Terpendek dari {start_node} ke {end_node}")  # Menambahkan judul pada plot
            plt.show()  # Menampilkan plot
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur antara node {start_node} dan {end_node}")  # Menampilkan pesan error jika tidak ada jalur
        except nx.NodeNotFound as e:
            print(f"Node tidak ditemukan dalam graf: {e}")  # Menampilkan pesan error jika node tidak ditemukan

# Implementasi
# Membuat Object
graph = Graf()  # Membuat objek Graf

# Menambah Node (titik)
graph.add_node(1)  # Menambahkan node 1
graph.add_node(2)  # Menambahkan node 2
graph.add_node(3)  # Menambahkan node 3
graph.add_node(4)  # Menambahkan node 4
graph.add_node(5)  # Menambahkan node 5

# Menambah sisi (Edge)
graph.add_edge(1, 2, weight=4.5)  # Menambahkan sisi antara node 1 dan 2 dengan bobot 4.5
graph.add_edge(1, 3, weight=3.2)  # Menambahkan sisi antara node 1 dan 3 dengan bobot 3.2
graph.add_edge(2, 4, weight=2.7)  # Menambahkan sisi antara node 2 dan 4 dengan bobot 2.7
graph.add_edge(3, 4, weight=1.8)  # Menambahkan sisi antara node 3 dan 4 dengan bobot 1.8
graph.add_edge(1, 4, weight=6.7)  # Menambahkan sisi antara node 1 dan 4 dengan bobot 6.7
graph.add_edge(3, 5, weight=2.7)  # Menambahkan sisi antara node 3 dan 5 dengan bobot 2.7

# Visualisasi Graf
graph.visualize_graph()  # Menampilkan visualisasi graf

# Jalur terpendek
print(graph.shortest_path(1, 5))  # Mencetak jalur terpendek dari node 1 ke node 5

# Visualisasi Jalur terpendek
graph.visual_shortest_path(1, 5)  # Menampilkan visualisasi graf dengan jalur terpendek dari node 1 ke node 5 yang disorot