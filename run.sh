start=$SECONDS
python driver/driver.py kcore test_data/soc-LiveJournal1.txt
#wait
echo $(( SECONDS - start ))
