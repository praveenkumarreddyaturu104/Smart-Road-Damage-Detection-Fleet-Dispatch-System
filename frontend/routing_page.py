"""
Routing page calculating and visualizing shortest repair paths.
"""
import sys
import os
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages
from algorithms.dijkstra import ROAD_NETWORK, calculate_multi_stop_route


def show_routing_page():
    """
    Render road network graph and run Dijkstra multi-stop routing on selected damages.
    """
    st.title("🛣️ Repair Dispatch & Routing")
    st.write("Optimize the dispatch route for the repair vehicle to visit and fix reported road damages.")

    # Retrieve logged damages
    damages = get_all_damages()

    if not damages:
        st.info("No road damage records logged yet. Go to the Upload page to scan road images.")
        return

    # Map damages to sectors based on ID
    sectors_list = ["Sector Alpha", "Sector Beta", "Sector Gamma", "Sector Delta", "Sector Epsilon"]
    for rec in damages:
        # Simple mapping rule: ID modulo number of sectors
        rec["sector"] = sectors_list[rec["id"] % len(sectors_list)]

    # Layout: columns for selections and graph rendering
    col_sel, col_graph = st.columns([1, 2])

    with col_sel:
        st.subheader("Route Configuration")
        start_node = st.selectbox(
            "Select Starting Hub (Depot):",
            options=["Repair Center"]
        )

        # Allow user to multi-select damages
        damage_options = {
            f"ID #{r['id']} - {r['damage_type']} ({r['sector']})": r["sector"]
            for r in damages
        }

        selected_options = st.multiselect(
            "Select damages to repair:",
            options=list(damage_options.keys())
        )

        # Extract unique sectors (stops) to visit
        stops = [damage_options[opt] for opt in selected_options]

        run_route = st.button("Optimize Route", type="primary")

    # Define layout coordinates for graph visualization
    node_positions = {
        "Repair Center": (0, 2),
        "Sector Alpha": (-2, 1),
        "Sector Beta": (-2, -1),
        "Sector Gamma": (2, 1),
        "Sector Delta": (0, 0),
        "Sector Epsilon": (2, -1)
    }

    # Build NetworkX graph
    G = nx.Graph()
    for u, neighbors in ROAD_NETWORK.items():
        for v, w in neighbors:
            G.add_edge(u, v, weight=w)

    route = []
    total_dist = 0.0

    if run_route and selected_options:
        # Calculate optimal path
        route, total_dist = calculate_multi_stop_route(ROAD_NETWORK, start_node, stops)
        
        with col_sel:
            st.success("Routing Optimized!")
            st.markdown(f"**Total Route Distance:** `{total_dist} km`")
            st.markdown("**Dispatch Sequence:**")
            path_display = " ➔ ".join([f"`{node}`" for node in route])
            st.write(path_display)
            
            # Step by step details
            st.markdown("**Transit Details:**")
            for i in range(len(route) - 1):
                u, v = route[i], route[i+1]
                # Find weight
                weight = 0
                for neighbor, w in ROAD_NETWORK[u]:
                    if neighbor == v:
                        weight = w
                        break
                st.write(f"• `{u}` to `{v}`: `{weight} km`")

    with col_graph:
        st.subheader("Road Network Visualization")
        
        # Plotting network
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Color nodes
        node_colors = []
        for node in G.nodes():
            if node == start_node:
                node_colors.append("#d9534f")  # Red for Repair Center
            elif node in stops:
                node_colors.append("#f0ad4e")  # Orange for Target Sectors
            else:
                node_colors.append("#0288d1")  # Blue for other nodes

        # Draw nodes & labels
        nx.draw_networkx_nodes(G, node_positions, node_color=node_colors, node_size=1600, ax=ax)
        nx.draw_networkx_labels(G, node_positions, font_color="white", font_weight="bold", font_size=9, ax=ax)

        # Color edges depending on whether they are in the active route
        edge_colors = []
        edge_widths = []
        
        # Set of edges in the path
        path_edges_set = set()
        if route:
            for i in range(len(route) - 1):
                path_edges_set.add((route[i], route[i+1]))
                path_edges_set.add((route[i+1], route[i]))

        for u, v in G.edges():
            if (u, v) in path_edges_set or (v, u) in path_edges_set:
                edge_colors.append("#d9534f")  # Red for route
                edge_widths.append(4.0)
            else:
                edge_colors.append("#cccccc")  # Light grey for normal network
                edge_widths.append(1.5)

        nx.draw_networkx_edges(G, node_positions, edge_color=edge_colors, width=edge_widths, ax=ax)

        # Edge labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        formatted_labels = {k: f"{v} km" for k, v in edge_labels.items()}
        nx.draw_networkx_edge_labels(G, node_positions, edge_labels=formatted_labels, font_size=8, ax=ax)

        # Style graph background
        ax.set_facecolor("none")
        plt.axis("off")
        
        # Display plot in streamlit
        st.pyplot(fig)
        plt.close(fig)
