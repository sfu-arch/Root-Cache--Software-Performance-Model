METAL Plots list:

Architectural Model

1. Address Based Cache Trace Plots
    1. Pie Chart moving - level wise cache occupancy along a given timeline
    2. Stacked bar graph - Intensity of eviction the (eviction rate) for gived levels along a timeline.
    3. Bar Graphs - Non primitive METAL levels saved due to shortcircuiting. Argument for domain specific tags. vs Generic Addresses.

2. Gem5-S : 
    1. Index Cache vs Address Based Cache for sequential search  latency. Latency vs Cache Size.


3. Primitive Plots (Reactive) : 
    
        Level Gather: Level Conctraint auxilary to the search
        cache_insert_level_with_search(start_level, end_level, key):
            if(key > node_val[i] && key < node_val[i+1]):
                if(level > start_level && level < end_level):
                    cache_insert()
        Key Gather: Key Constraint auxilary to search
        cache_insert_key_with_search(key_con, key):
            if(key > node_val[i] && key < node_val[i+1]):
                if(key_con in node):
                    cache_insert()
                    
    1. Gather (Level Vs Basic) : tuned parameters vs fixed basic model occupancy per level (ordered search key set)
    2. Gather (Level Vs Basic) : tuned parameyers vs fixed basic model performance plot (ordered search key set)
    4. Gather (Level Vs Key) : Tuned Parameters Gather Vs Moving Key Gather Vs basic performance plot (in levels traversed)
    5. Gather (Level Vs Key) : Occupancy per level (FSME: Full Search Motion Estimation; y^2 = 4ax)

Proactive:

    Partial Filter: Level Constraint with node index constraint.
    
    cache_insert_level(start_level, end_level):
        cache_insert_node(start_index, end_index):
            Partial_Traversal_BTree()
            cache_insert()


