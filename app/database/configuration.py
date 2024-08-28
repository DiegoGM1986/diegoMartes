#datos para la conexion a BD

dataBaseName="diegodb"
userName="root"
userPassword=""
ConnectionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{ConnectionPort}/{dataBaseName}"

print()

