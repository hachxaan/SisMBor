mysql -u admin -p123456 sismbordb -v < ../db/migration.v03/borrar_all_db_sismbordb.sql
rm OBTaller/migrations/0001_initial.py
python manage.py makemigrations
python manage.py migrate

echo "../db/migration.v03/definers_08062021.sql"
echo "-------------------------------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/definers_08062021.sql
echo "../db/migration.v03/views.sql"
echo "-------------------------------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/views.sql
echo "../db/migration.v03/parametros_iniciales.sql" 
echo "-------------------------------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/parametros_iniciales.sql
echo "../db/migration.v03/datos_desarrollo.sql"
echo "-------------------------------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/datos_desarrollo.sql
echo "../db/migration.v03/conceptos_desarrollo.sql"
echo "-------------------------------------------------------------------"

mysql -u admin -p123456 sismbordb  < ../db/migration.v03/conceptos_desarrollo.sql
echo "../db/migration.v03/unidades_desarrollo.sql"
echo "-------------------------------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/unidades_desarrollo.sql
echo "../db/migration.v03/set_id_base.sql"
echo "-------------------------------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/set_id_base.sql
echo "LISTO"
echo "-------------------------------------------------------------------"

python manage.py createsuperuser


