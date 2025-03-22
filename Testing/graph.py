from graphviz import Digraph

def create_system_architecture():
    dot = Digraph(format='png')
    
    # Nodes
    dot.node('A', 'Data Acquisition')
    dot.node('B', 'Data Preprocessing')
    dot.node('C', 'Machine Learning Models')
    dot.node('D', 'Model Training & Validation')
    dot.node('E', 'Prediction & Analysis')
    dot.node('F', 'Deployment & Integration')
    dot.node('G', 'User Interface')
    
    # Sub-nodes
    dot.node('A1', 'Genomic Datasets')
    dot.node('A2', 'Patient Records')
    dot.node('A3', 'Public Databases')
    dot.edge('A', 'A1')
    dot.edge('A', 'A2')
    dot.edge('A', 'A3')
    
    dot.node('C1', 'KNN')
    dot.node('C2', 'Naive Bayes')
    dot.node('C3', 'Decision Tree')
    dot.edge('C', 'C1')
    dot.edge('C', 'C2')
    dot.edge('C', 'C3')
    
    # Connections
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    
    return dot

# Generate and render the diagram
architecture_diagram = create_system_architecture()
architecture_diagram.render('ml_system_architecture')
