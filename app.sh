export LIBPATH=/usr/lib:/usr/lib64:$LIBPATH
export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:$LD_LIBRARY_PATH

# for running on OSX
virtualenv venv
source venv/bin/activate
pip install cx_Oracle
python app.py $@
RC=$?
echo "Program ended with RC $RC"
deactivate
exit $RC