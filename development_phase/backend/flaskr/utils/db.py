from pickle import NONE
import ibm_db
from dotenv import load_dotenv
from ..config.db_config import get_db_credential

load_dotenv()



def run_sql(query, params = None):
    conn = ibm_db.connect(get_db_credential(), "", "")
    statement = ibm_db.prepare(conn, query)
    print('hi')
    if(params == None):
        print('in')
        ibm_db.execute(statement)
        data = ibm_db.fetch_assoc(statement)
        print(data)
    ibm_db.execute(statement, params)
    data = ibm_db.fetch_assoc(statement)
    print(data)