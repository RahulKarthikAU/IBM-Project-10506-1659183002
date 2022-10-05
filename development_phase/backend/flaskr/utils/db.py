from pickle import NONE
import ibm_db
from dotenv import load_dotenv
from ..config.db_config import get_db_credential

load_dotenv()



def run_sql_select(query, params = None):
    conn = ibm_db.connect(get_db_credential(), "", "")
    statement = ibm_db.prepare(conn, query)
    try:
        if(params == None):
            ibm_db.execute(statement)
            data = ibm_db.fetch_assoc(statement)
            return data
        ibm_db.execute(statement, params)
        data = ibm_db.fetch_assoc(statement)
        ibm_db.close(conn)
        return data

    except:
        return False

def run_sql_insert(query, params):
    conn = ibm_db.connect(get_db_credential(), "", "")
    statement = ibm_db.prepare(conn, query)
    try:
        ibm_db.execute(statement, params)
        ibm_db.close(conn)
        return True
        
    except:
        return False
