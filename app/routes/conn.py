from mysql import connector


DB_CONFIG = {
      'host': 'localhost',
      'database': 'chatbot',
      'user': 'root',
      'password': ''
}

class connection:

      def __init__(self):
            self.conn = None   
            self.cursor = None
            
      def openConn(self):
            try:
                  self.conn = connector.connect(**DB_CONFIG)
                  self.cursor = self.conn.cursor()
                  print('connessione riuscita')
            except mysql.connect.Error as e:
                  print(f'connessione fallita {e}')
                  raise

      def sqlQuery(self, query, params=None):
            if not self.conn or not self.cursor:
                  raise Exception('connessione non attiva')
            try:
                  self.cursor.execute(query, params)

                  # Esegui il commit solo per query che modificano i dati
                  if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                        self.conn.commit()

                  # Ritorna i risultati solo per query di lettura
                  if query.strip().upper().startswith("SELECT"):
                        return self.cursor.fetchall()           
            except Exception as e:
                  print(f"error query {e}")

      def closeConn(self):
            if self.cursor:
                  self.cursor.close()
                  print("Cursore chiuso.")
            if self.conn:
                  self.conn.close()
                  print("Connessione chiusa.")


            