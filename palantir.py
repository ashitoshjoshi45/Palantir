# Added on 27-10-2026
# Palantir Threat Ontology & Autonomous AI SOC Platform

import sqlite3

def initialize_palantir_ontology(db_name="palantir_ontology.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Ontology Objects: Threat Actors, Cloud Workloads, IAM Roles, Data Vaults
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ontology_objects (
            object_id TEXT PRIMARY KEY,
            object_name TEXT NOT NULL,
            object_type TEXT NOT NULL,
            risk_score INTEGER DEFAULT 0,
            status TEXT DEFAULT 'ACTIVE'
        )
    ''')

    conn.commit()
    conn.close()
    print(f'[+] Palantir Ontology core initialized in {db_name}')

if __name__ == '__main__':
    initialize_palantir_ontology()
