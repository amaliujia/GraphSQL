start=$SECONDS
python driver/driver.py degreedist test_data/soc-LiveJournal1.txt
#wait
echo $(( SECONDS - start ))
