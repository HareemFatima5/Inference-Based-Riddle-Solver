# Function to apply resolution on two clauses
def resolve(c1, c2):
    """
    Resolves two clauses c1 and c2. If they can be resolved, returns the resolved clause.
    If no resolution is possible, returns None.
    """
    for literal in c1:
        if f"~{literal}" in c2:
            resolved_clause = (set(c1) | set(c2)) - {literal, f"~{literal}"}
            return resolved_clause
    return None

# Function to check if the clauses can lead to a contradiction (empty clause)
def resolution_algorithm(clauses):
    new_clauses = set(clauses)  # Start with the original clauses
    while True:
        pairs = list(new_clauses)  # Convert the set to a list to pair up clauses
        resolvents = set()  # To store newly resolved clauses
        
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                resolved = resolve(pairs[i], pairs[j])
                if resolved:
                    resolvents.add(frozenset(resolved))
        
        # If no new clauses are found, stop
        if not resolvents:
            return True, new_clauses  # No contradiction found, satisfiable
        
        # Add new clauses to the list of clauses
        new_clauses.update(resolvents)
        
        # Check for empty clause (contradiction)
        if frozenset() in new_clauses:
            return False, new_clauses  # Contradiction found, unsatisfiable
