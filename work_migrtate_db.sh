ssh /home/apipiltzin/DESARROLLOS/OscarBordon/V02/db/getLocalAll.sh

sh /home/apipiltzin/DESARROLLOS/OscarBordon/V02/db/migration.v03/dump/dump_store_triggers.sh
sh /home/apipiltzin/DESARROLLOS/OscarBordon/V02/db/migration.v03/dump/dump_views.sh
sh /home/apipiltzin/DESARROLLOS/OscarBordon/V02/db/migration.v03/dump/dump_parametros_iniciales.sh
sh /home/apipiltzin/DESARROLLOS/OscarBordon/V02/db/migration.v03/dump/dump_datos_desarrollo.sh

mysql -u admin -p123456 sismbordb -v < ../db/migration.v03/borrar_all_db_sismbordb.sql
rm OBTaller/migrations/0001_initial.py
python manage.py makemigrations
python manage.py migrate

echo "-------------------------------------------------------------------"
echo "-------------------------------------------------------------------"
echo "-------------------------------------------------------------------"
echo "../db/migration.v03/dump/scripts/dump_store_triggers.sh"
echo "-----------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/dump/scripts/stored_triggers.sql
echo "-------------------------------------------------------------------"
echo "../db/migration.v03/dump/scripts/views.sql"
echo "-------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/dump/scripts/views.sql
echo "-------------------------------------------------------------------"
echo "../db/migration.v03/dump/scripts/parametros_iniciales.sql" 
echo "----------------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/dump/scripts/parametros_iniciales.sql
echo "--------------------------------------------------------------------"
echo "../db/migration.v03/dump/scripts/datos_desarrollo.sql"
echo "-----------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/dump/scripts/datos_desarrollo.sql
echo "-------------------------------------------------------------------"

echo "../db/migration.v03/dump/scripts/superuser.sql"
echo "-----------------------------------------"
mysql -u admin -p123456 sismbordb  < ../db/migration.v03/dump/scripts/superuser.sql
echo "-------------------------------------------------------------------"


#echo "../db/migration.v03/categorias_desarrollo.sql"
#echo "----------------------------------------------"
#mysql -u admin -p123456 sismbordb  < ../db/migration.v03/categorias_desarrollo.sql
#echo "-------------------------------------------------------------------"
#echo "../db/migration.v03/conceptos_desarrollo.sql"
#echo "---------------------------------------------"
#mysql -u admin -p123456 sismbordb  < ../db/migration.v03/conceptos_desarrollo.sql
#echo "-------------------------------------------------------------------"
#echo "../db/migration.v03/unidades_desarrollo.sql"
#echo "--------------------------------------------"
#mysql -u admin -p123456 sismbordb  < ../db/migration.v03/unidades_desarrollo.sql
#echo "-------------------------------------------------------------------"
#echo "../db/migration.v03/personal_tipo_desarrollo.sql"
#echo "------------------------------------------------"
#mysql -u admin -p123456 sismbordb  < ../db/migration.v03/personal_tipo_desarrollo.sql
#echo "-------------------------------------------------------------------"
#echo "../db/migration.v03/set_id_base.sql"
#echo "-------------------------------------"
#mysql -u admin -p123456 sismbordb  < ../db/migration.v03/set_id_base.sql
#echo "-------------------------------------------------------------------"
echo "-------------------------------------------------------------------"
echo "-------------------------------------------------------------------"
echo "LISTO"
echo "-------------------------------------------------------------------"
echo "-------------------------------------------------------------------"
echo "-------------------------------------------------------------------"
#python manage.py createsuperuser


