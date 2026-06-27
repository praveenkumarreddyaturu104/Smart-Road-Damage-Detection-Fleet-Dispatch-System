"""
Vehicle page for Fleet Dispatch & Vehicle Allocation.
"""
import sys
import os
import streamlit as st

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages
from scheduler.damage_priority import get_priority
from scheduler.priority_queue_manager import PriorityQueueManager
from multi_vehicle_scheduler.vehicle import Vehicle
from gps.nearest_damage import get_nearest_damage
from algorithms.dijkstra import calculate_multi_stop_route, ROAD_NETWORK

def show_vehicle_page():
    st.title("🚚 Fleet Dispatch & Vehicle Allocation")
    st.write("Manage repair fleet and auto-dispatch vehicles to high-priority road damages.")

    # Initialize session state for vehicles
    if "vehicles" not in st.session_state:
        st.session_state["vehicles"] = [
            Vehicle("Dispatch Truck A", "Repair Center"),
            Vehicle("Dispatch Truck B", "Sector Beta")
        ]
    
    if "assignments" not in st.session_state:
        st.session_state["assignments"] = []

    # UI: Fleet Management
    st.subheader("Fleet Registration")
    with st.form("add_vehicle_form"):
        col1, col2 = st.columns(2)
        with col1:
            v_name = st.text_input("Vehicle Name/ID (e.g., Truck C)")
        with col2:
            v_loc = st.selectbox("Current Location", list(ROAD_NETWORK.keys()))
        
        submitted = st.form_submit_button("Add Vehicle")
        if submitted and v_name:
            st.session_state["vehicles"].append(Vehicle(v_name, v_loc))
            st.success(f"Added {v_name} at {v_loc}")

    # Display Current Fleet
    st.write("### Current Fleet Status")
    cols = st.columns(3)
    for i, v in enumerate(st.session_state["vehicles"]):
        with cols[i % 3]:
            st.info(f"**{v.vehicle_id}**\n\n📍 {v.current_location}\n\nStatus: {'🟢 Available' if v.available else '🔴 Busy'}")

    # Load Damages and Priorities
    damages = get_all_damages()
    if not damages:
        st.info("No pending damages to dispatch.")
        return

    # Assign sectors to damages (mock logic as in routing_page)
    sectors_list = ["Sector Alpha", "Sector Beta", "Sector Gamma", "Sector Delta", "Sector Epsilon"]
    for rec in damages:
        rec["sector"] = sectors_list[rec["id"] % len(sectors_list)]

    pq = PriorityQueueManager()
    for rec in damages:
        # Avoid putting dict directly because PriorityQueueManager might have issues with dict comparison if priorities tie
        # But wait, python heapq compares tuples. If priorities match, it compares rec dict, which throws TypeError.
        pass

    # Actually, let's fix the pq adding to prevent TypeError on tie
    import heapq
    heap = []
    # Using enumerate to avoid tie breaking on dicts
    for i, rec in enumerate(damages):
        priority = get_priority(rec["severity"])
        heapq.heappush(heap, (-priority, i, rec))

    # UI: Prioritized Queue
    st.subheader("Prioritized Repair Queue")
    queue_display = []
    temp_heap = heap.copy()
    while temp_heap:
        p, _, rec = heapq.heappop(temp_heap)
        queue_display.append({"ID": rec["id"], "Type": rec["damage_type"], "Severity": rec["severity"], "Priority Score": -p, "Location": rec["sector"]})
    
    st.dataframe(queue_display, use_container_width=True)

    # Auto-Dispatch Logic
    st.subheader("Auto-Dispatch System")
    if st.button("🚀 Run Auto-Dispatch", type="primary"):
        available_vehicles = [v for v in st.session_state["vehicles"] if v.available]
        
        if not available_vehicles:
            st.warning("No available vehicles to dispatch!")
            return
            
        assignments = []
        
        # Extract top N damages
        top_damages = []
        # Copy heap again to pop real tasks
        work_heap = heap.copy()
        for _ in range(min(len(available_vehicles), len(damages))):
            if work_heap:
                p, _, rec = heapq.heappop(work_heap)
                top_damages.append(rec)
        
        # For each vehicle, find the nearest damage from top_damages
        for v in available_vehicles:
            if not top_damages:
                break
                
            sector_coords = {
                "Repair Center": (17.3850, 78.4867),
                "Sector Alpha": (17.400, 78.490),
                "Sector Beta": (17.450, 78.520),
                "Sector Gamma": (17.350, 78.450),
                "Sector Delta": (17.420, 78.470),
                "Sector Epsilon": (17.390, 78.500)
            }
            v_lat, v_lon = sector_coords.get(v.current_location, (17.3850, 78.4867))
            
            nearest = get_nearest_damage(v_lat, v_lon, top_damages)
            if nearest:
                top_damages.remove(nearest)
                v.available = False
                
                # Dijkstra from vehicle location -> damage sector -> Repair Center
                route, dist = calculate_multi_stop_route(
                    ROAD_NETWORK, 
                    v.current_location, 
                    [nearest["sector"]]
                )
                
                # calculate_multi_stop_route returns back to starting node. 
                # e.g., v.current_location -> nearest["sector"] -> v.current_location.
                # If we want it to end at Repair Center, we do that manually.
                # Since calculate_multi_stop_route already goes back to start_node,
                # let's just use dijkstra_path
                from algorithms.dijkstra import dijkstra_path
                
                path1, dist1 = dijkstra_path(ROAD_NETWORK, v.current_location, nearest["sector"])
                path2, dist2 = dijkstra_path(ROAD_NETWORK, nearest["sector"], "Repair Center")
                
                if path1 and path2:
                    final_route = path1 + path2[1:]
                    final_dist = dist1 + dist2
                else:
                    final_route = []
                    final_dist = 0
                
                assignments.append({
                    "Vehicle": v.vehicle_id,
                    "Damage ID": nearest["id"],
                    "Damage Type": nearest["damage_type"],
                    "Sector": nearest["sector"],
                    "Route": " ➔ ".join(final_route) if final_route else "No route",
                    "Total Distance (km)": final_dist
                })
        
        st.session_state["assignments"] = assignments
        st.success("Dispatch complete!")
        st.rerun()

    # Display Active Assignments
    if st.session_state["assignments"]:
        st.subheader("Active Dispatch Assignments")
        for asg in st.session_state["assignments"]:
            st.info(
                f"**{asg['Vehicle']}** assigned to **Damage #{asg['Damage ID']}** ({asg['Damage Type']} in {asg['Sector']})\n\n"
                f"**Route:** {asg['Route']}\n\n"
                f"**Distance:** {asg['Total Distance (km)']} km"
            )
            
        if st.button("Reset Fleet (Mark all available)"):
            for v in st.session_state["vehicles"]:
                v.available = True
            st.session_state["assignments"] = []
            st.rerun()