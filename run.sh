start=$SECONDS
python driver/driver.py kcore test_data/soc-Slashdot0811.txt
#wait
echo $(( SECONDS - start ))
